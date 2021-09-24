# Design

## Overall Input: 
Main input is a user-inputted keyword.

## Overall Output: 
Program should generate a timeline of the relevancy of the keyword throughout the years. Along with that, the program should display a bar graph of the usage of the keyword within specific categories within CS.

### Example: 
	User Inputted Keyword: Data Structure
	Output:
  
  
 ## Methodology:

### External Library: Whoosh
 
Whoosh is a fast, featureful full-text indexing and searching library implemented in pure Python. Programmers can use it to easily add search functionality to their applications and websites. Every part of how Whoosh works can be extended or replaced to meet your needs exactly.

We can use Whoosh in order to access certain bits of information that we need. The input is the Documents from the Arxiv Dataset.



### Extracting Information

We are trying to generate a timeline of a specific keyword. Using the Arxiv Dataset of CS Google Scholar articles, we can gather the abstract, the keyword, the year the document was uploaded, as well as the categories. After gathering this information, we can move it into a separate csv file.

In order to associate a keyword with each Scholar article we will use the abstract of each article. By iterating through the Scholar Dataset, we will determine what keywords appear in the abstract. From there, we will increment the keyword-year frequency. 

In order to generate other information, we will also note the categories that are associated with that specific keyword. Through doing this, we can determine the history of the usage of that keyword within that category.

### Database 
We can create a database in order to generate a timeline of a specific keyword and other needed information. We can create a table with attributes of the keyword itself, the year, and the frequency. In order to determine the frequency of a keyword in a specific category, we can also create another table that stores the keyword, category, and it’s frequency.

For both of these operations, we will use MySQL as the database program.

### Tables Included

- Keyword, Year, Frequency
- Keyword, Category, Frequency

### Display

With both tables, we can display them in different ways. With the keyword, year, and frequency, we can display it in a timeline, similar to the Ngram Viewer. With the categories associated with the keyword, we can display it as a sort of bar graph.


