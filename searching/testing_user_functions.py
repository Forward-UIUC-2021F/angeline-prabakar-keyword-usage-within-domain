import database_internal as searcher
import checking_database as check
import mysql.connector as mysql
import plotly.graph_objects as go
import collections
import random

'''
testing for all bad inputs of user functions
'''

assert sum([1, 2, 3]) == 6, "Should be 6"

def test_category_object():
    freq = 35
    cat_object = searcher.Category_Bubble("astro-ph.HE", "High Energy Astrophysical Phenomena", "Astrophysics", 
    "Cosmic ray production, acceleration, propagation, detection. Gamma ray astronomy and bursts, X-rays, charged particles, supernovae and other explosive phenomena, stellar remnants and accretion systems, jets, microquasars, neutron stars, pulsars, black holes",
    freq)

    category_freq = {"astro-ph.HE": freq}

    final_list = searcher.creating_category_object_list(category_freq)
    comp_cat_object = final_list[0]

    assert comp_cat_object.id == cat_object.id 
    print("pass1")
    assert comp_cat_object.name == cat_object.name
    print("pass2")
    assert comp_cat_object.type == cat_object.type
    print("pass3")
    assert comp_cat_object.abstract == cat_object.abstract
    print("pass4")
    assert comp_cat_object.frequency == cat_object.frequency
    print("pass5")


def test_display_multiple_year():
    wrong_list = [3,4,5]
    return_message = check.display_multiple_year(wrong_list)

    assert return_message == "3 is not accurate keyword."
    print('pass6')

    wrong_list = 'hello'
    return_message = check.display_multiple_year(wrong_list)
    assert return_message == "Not proper list included."
    print('pass7')

    wrong_list = []
    return_message = check.display_multiple_year(wrong_list)
    assert return_message == "Not proper list included."
    print('pass8')


def test_display_year():
    wrong_keyword = []
    return_message = check.display_year(wrong_keyword)

    assert return_message == "Input is not a String"
    print('pass9')

    wrong_keyword = "mchune learning"
    return_message = check.display_year(wrong_keyword)
    assert return_message == "Spelled improperly or no data exists for keyword."
    print('pass10')

def test_return_categories_for_keyword():
    wrong_keyword = []
    return_message = check.return_categories_for_keyword(wrong_keyword)
    assert return_message == "Input is not a String"
    print('pass11')

    wrong_keyword = 'call trses'
    return_message = check.return_categories_for_keyword(wrong_keyword)
    assert return_message == "Spelled improperly or no data exists for keyword."
    print('pass12')

def test_return_years_for_keyword():
    wrong_keyword = 4
    return_message = check.return_years_for_keyword(wrong_keyword)
    assert return_message == "Input is not a String"
    print('pass13')

    wrong_keyword = 'call trses'
    return_message = check.return_years_for_keyword(wrong_keyword)
    assert return_message == "Spelled improperly or no data exists for keyword."
    print('pass14')

def test_display_categories():
    wrong_keyword = 4
    return_message = check.display_categories(wrong_keyword, wrong_keyword)
    assert return_message == "Input is not a String"
    print('pass15')

    keyword = 'data structure'
    wrong_num = 600
    return_message = check.display_categories(keyword, wrong_num)
    assert return_message == "Improper bar length given. Given keyword data structure has 154."
    print('pass16')


if __name__ == "__main__":
    test_category_object()
    test_display_multiple_year()
    test_display_year()
    test_return_categories_for_keyword()
    test_return_years_for_keyword()
    test_display_categories()

    print("Everything passed")
