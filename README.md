# Popularity of Keywords throughout the Years and Categories

# Overall Design 

## Overall Input: 
Main input is a user-inputted keyword.



## Overall Output: 
- Program should generate a timeline line graph of the relevancy of the keyword throughout the years. 
- Program should display a bar graph of the usage of the keyword within specific categories, generally Computer Science - related.
- Program should return year-frequency data of a keyword
- Program should return category-frequency data of a keyword
- Program should return comparison line graph for multiple keywords
- Program shouild return category information of specific Category ID's


## Example

- User Inputted Keyword: Bayesian Inversion

- Output for Timeline Line Graph: 
![Screenshot](https://github.com/Forward-UIUC-2021F/keyword-usage-within-domain/blob/master/images_readme/year_bayesian_inversion.png)

- Output for Category Bar Graph:
![Screenshot](https://github.com/Forward-UIUC-2021F/keyword-usage-within-domain/blob/master/images_readme/category_bayesian_inversion.png)

- User Inputted Keyword: Keyword Frequency

- Output for Timeline Line Graph:
![Screenshot](https://github.com/Forward-UIUC-2021F/keyword-usage-within-domain/blob/master/images_readme/year_keyword_frequency.png)

- Output for Category Bar Graph:
![Screenshot](https://github.com/Forward-UIUC-2021F/keyword-usage-within-domain/blob/master/images_readme/category_keyword_frequency.png)

- User Inputted Keywords: [‘data structure’, ‘machine learning’, ‘data mining’]

- Output Timeline Line Graph:
![Screenshot](https://github.com/Forward-UIUC-2021F/keyword-usage-within-domain/blob/master/images_readme/multiple_plots.png)

## Methodology:

### Using Whoosh and Indexing Arxiv Documents
 
Whoosh is a fast, featureful full-text indexing and searching library implemented in pure Python. Programmers can use it to easily add search functionality to their applications and websites. Every part of how Whoosh works can be extended or replaced to meet your needs exactly.

We can use Whoosh in order to access certain bits of information that we need. The input is the Documents from the Arxiv Dataset.


### Extracting Information from Whoosh Into SQL Database

We are trying to generate a timeline of a specific keyword. Using the Arxiv Dataset of CS Google Scholar articles, we can gather the abstract, the keyword, the year the document was uploaded, as well as the categories. After gathering this information, we can add it into a MySQL database.

In order to associate a keyword with each Scholar article we will use the abstract of each article. By iterating through the Scholar Dataset, we will determine what keywords appear in the abstract. From there, we will increment the keyword-year frequency. 

In order to generate other information, we will also note the categories that are associated with that specific keyword. Through doing this, we can determine the history of the usage of that keyword within that category.

### Database

We can create a database in order to generate a timeline of a specific keyword and other needed information. We can create a table with attributes of the keyword itself, the year, the category code, and it’s frequency. 
In order for the user to get more information of each of the categories, we can create another table with attributes of the category id, category type, category name, as well as it's abstracts. We obtain this from Cornell University's Arxiv's website.

For both of these operations, we will use MySQL as the database program. 

### Tables in Database With Fields

**CS_DOMAIN_KEYWORDS TABLE**
(Keyword, Year, Category Code, Frequency)

**ARXIV_TAXONOMY**
(Category ID, Category Type, Category Name, Abstract)

### Display using Plotly

"Plotly's Python graphing library makes interactive, publication-quality graphs. Examples of how to make line plots, scatter plots, area charts, bar charts, error bars, box plots, histograms, heatmaps, subplots, multiple-axes, polar charts, and bubble charts."

With the tables, we can display the information in different ways. We can use SQL's fetch function to search for rows of similar information and increment our counts as needed. With the keyword, year, and frequency, we can display it in a timeline line graph, similar to the Ngram Viewer. With the categories associated with the keyword, we can display it as a sort of bar graph.

For the line graph, if there are multiple lines present, each line is labeled and colored based on their keyword. As you move along the line, you can see the frequency associated with each year.

For the bar graph, it is ordered based on most popular category associated with the keyword to least, With every bar, it is color coded based on category type. Hovering over each category provides more information, if existing. If there are display issues present, running `display_category_information(category_id = CATEGORY CODE):` will print out full information of each category.

# Setup
To download the dependencies, you can run the following requirements.txt

```
pip install -r requirements.txt 
```

In order to use this module, you must also install MySQL workbench to keep track of the data since there is a lot. You can follow the instructions on https://dev.mysql.com/doc/workbench/en/wb-installing.html to download the workbench. Select what you're working on: Linux, MacOS, or Windows.


I used Visual Studio Code as a coding environment. To download Visual Studio code, follow the instructions here: https://code.visualstudio.com/download. Select what you're working on: Linux, MacOS, or Windows.


To create the first SQL table, I used the dataset here https://www.kaggle.com/Cornell-University/arxiv. Be sure to download it. 


To create the second SQL table, I created my own csv file with the necessary information. If included, it is in the data folder. Otherwise, this is the website I used for reference: https://arxiv.org/category_taxonomy

Fill in the correct db connection info at `searching/database_internal.py` in the `connecting_sql()` function. 

Since a majority of this module involves dealing with large sums of data in SQL, it was difficult to make physical test cases for the project. However, testing was involved as I coded the module. To run the current tests, you can just run the 'testing_user_functions.py' in the 'searching' folder. They were made testing bad inputs of the user functions.

**Here is the directory of the module**
```
angeline-prabakar-keyword-usage-within-domain/
    - requirements.txt
	- README.md
	- .gitignore
    - data/ 
        -- arxiv_category_taxonomy.json: category information for all types of categories in arxiv
        -- filtered_arxiv.json: articles in CS arxiv from Cornell
        -- Keywords_Springer.csv: keywords to use to search documents
		-- not_accounted_words.csv: keywords that were not found in CS arxiv dataset
    - images_readme/
        -- all images that are used in README.md
    - parsing/
    	-- adding_taxonomy.py: fetching categories from arxiv_category_taxonomy.json and adding to SQL
        -- create_index.py: adding documents from filtered_arxiv.json to Whoosh index
        -- open_index.py: searching Whoosh index and adding rows to SQL
    - searching/
    	-- checking_database.py: user functions for displaying graphs and returning data
    	-- database_internal.py: internal functions for checking_database functions
		-- testing_user_functions.py: testing user functions in checking_database
	- cs_domain_directory/
		-all the indexed documents/articles from Whoosh
	- videos/
		--demo_video.mp4: how user functions work
```

# Demo Video

![Video](https://github.com/Forward-UIUC-2021F/angeline-prabakar-keyword-usage-within-domain/blob/master/videos/demo_video.mp4)

# Functional Design
**Returning Categories-Frequency of a Keyword**
```
'''
given a keyword, returns a dictionary of category code and frequency for that keyword

arguments:
keyword - string of keyword to search

return:
category_frequency - dictionary of {category: frequency} for the given keyword
'''
```
```
def return_categories_for_keyword(keyword):
	#return category-frequency dictionary for given keyword
```
Example command in terminal
```
python3 -c "import searching.checking_database as check; print(check.return_categories_for_keyword(‘data mining’))"
```

**Returning Year-Frequency of a Keyword**
```
'''
given a keyword, returns a dictionary of years and frequency for that keyword

arguments:
keyword - string of keyword to search

return:
year_frequency - dictionary of {year: frequency} for the given keyword
'''
```
```
def return_years_for_keyword(keyword):
    #return year-frequency dictionary for given keyword
```
Example command in terminal
```
python3 -c "import searching.checking_database as check; print(check.return_years_for_keyword(‘data mining’))"
```

**Display Multiple Keyword Year Timelines**
```
'''
using multiple keywords, display multiple graphs for use of comparison

arguments:
keyword_list = formatted keywords like  list
ex. ['machine learning', 'data structure', 'data mining']

return:
displays multiple line graph for each keyword listed
'''
```
```
def display_multiple_year(keyword_list):
	#return multiple lines in single graph for each keyword listed
```
Example command in terminal
```
python3 -c "import searching.checking_database as check; print(check.display_multiple_year([‘data structure’, ‘machine learning’, ‘data mining’]))”
```

**Display Timeline for a Single Keyword**
```
'''
takes resulting year dictionary and creates simple graph

argument:
keyword - given keyword used to find year information

return:
displays line graph for keyword
'''
```
```
def display_year(keyword):
	#return line graph displaying timeline
```
Example command in terminal
```
python3 -c "import searching.checking_database as check; print(check.display_year(‘data mining’))"
```

**Display Popular Categories for a Single Keyword**
```
'''
takes keyword and creates simple graph of most popular categories of keyword

arguments:
keyword - given keyword used to find category information
num_bars - how many resulting bars you want in your graph

return:
display bar graph for most popular categories with description of given keyword and bar length
'''
```
```
def display_categories(keyword, num_bars):
	#return bar graph with user given number of bars
```
Example command in terminal
```
python3 -c "import searching.checking_database as check; print(check.display_categories(‘data mining’, 20))"
```

**Returning Category Information**
```
'''
user function
return category information for given category code id

arguments:
category_id - category code id to look up in sql

return:
if improper, returns possible sql category codes to search. if correct, returns category information
as a list of dictionaries
'''
```
```
def display_category_information(category_id):
	#return information as a json object
```

Example command in terminal
```
python3 -c "import searching.checking_database as check; print(check.display_category_information(‘cs.AR'))"
```

**Display All Possible Information**
```
'''
user function
takes keyword and displays all possible keyword information

arguments:
keyword - given keyword

return:
bar graph for categories, line graph for years, category-frequency, and year-frequency
'''
```
```
def return_all_keyword_information(keyword):
	#return all possible information about keyword.
```
Example command in terminal
```
python3 -c "import searching.checking_database as check; print(check.return_all_keyword_information('data mining'))"
```

# Algorithmic Design
*These are general functions of how the process works of storing in SQL, not the actual functions.*

### Whoosh Directory to SQL Database
- We can use the fields in Whoosh to store our documents

![Alt Text](https://github.com/Forward-UIUC-2021F/keyword-usage-within-domain/blob/fbfb0cd4160400a8d12e9ba8945ce718be663fb6/images_readme/Screen%20Shot%202021-09-24%20at%2012.26.09%20PM.png)

**Storing documents into Whoosh**
```
'''
adding arxiv documents/articles from json file and storing it to be searched for sql later
currently committing all parts of the document. commits documents one by one
'''

def index_documents(self, docs: Sequence):
	#loop through the csv file and gather each document and store it within Whoosh
	#adds each document from csv one by one and commits into whoosh's index
```

**Schema used to search Whoosh**
```
'''
creating a schema of what parts of the document to search through in the directory for sql
'''

schema = Schema(
        id = ID(stored=True),
        title = TEXT(stored=True, analyzer=StemmingAnalyzer()),
        abstract = TEXT(stored=True, analyzer=StemmingAnalyzer()),
        categories = TEXT(stored=True, analyzer=StemmingAnalyzer()),

)
```

**Searching Whoosh for associated articles with given keyword**
```
'''
function that searches whoosh for list of articles associated with a keyword

arguments:
words - list of words that had no results in whoosh
ix - directory for whoosh to search
schema - searching whoosh using these arguments
q - string keyword 
fields - associated with schema in whoosh search

return:
search_results - whoosh results from the keyword search
'''

def searching_whoosh(words, ix,  schema, q: str, fields: Sequence, highlight: bool=True) -> List[Dict]:
	#returns search_results
```

**Processing Search Results for SQL**
```
'''
taking search results and processing it to add to SQL
'''

def processing_search_results(search_results)
	#returns processed search results, ready for sql
```

**Adding row to SQL Database Table**
```
'''
function that adds the proper fields into the database table

arguments:
db - the database used for sql
mycursor - sql object
keyword - field 1 stored into sql
freq - field 2 stored into sql
year - field 3 stored into sql
category - field 4 stored into sql

return:
db - updated database with new record inserted
'''

def add_row_to_sql(db, mycursor, keyword, freq, year, category):
	#returns db
```

### Adding Taxonomy Information to SQL
**Adding row to SQL table**
```
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
	#loops through categories and adds one by one 
	#returns updated database
```

By the end, we will have a SQL table that holds the keyword, year, category code, and frequency. We will also have a table of the category information for all the categories of each keyword. With this table, we will create the visual diagrams of popularity of keywords within the CS domain. We can do this by using SQL's fetch function and incrementing the frequency counters for the categories as well as years associated with the keyword given.

### Using SQL Database to Output Proper Data
To output the visual graphs as well as the data of the keyword inserted, dictionaries were used. 

Using SQL's fetchall functions with the user's keyword, we iterate through the rows returned and increment the {category-frequency} as well as {year-frequency} dictionaries based on the frequency value of the row. With the {year-frequency} dictionary, we can translate the data into a line graph. However with the category graph, with each category returned for the kewyord, a Category_Bubble object was created.

```
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
		#initialize object
```

Using this newly made object, we can create a bar graph that provides extensive information about each popular category. 

# Issues and Future Work
Since the data is extensive and large, adding the documents to Whoosh as well as the SQL database took some time. 

- Importing Documents to Whoosh: ~3 hours
- Searching Whoosh for Documents associated with Keyword and adding to SQL table: ~85 hours
- Overall search time to display graphs and/or other information: ~10-15 seconds

Along with that, there is no code that has been implemented so far to find similar keywords for what you search. Make sure to type all your searches clearly.

While adding to SQL from Whoosh, we had keywords that returned no possible documents of association. They are inside `data/not_accounted_words.csv`. In the future, there are plans to process the keywords and try to see if there are any other ways to make association for search functionality. 

# Sources/References

### Cornell University Google Scholar Articles
https://www.kaggle.com/Cornell-University/arxiv 

### Filtered CS Papers JSON
https://serioussoftwa-lbh6237.slack.com/files/U027N51FQ58/F02CNDRN12L/filtered_arxiv.json

### Keywords CSV
https://serioussoftwa-lbh6237.slack.com/files/U027N51FQ58/F02BS30488N/keywords-springer-83k.csv

### Whoosh Library 
https://github.com/mchaput/whoosh

### Cornell University Taxonomy Archive
https://arxiv.org/category_taxonomy

### Plotly Python Open Source Graphing Library
https://plotly.com/python/


