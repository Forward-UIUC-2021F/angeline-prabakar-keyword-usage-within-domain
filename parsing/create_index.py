from typing import Dict, List, Sequence
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import MultifieldParser
from whoosh.filedb.filestore import RamStorage
from whoosh.analysis import StemmingAnalyzer
import json
import os, os.path
from whoosh import index
import whoosh.index as index
import tqdm
from tqdm import tqdm
from time import sleep
from tqdm import trange

class SearchEngine:

    '''
    creates a search engine with a schema of each document it might need to look through
    '''
    def __init__(self, schema):
        self.schema = schema
        schema.add('raw', TEXT(stored=True))
        if not os.path.exists("cs_domain_directory"):
            os.mkdir("cs_domain_directory")
        self.ix = index.create_in("cs_domain_directory", schema)

    '''
    adding documents from json file and storing it to be searched later
    currently committing documents one by one
    '''
    def index_documents(self, docs: Sequence):
    
        self.ix = index.open_dir("cs_domain_directory")
        writer = self.ix.writer()
    
        for doc in tqdm(docs):
                d = {k: v for k,v in doc.items() if k in self.schema.stored_names()}
                d['raw'] = json.dumps(doc) 
                writer.add_document(**d)

        tqdm(writer.commit())
        print("done")
        
    '''
    this is the total of documents that have been indexed.
    ''' 
    def get_index_size(self) -> int:
        self.ix = index.open_dir("cs_domain_directory")
        return self.ix.doc_count_all()

      

'''
creating a schema of what parts of the document to search through in the directory
'''
schema = Schema(
        id = ID(stored=True),
        title = TEXT(stored=True, analyzer=StemmingAnalyzer()),
        abstract = TEXT(stored=True, analyzer=StemmingAnalyzer()),
        categories = TEXT(stored=True, analyzer=StemmingAnalyzer()),

)


'''
f = open('data/filtered_arxiv.json',  "r")
  

#takes documents and converts to json

data = json.load(f)


#create SearchEngine object with new directory indexdir

engine = SearchEngine(schema)


#adding the documents into the newly created directory

engine.index_documents(data)


print(engine.get_index_size())
'''