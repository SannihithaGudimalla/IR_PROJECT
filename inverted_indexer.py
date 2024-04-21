import pickle
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Indexer:

    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.documents = []
        self.urls = []

    # appending the url and content 
    def append_docs(self, url, content):
         self.urls.append(url)
         self.documents.append(content)

    # creating index
    def create_inverted_index(self):
         self.tfidf_matrix = self.vectorizer.fit_transform(self.documents)

    # saving the index into pickle file
    def save_ind(self, filename):
        with open(filename, "wb") as f:
            pickle.dump((self.vectorizer,self.tfidf_matrix, self.urls),f)

    # loading the index
    def load_ind(self,filename):
        with open(filename, "rb") as f:
            self.vectorizer,self.tfidf_matrix, self.urls = pickle.load(f)

    # computing the scores
    def search(self, query, k=8):
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        # Check if all scores are zero which indicate no matches
        if not any(scores):
            return []
        top_k_indices = scores.argsort()[-k:][::-1]
        return [(self.urls[i], scores[i]) for i in top_k_indices]

    
if __name__ == '__main__':
        indexer = Indexer()
        with open('JSONOutput.json','r', encoding='utf-8') as f:
             data = json.load(f)
             for item in data:
                  indexer.append_docs(item['url'], item['content'])


        indexer.create_inverted_index()
        indexer.save_ind('inverted_index.pkl')    

    