import csv
import json
import os, os.path

import mysql.connector as mysql

'''
all functions are internal
'''

'''
initializing connection and connector to database. making data readable as dictionary

return:
db - database for project
mycursor - object used to search sql
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
function that adds the proper fields into the database table

arguments:
db - database being used 
category_id - 1st field for taxonomy table
category_type - 2nd field for taxonomy table
category_name - 3rd field for taxonomy table
abstract -  4th field for taxonomy table

return:
db - database with new category inserted
'''
def add_category_to_sql(db, mycursor, category_id, category_type, category_name, abstract):
    sql = "INSERT INTO arxiv_taxonomy (id, category_type, category_name, abstract) VALUES (%s, %s, %s, %s)"
    val = (category_id, category_type, category_name, abstract)
    mycursor.execute(sql, val)
    db.commit()

    print()
    print(category_id)
    print()
    print(mycursor.rowcount, "record inserted.")

    return db

#creating database object and sql object
db, mycursor = connecting_sql()

#opening taxonomy file
f = open('data/arxiv_category_taxonomy.json',  "r")
  

#takes documents and converts to json
data = json.load(f)

#adds each line as a catgeory into sql
for x in data:
    category_id = x['id']
    category_type = x['type']
    category_name = x['name']
    abstract = x['abstract']
    db = add_category_to_sql(db, mycursor, category_id, category_type, category_name, abstract)

