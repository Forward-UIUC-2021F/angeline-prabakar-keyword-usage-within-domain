import mysql.connector as mysql
import pandas

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
disconnecting
'''
def disconnecting_sql(db, mycursor):
    pass

'''
mysql query to find the rows that have specific keyword
returns resulting rows
'''
def keyword_finder(mycursor, keyword):
    sql = "SELECT * FROM keyword_frequency_table WHERE keyword = %s"
    key = (keyword, )

    mycursor.execute(sql, key)

    myresult = mycursor.fetchall()

    return myresult

'''
mysql query to find the rows that have specific keyword and category
returns resulting rows
'''
def keyword_category_finder(mycursor, keyword, category):
    sql = "SELECT * FROM keyword_frequency_table WHERE keyword = %s and category_code = %s"
    search = (keyword, category)

    mycursor.execute(sql, search)

    myresult = mycursor.fetchall()

    return myresult

'''
mysql query to find the rows that have specific keyword and year
returns resulting rows
'''
def keyword_year_finder(mycursor, keyword, year):
    sql = "SELECT * FROM keyword_frequency_table WHERE keyword = %s and year = %s"
    search = (keyword, year)

    mycursor.execute(sql, search)

    myresult = mycursor.fetchall()

    return myresult

'''
takes resulting documents from user search keyword only and seperates by year and also category
'''
def year_cat_frequency(myresult):
    storing_cat = {}
    storing_year = {}
    for x in myresult:
        code = x['category_code']
        year_ = x['year']
        freq_ = int(x['frequency'])
        if code not in storing_cat:
            storing_cat[code] = freq_
        elif code in storing_cat:
            storing_cat[code] += freq_

        if year_ not in storing_year:
            storing_year[year_] = freq_
        elif year_ in storing_year:
            storing_year[year_] += freq_

    return storing_cat, storing_year


db, mycursor = connecting_sql()
another_keyword = 'y'


'''
prints out keyword data separated by year and category
'''
while (another_keyword == 'y'):
    ask_keyword = input("Provide keyword: ")
    ask_category = input("Provide category: ")
    ask_year = input("Provide year: ")
    another_keyword = input("Another keyword lookup?: ")

    if ask_category == "na" and ask_year == "na":
        myresult = keyword_finder(mycursor, ask_keyword)
        storing_cat, storing_year = year_cat_frequency(myresult)

        print()
        print(storing_cat)
        print('-------------------------------------------------')
        print(storing_year)
        print()





