from flask import Flask, render_template, request
import pickle
from inverted_indexer import Indexer

app = Flask(__name__)

indexer = Indexer()
indexer.load_ind('inverted_index.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    if not query:
        empty_query_msg = "Please enter a query."
        return render_template('index.html', empty_query_msg=empty_query_msg)
    else:
        results = indexer.search(query)
        if not results:
            no_results_msg = "No results found for '{}'".format(query)
            return render_template('results.html', query=query, no_results_msg=no_results_msg)
        else:
            return render_template('results.html', query=query, results=results, urls=indexer.urls)

if __name__ == '__main__':
    app.run(debug=True)