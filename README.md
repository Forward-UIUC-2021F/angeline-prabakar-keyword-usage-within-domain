# Creating Timeline of Keywords

#Overall Design 

## Overall Input: 
Main input is a user-inputted keyword.



## Overall Output: 
Program should generate a timeline of the relevancy of the keyword throughout the years. Along with that, the program should display a bar graph of the usage of the keyword within specific categories within CS.


## Example

- User Inputted Keyword: Data Structure
- Output:

![Screenshot](https://github.com/Forward-UIUC-2021F/keyword-usage-within-domain/blob/fbfb0cd4160400a8d12e9ba8945ce718be663fb6/images_readme/Screen%20Shot%202021-08-26%20at%2011.08.00%20PM.png)

![Screenshot](https://github.com/Forward-UIUC-2021F/keyword-usage-within-domain/blob/fbfb0cd4160400a8d12e9ba8945ce718be663fb6/images_readme/Screen%20Shot%202021-09-10%20at%204.25.32%20PM.png)

- User Inputted Keyword: Machine Learning
- Output:

![Screenshot](https://github.com/Forward-UIUC-2021F/keyword-usage-within-domain/blob/fbfb0cd4160400a8d12e9ba8945ce718be663fb6/images_readme/Screen%20Shot%202021-08-26%20at%2011.51.09%20PM.png)




## Methodology:

### Whoosh
 
Whoosh is a fast, featureful full-text indexing and searching library implemented in pure Python. Programmers can use it to easily add search functionality to their applications and websites. Every part of how Whoosh works can be extended or replaced to meet your needs exactly.

We can use Whoosh in order to access certain bits of information that we need. The input is the Documents from the Arxiv Dataset.


### Extracting Information

We are trying to generate a timeline of a specific keyword. Using the Arxiv Dataset of CS Google Scholar articles, we can gather the abstract, the keyword, the year the document was uploaded, as well as the categories. After gathering this information, we can add it into a MySQL database.

In order to associate a keyword with each Scholar article we will use the abstract of each article. By iterating through the Scholar Dataset, we will determine what keywords appear in the abstract. From there, we will increment the keyword-year frequency. 

In order to generate other information, we will also note the categories that are associated with that specific keyword. Through doing this, we can determine the history of the usage of that keyword within that category.

### Database 

We can create a database in order to generate a timeline of a specific keyword and other needed information. We can create a table with attributes of the keyword itself, the year, the category code, and it’s frequency. 

For both of these operations, we will use MySQL as the database program. 

### Table With Fields

Keyword, Year, Category Code, Frequency

### Display

With the table, we can display them in different ways. We can use SQL’s group by function to display the two different outputs. With the keyword, year, and frequency, we can display it in a timeline, similar to the Ngram Viewer. With the categories associated with the keyword, we can display it as a sort of bar graph.






# Functional Design

- user can pass in a keyword within CS domain within a given year and find frequency. if no frequency for that year, return closest frequency
```
def get_frequency_of_year(keyword, year):
	#return frequency of a keyword in a given year
```

- user can pass in a keyword within CS domain and a category code to find the frequency it appears.
```
def get_frequency_of_category(keyword, category_code):
	#return frequency of a given keyword in a specific category
```

- display visual timeline of keywords throughout the years
```
def display_timeline(keyword):\
	#return graph
```

- display visual graph of keywords and their relevance within a given category
```
def display_category_usage(keyword):
	#return graph
```


# Algorithmic Design

### External Library: Whoosh
- We can use the fields in Whoosh to store our documents

![Alt Text](https://github.com/Forward-UIUC-2021F/keyword-usage-within-domain/blob/fbfb0cd4160400a8d12e9ba8945ce718be663fb6/images_readme/Screen%20Shot%202021-09-24%20at%2012.26.09%20PM.png)

### DataSet: Keywords, Arxiv Scholar Papers 


- storing each document from dataset into Whoosh
```
def store_documents() :
	#loop through the csv file and gather each document and store it within Whoosh
	#each document has fields to fill in: gather title, abstract, year created, and category code.
```

- simple function that just recreates file of original keywords csv for more readability
```
def clean_keywords():
	#loop through csv file and take out unnecessary information that comes in keywords file.
	#just creates a new csv file to work with
 ```

- adding data into SQL table for given keyword. uses helper functions
```
def assign_keyword_frequencies():
	#loop through keyword csv file and search using Whoosh functionality. 
	#for each keyword, call `search_keyword_documents(keyword)` to receive document list that have that keyword
	#pass document list into  `create_table_data(document_list)` to get the graph object that holds the list of keyword objects(name, year, category, frequency)
	#append values in MySQL table
 ```
 
- returns a list of documents from whoosh library that includes that specific keyword
```
def search_keyword_documents(keyword):
#using input keyword, search Whoosh created index library for documents that contain that keyword. Must search the Document’s abstract.
#return document objects in a list
```

- creates objects in order to add to SQL table
```
def create_table_data(document_list):
	#create a graph_object (just holds list of keyword objects)
	#loop through input document_list which includes the keyword. if the year does not previously exist in the list as well as the category code, create a new keyword object and add it to the graph object. if it does, find the keyword object in the graph object and increment the frequency counter of the object.
	#return graph object
 ```

By the end, we will have a SQL table that holds the keyword, year, category code, and frequency. With this table, we will create the visual diagrams of popularity of keywords within the CS domain.

# Sources/References

### Cornell University Google Scholar Article
https://www.kaggle.com/Cornell-University/arxiv 

### Filtered CS Papers JSON
https://serioussoftwa-lbh6237.slack.com/files/U027N51FQ58/F02CNDRN12L/filtered_arxiv.json

### Keywords CSV
https://serioussoftwa-lbh6237.slack.com/files/U027N51FQ58/F02BS30488N/keywords-springer-83k.csv




