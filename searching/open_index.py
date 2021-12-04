from typing import Dict, List, Sequence
from whoosh.fields import *
from whoosh.qparser import MultifieldParser
from whoosh.analysis import StemmingAnalyzer

import json
from whoosh import index, query
import whoosh.index as index
import csv
import ast
import re

import datetime
from datetime import datetime
import mysql.connector as mysql


'''
initializing connection and connector to database. making data readable as dictionary
'''
def connecting_sql():
    db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    database = "keyword_frequency"
    )
    mycursor = db.cursor(dictionary=True)

    return db, mycursor

'''
function that searches whoosh for list of documents associated with a keyword
'''
def query(ix,  schema, q: str, fields: Sequence, highlight: bool=True) -> List[Dict]:
        search_results = []
        with ix.searcher() as searcher:
            results = searcher.search(MultifieldParser(fields, schema=schema).parse(q), limit=None)
            for r in results:
                d = json.loads(r['raw'])
                if highlight:
                    for f in fields:
                        if r[f] and isinstance(r[f], str):
                            d[f] = r.highlights(f) or r[f]

                search_results.append(d)

        return search_results

'''
going through dictionary and adding key value terms
'''
def adding_dictionary(db, mycursor, keyword, keyword_dictionary):
    for entry in keyword_dictionary:
        year = entry[1]
        category = entry[0]
        freq = keyword_dictionary[entry]
        
        db = add_row_to_sql(db, mycursor, keyword, freq, year, category)

'''
function that adds the proper fields into the database table
'''
def add_row_to_sql(db, mycursor, keyword, freq, year, category):
    sql = "INSERT INTO cs_keyword (keyword, year, category_code, frequency) VALUES (%s, %s, %s, %s)"
    val = (keyword, year, category, freq)
    mycursor.execute(sql, val)
    db.commit()

    print()
    print(keyword)
    print()
    print(mycursor.rowcount, "record inserted.")

    return db

'''
function that prints tables for checking
'''
def print_tables(mycursor):
    mycursor.execute("SHOW TABLES")

    for x in mycursor:
        print(x)

    pass

'''
function that prints databases for checking
'''    
def print_databases(mycursor):
    mycursor.execute("SHOW DATBASES")

    for x in mycursor:
        print(x)
    
    pass

'''
formatting year from json object so it's proper int year
'''    
def formatting_year(year_string):
    datetime_object = datetime.strptime(year_string, '%a, %d %b %Y %H:%M:%S %Z')
    year = int(datetime_object.year)
    return year

'''
formatting categories from json object so it's proper list of categories
'''  
def formatting_categories(cs_categories):
    cs_categories = "['" + re.sub(" ", "','", cs_categories) + "']"
    categories = ast.literal_eval(cs_categories)
    return categories


'''
places to search for the keyword
'''
schema = Schema(
        id = ID(stored=True),
        title = TEXT(stored=True, analyzer=StemmingAnalyzer()),
        abstract = TEXT(stored=True, analyzer=StemmingAnalyzer()),
        categories = TEXT(stored=True, analyzer=StemmingAnalyzer()),
)


db, mycursor = connecting_sql()

'''
opening the cs directory to access whoosh documents
'''
ix = index.open_dir("cs_domain_directory")

'''
using the keywords to search the title and abstract
'''
fields_to_search = ["title", "abstract", "categories"]


'''
opening the keywords csv file and checking each keyword for related documents
'''

with open("data/Keywords-Springer-83K.csv", 'r') as keywords_csv_file:
    keywords_csv = csv.reader(keywords_csv_file, delimiter=',')
    count = 0
    for row in keywords_csv:
        count += 1
        keyword = row[0]
        print(f"Keyword:: " + keyword)
        #using query function above to find related documents
        return_results = query(ix, schema, keyword, fields_to_search, highlight=True)
        
        #gathering specific info from each document found
        keyword_dictionary = {}
        for x in return_results:

            cs_categories = formatting_categories(x['categories'])
            year_created = formatting_year(x['versions'][0]['created'])

            #frequency counter 
            for x in cs_categories:
                if (x, year_created) not in keyword_dictionary:
                    keyword_dictionary[(x, year_created)] = 1
                else:
                    keyword_dictionary[(x, year_created)] += 1

        adding_dictionary(db, mycursor, keyword, keyword_dictionary)

'''
return_results = query(ix, schema, "machine learning", fields_to_search, highlight=True)
for x in return_results:
    print(x)
    print()
        
print(len(return_results))
'''
