import mysql.connector as mysql
import plotly.graph_objects as go
import collections
import random

import os
from dotenv import load_dotenv

load_dotenv()

'''
object for categories associated with a keyword

id - category code id
name - proper name of category code id
type - what larger general category it is under
abstract - small description
frequency - frequency associated with category of given keyword
'''
class Category_Bubble:
    def __init__(self, category_id, category_name, category_type, category_abstract, frequency):
        self.id = category_id
        self.name = category_name
        self.type =  category_type
        self.abstract = category_abstract
        self.frequency = frequency

'''
initializing connection and connector to database. making data readable as dictionary

return:
db - database for project
mycursor - object used to search sql
'''
def connecting_sql():
    # print("Yiuup", os.getenv('MYSQL_HOST'), os.getenv('MYSQL_USER'), os.getenv('MYSQL_PASS'), os.getenv('MYSQL_DB'))
    db = mysql.connect(
        host = os.getenv('MYSQL_HOST'),
        user = os.getenv('MYSQL_USER'),
        passwd = os.getenv('MYSQL_PASS'),
        database = os.getenv('MYSQL_DB')
    )
    mycursor = db.cursor(dictionary=True)

    return db, mycursor

'''
mysql query to find the rows that have specific keyword

arguments:
mycursor - object used to search sql
keyword - keyword used to search sql

return:
myresult - resulting rows with given keyword
'''
def keyword_finder(mycursor, keyword):
    sql = "SELECT * FROM cs_domain_keywords WHERE keyword = %s"
    key = (keyword, )

    mycursor.execute(sql, key)

    myresult = mycursor.fetchall()

    return myresult

'''
internal function
lowercases and strips whitespace from keyword

arguments:
keyword - keyword to clean

return:
myresult - cleaned keyword
'''
def clean_keyword(keyword):
    keyword = keyword.strip().lower()
    
    return keyword

'''
internal function
mysql query to find row that have specific taxonomy category

arguments:
mycursor - object used to search sql
category_id - the category id used to search sql

return:
myresult - resulting row with taxonomy information
'''
def taxonomy_finder(mycursor, category_id):
    sql = "SELECT * FROM arxiv_taxonomy WHERE id = %s"
    search = (category_id, )

    mycursor.execute(sql, search)

    myresult = mycursor.fetchall()

    return myresult

'''
generate color for graph

return:
color - color generated from random ints
'''
def color_generator():
    color1 = random.randint(0, 255)
    color2 = random.randint(0, 255)
    color3 = random.randint(0, 255)
    color = 'rgb(' + str(color1) + "," + str(color2) + "," + str(color3) + ")"
    return color


'''
internal function
using results from mysql, creates a dictionary of {year: frequency} for the given keyword

arguments:
myresults - search results from sql, rows formatted as a list

return:
year_frequency - dictionary of {year: frequency} for the given keyword
'''
def finding_year_frequency(myresults):
    year_frequency = {}
    for x in myresults:
        sql_year = x['year']
        sql_frequency = x['frequency']

        if sql_year not in year_frequency:
            year_frequency[sql_year] = sql_frequency
        elif sql_year in year_frequency:
            year_frequency[sql_year] += sql_frequency
    year_frequency = collections.OrderedDict(sorted(year_frequency.items()))
    return year_frequency

'''
internal function
using search results from mysql, creates a dictionary of {category: frequency} for the given keyword

arguments:
myresults - search results from sql, rows formatted as a list

return:
category_frequency - dictionary of {category: frequency} for the given keyword
'''
def finding_category_frequency(myresults):
    category_frequency = {}
    for x in myresults:
        sql_cat = x['category_code']
        sql_frequency = x['frequency']

        if sql_cat not in category_frequency:
            category_frequency[sql_cat] = sql_frequency
        elif sql_cat in category_frequency:
            category_frequency[sql_cat] += sql_frequency
    category_frequency = {k: v for k, v in sorted(category_frequency.items(), key=lambda item: item[1], reverse = True)}
    return category_frequency

'''
internal function
using search results from mysql, creates dictionaries of {category: frequency}, {year: frequency}
    for the given keyword simultaneously

arguments:
myresults - search results from sql, rows formatted as a list

return:
category_frequency - dictionary of {category: frequency} for the given keyword
year_frequency - dictionary of {year: frequency} for the given keyword
'''
def finding_year_cat_frequency(myresults):
    category_frequency = {}
    year_frequency = {}
    for x in myresults:
        sql_cat = x['category_code']
        sql_year = x['year']
        sql_frequency = int(x['frequency'])

        if sql_cat not in category_frequency:
            category_frequency[sql_cat] = sql_frequency
        elif sql_cat in category_frequency:
            category_frequency[sql_cat] += sql_frequency

        if sql_year not in year_frequency:
            year_frequency[sql_year] = sql_frequency
        elif sql_year in year_frequency:
            year_frequency[sql_year] += sql_frequency

    category_frequency = {k: v for k, v in sorted(category_frequency.items(), key=lambda item: item[1], reverse = True)}
    year_frequency = collections.OrderedDict(sorted(year_frequency.items()))

    return category_frequency, year_frequency

'''
internal function
appending category objects to list

arguments:
category_frequency - dictionary of {category: frequency} for the given keyword

return:
list of category objects
'''
def creating_category_object_list(category_frequency):
    db, mycursor = connecting_sql()
    category_object_list = []

    for category_id in category_frequency:
        category_information = taxonomy_finder(mycursor, category_id)
        cat_code_frequency = category_frequency[category_id]
        category_object = creating_category_object(category_information, category_id, cat_code_frequency)
        category_object_list.append(category_object)
        
    return category_object_list

'''
internal function
creating category object with info about category of a given keyword

arguments:
category_information - results from taxonomy sql, length should be 1 or 0
category_id - category code
frequency - frequency of given category

return:
newly created category object storing info about each category for given keyword
'''
def creating_category_object(category_information, category_id, frequency):
    if len(category_information) == 0:
        category_object = Category_Bubble(category_id, "NAN", "NAN", "NAN", frequency)
    else:
        category_name = category_information[0]['category_name']
        category_type = category_information[0]['category_type']
        category_abstract = category_information[0]['abstract']
        category_object = Category_Bubble(category_id, category_name, category_type, category_abstract, frequency)
    
    return category_object

