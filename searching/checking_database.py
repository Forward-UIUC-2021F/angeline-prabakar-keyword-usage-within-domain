import searching.database_internal as searcher
import mysql.connector as mysql
import plotly.graph_objects as go


'''
user function
given a keyword, returns a dictionary of category code and frequency for that keyword

arguments:
keyword - string of keyword to search

return:
category_frequency - dictionary of {category: frequency} for the given keyword
'''
def return_categories_for_keyword(keyword):
    #case checking input
    if type(keyword) != str:
        return "Input is not a String"

    keyword = searcher.clean_keyword(keyword)
    db, mycursor = searcher.connecting_sql()
    myresults = searcher.keyword_finder(mycursor, keyword)

    #case if keyword is mispelled or incorrect
    if len(myresults) == 0:
        return "Spelled improperly or no data exists for keyword."

    category_frequency = searcher.finding_category_frequency(myresults)

    return category_frequency

'''
user function
given a keyword, returns a dictionary of years and frequency for that keyword

arguments:
keyword - string of keyword to search

return:
year_frequency - dictionary of {year: frequency} for the given keyword
'''
def return_years_for_keyword(keyword):
    #case checking input
    if type(keyword) != str:
        return "Input is not a String"

    keyword = searcher.clean_keyword(keyword)
    db, mycursor = searcher.connecting_sql()
    myresults = searcher.keyword_finder(mycursor, keyword)

    #case if keyword is mispelled or incorrect
    if len(myresults) == 0:
        return "Spelled improperly or no data exists for keyword."

    year_frequency = searcher.finding_year_frequency(myresults)

    return year_frequency

'''
user function
using multiple keywords, display multiple graphs for use of comparison

arguments:
keyword_list = formatted keywords like  list
ex. ['machine learning', 'data structure', 'data mining']

return:
displays multiple line graph for each keyword listed
'''
def display_multiple_year(keyword_list):
    db, mycursor = searcher.connecting_sql()

    #case if incorrect list stated
    if type(keyword_list) != list:
        return "Not proper list included."
    elif len(keyword_list) < 1:
        return "Not proper list included."
    



    fig = go.Figure()
    for keyword in keyword_list:

        #case if incorrect list stated
        if type(keyword) != str:
            return str(keyword) + " is not accurate keyword."

        myresults = searcher.keyword_finder(mycursor, keyword)
        #case if keyword is mispelled or incorrect
        if len(myresults) == 0:
            return "Spelled improperly or no data exists for keyword."

        year_frequency = searcher.finding_year_frequency(myresults)

        keyword_new = keyword.replace(" ", "+")
        color = searcher.color_generator()

        fig.add_trace(go.Scatter(x=list(year_frequency.keys()), y=list(year_frequency.values()),
            line=dict(color=color, width=4), name=keyword_new))

    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', connectgaps=True,
        marker_line_width=1.5, opacity=0.6)
    fig.update_layout(title ='Year Frequencies for ' + str(keyword_list), xaxis_title = 'YEAR',
        yaxis_title = 'FREQUENCY')

    fig.show()

'''
user function
takes resulting year dictionary and creates simple graph

argument:
keyword - given keyword used to find year information

return:
displays line graph for keyword
'''
def display_year(keyword):
    #case checking input
    if type(keyword) != str:
        return "Input is not a String"

    keyword = searcher.clean_keyword(keyword)
    db, mycursor = searcher.connecting_sql()

    myresults = searcher.keyword_finder(mycursor, keyword)

    #case if keyword is mispelled or incorrect
    if len(myresults) == 0:
        return "Spelled improperly or no data exists for keyword."

    year_frequency = searcher.finding_year_frequency(myresults)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(year_frequency.keys()), y=list(year_frequency.values()),
        line=dict(color='royalblue', width=4)))
    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', connectgaps=True,
        marker_line_width=1.5, opacity=0.6)
    fig.update_layout(title='Year Frequencies for ' + keyword.upper(), xaxis_title = 'YEAR',
        yaxis_title = 'FREQUENCY')

    fig.show()


