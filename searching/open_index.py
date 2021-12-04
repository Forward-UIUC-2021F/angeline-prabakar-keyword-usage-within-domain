from typing import Dict, List, Sequence
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import MultifieldParser
from whoosh.filedb.filestore import RamStorage
from whoosh.analysis import StemmingAnalyzer

import json
import os, os.path
from whoosh import index, query
import whoosh.index as index
from whoosh.qparser import QueryParser
import csv
import ast


import datetime
from datetime import date
from datetime import datetime


'''
function that searches whoosh for list of documents associated with a keyword
'''
def query(ix,  schema, q: str, fields: Sequence, highlight: bool=True) -> List[Dict]:
        search_results = []
        with ix.searcher() as searcher:
            results = searcher.search(MultifieldParser(fields, schema=schema).parse(q))
            for r in results:
                d = json.loads(r['raw'])
                if highlight:
                    for f in fields:
                        if r[f] and isinstance(r[f], str):
                            d[f] = r.highlights(f) or r[f]

                search_results.append(d)

        return search_results

'''
places to search for the keyword
'''
schema = Schema(
        id = ID(stored=True),
        title = TEXT(stored=True, analyzer=StemmingAnalyzer()),
        abstract = TEXT(stored=True, analyzer=StemmingAnalyzer()),
        categories = TEXT(stored=True, analyzer=StemmingAnalyzer()),

)

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

        num_documents = len(return_results)
        
        
        #gathering specific info from each document found
        for x in return_results:
            print("Keyword: " + keyword)
            print(x)
            print()

            cs_categories = x['categories']
            year_created = x['versions'][0]['created']


            print(cs_categories)
            print(year_created)

            print("-"*100)
        if count == 10:
            break

        

