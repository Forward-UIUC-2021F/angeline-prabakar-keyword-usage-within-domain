# Functional Design 

If given a group of papers, or documents, and keywords of a certain Domain, this will be able to output the popularity of those keyword within that domain.

## External Library:
Whoosh
## DataSet: Keywords, Arxiv Scholar Papers 

Whoosh is a fast, featureful full-text indexing and searching library implemented in pure Python. Programmers can use it to easily add search functionality to their applications and websites. Every part of how Whoosh works can be extended or replaced to meet your needs exactly.

## Source:
https://github.com/mchaput/whoosh



## Gathering Data For MySQL Tables:
```
#storing each document from dataset into Whoosh

def store_documents() :
	#loop through the csv file and gather each document and store it within Whoosh
	#each document has fields to fill in: gather title, abstract, year created, and category code.`
```

```
#simple function that just recreates file of original keywords csv for more readability

def create_keywords():
	#loop through csv file and take out unnecessary information that comes in keywords file.
	#just creates a new csv file to work with
```

```
#finding frequency for keywords. uses helper functions

def assign_keyword_frequencies():
	#loop through newly created keyword csv file and search using Whoosh functionality. 
	#for each keyword, call `search_keyword_documents(keyword)` to receive document list that have that keyword
	#pass document list into  `keyword_year_frequency(document_list)` and `keyword_catcode_frequency(keyword)` to get dictionary lists of {year, frequency} and {code, frequency}.
	#pass those values into `create_keyword_frequency_csv(keyword, year, frequency)` and `create_keyword_code_frequency(keyword, code, frequency):`
```

```	
#returns a list of documents from whoosh library that includes that specific keyword

def search_keyword_documents(keyword):
    #using input keyword, search Whoosh created index library for documents that contain that keyword. Must search the Document’s abstract.
    #return document objects in a list
```

```
#creates a dictionary of year and frequency values of specific keyword

def keyword_year_frequency(document_list):
	#create a dictionary of type {int : int}. This will store the year, and its frequency.
	#loop through input document_list which include the word. if the year does not previously exist in the dictionary, add new entry. If it does, increment frequency counter.
	#return dictionary with year and frequency values
```

```
#creates a dictionary of code and frequency values of specific keyword

def keyword_catcode_frequency(document_list):
	#create a dictionary of type {string : int}. This will store the category code, and its frequency.
	#loop through input document_list. if the category does not previously exist in the dictionary, add new entry. If it does, increment frequency counter.
	#return dictionary with category code and frequency values
```
	
```
#adding values into csv file to create SQL table in future

def create_keyword_frequency_csv(keyword, year, frequency):
	#appends keyword, year, frequency value into keyword_year csv file
```

```
#adding values into csv file to create SQL table in future

def create_keyword_code_frequency(keyword, code, frequency):
	#appends keyword, code, frequency into keyword_code csv file
```


by the end, will have 2 newly created csv files to add into MySQL tables. One table will be keyword, year, frequency. another will be keyword, category code, frequency. Will use these to create visual diagrams of popularity of keywords within CS domain.