'''
user function
takes keyword and creates simple graph of most popular categories of keyword

arguments:
keyword - given keyword used to find category information
num_bars - how many resulting bars you want in your graph

return:
display bar graph for most popular categories with description of given keyword and bar length
'''
def display_categories(keyword, num_bars):
    #case checking input
    if type(keyword) != str:
        return "Input is not a String"

    keyword = searcher.clean_keyword(keyword)
    db, mycursor = searcher.connecting_sql()
    myresults = searcher.keyword_finder(mycursor, keyword)

    #case if keyword is mispelled or incorrect
    if len(myresults) == 0:
        return "Spelled improperly or no data exists for keyword."

    category_frequency = searcher.finding_category_frequency(myresults)
    category_object_list = searcher.creating_category_object_list(category_frequency)

    #case if num_bars doesn't fit bounds
    if int(num_bars) == 0 or num_bars > len(category_object_list):
        return ("Improper bar length given. Given keyword " + keyword + " has " + 
        str(len(category_object_list)) + ".")

    x_list = []
    y_list = []
    hover_text = []
    hover_name = []
    count = 0
    color_list = []
    colors_to_use = {}

    for category_object in category_object_list:
        x_list.append(category_object.id)
        y_list.append(category_object.frequency)
        hover_text.append(('ID: {id}<br>'+
                        'Name: {name}<br>'+
                        'Type: {type}<br>'+
                        'Abstract: {abstract}').format(id=category_object.id,
                                                name=category_object.name,
                                                type=category_object.type,
                                                abstract=category_object.abstract))
        hover_name.append(category_object.name)

        if category_object.type not in colors_to_use:
            colors_to_use[category_object.type] = searcher.color_generator()
            color_list.append(colors_to_use[category_object.type])
        else:
            color_list.append(colors_to_use[category_object.type])

        count += 1
        if count == int(num_bars):
            break

    fig = go.Figure(data=[go.Bar(x=x_list, y=y_list,
        hovertext=hover_text, text = hover_name, marker_color=color_list)])

    fig.update_traces(marker_line_width=1.5, opacity=0.6)
    fig.update_layout(hoverlabel=dict(bgcolor="white", font_size=8, font_family="Rockwell"),
        title='Category Frequencies for ' + keyword.upper(), xaxis_title = 'CATEGORIES',
         yaxis_title = 'FREQUENCY')

    fig.show()

'''
user function
takes keyword and displays all possible keyword information

arguments:
keyword - given keyword

return:
bar graph for categories, line graph for years, category-frequency, and year-frequency
'''
def return_all_keyword_information(keyword):
    #case checking input
    if type(keyword) != str:
        return "Input is not a String"

    keyword = searcher.clean_keyword(keyword)
    db, mycursor = searcher.connecting_sql()
    myresults = searcher.keyword_finder(mycursor, keyword)

    #case if keyword is mispelled or incorrect
    if len(myresults) == 0:
        return "Spelled improperly or no data exists for category ID."

    category_frequency, year_frequency = searcher.finding_year_cat_frequency(myresults)
    category_object_list = searcher.creating_category_object_list(category_frequency)

    num_bars = 15
    if (num_bars > len(category_frequency)):
        num_bars = len(category_frequency)

    x_list = []
    y_list = []
    hover_text = []
    hover_name = []
    count = 0
    color_list = []
    colors_to_use = {}

    for category_object in category_object_list:
        x_list.append(category_object.id)
        y_list.append(category_object.frequency)
        hover_text.append(('ID: {id}<br>'+
                        'Name: {name}<br>'+
                        'Type: {type}<br>'+
                        'Abstract: {abstract}').format(id=category_object.id,
                                                name=category_object.name,
                                                type=category_object.type,
                                                abstract=category_object.abstract))
        hover_name.append(category_object.name)

        if category_object.type not in colors_to_use:
            colors_to_use[category_object.type] = searcher.color_generator()
            color_list.append(colors_to_use[category_object.type])
        else:
            color_list.append(colors_to_use[category_object.type])

        count += 1
        if count == int(num_bars):
            break

    fig = go.Figure(data=[go.Bar(x=x_list, y=y_list,
        hovertext=hover_text, text = hover_name, marker_color=color_list)])

    fig.update_traces(marker_line_width=1.5, opacity=0.6)
    fig.update_layout(hoverlabel=dict(bgcolor="white", font_size=8, font_family="Rockwell"),
        title='Category Frequencies for ' + keyword.upper(), xaxis_title = 'CATEGORIES',
         yaxis_title = 'FREQUENCY')

    fig.show()

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=list(year_frequency.keys()), y=list(year_frequency.values()),
        line=dict(color='royalblue', width=4)))
    fig2.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', connectgaps=True,
        marker_line_width=1.5, opacity=0.6)
    fig2.update_layout(title='Year Frequencies for ' + keyword.upper(), xaxis_title = 'YEAR',
        yaxis_title = 'FREQUENCY')

    fig2.show()

    return category_frequency, year_frequency




'''
user function
return category information for given category code id

arguments:
category_id - category code id to look up in sql

return:
if improper, returns possible sql category codes to search. if correct, returns category information
as a list of dictionaries
'''
def display_category_information(category_id):
    #case checking input
    if type(category_id) != str:
        return "Input is not a String"

    db, mycursor = searcher.connecting_sql()
    category_infomation = searcher.taxonomy_finder(mycursor, category_id)

    if len(category_infomation) == 0:
        print("Category does not exist or is mispelled. Returning possible categories to search.")

        mycursor.execute("SELECT category_code FROM arxiv_taxonomy")
        myresults = mycursor.fetchall()

        return myresults
    else:
        return category_infomation