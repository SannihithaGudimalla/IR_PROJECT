import unittest
from unittest.mock import Mock
from PROJECT.spiders.WebSpider import WebspiderSpider
from inverted_indexer import Indexer
from app import app

class TestWebCrawler(unittest.TestCase):
    def test_crawl_web_pages(self):
        # Initializing the web crawler
        crawler = WebspiderSpider()

        # Defining seed URLs for testing
        seed_urls = ['https://www.splashlearn.com/blog/friendship-quotes-for-kids/',
                  'https://www.amazon.com/',                  
                  'https://en.wikipedia.org/wiki/Lion',
                  'https://www.goodreads.com/quotes/tag/life-experience',
                  'https://www.rei.com/c/backpacks',
                  'https://www.patagonia.com/shop/luggage-travel-duffel-bags',
                  'https://www.randomactsofkindness.org/kindness-quotes',
                  'https://www.jewelosco.com/',
                  'https://www.ashleyfurniture.com/c/furniture/living-room/sofas/reclining-sofas/']

        # Using Mock response object
        mock_response = Mock()

        # Calling the parse method and checking if web pages are crawled
        for self.url in seed_urls:
            response = crawler.parse(mock_response)
            self.assertIsNotNone(response)

    def test_follow_links(self):
        # Initializing the web crawler
        crawler = WebspiderSpider()

        # Defining seed URLs with links for testing
        seed_urls = ['https://www.splashlearn.com/blog/friendship-quotes-for-kids/',
                  'https://www.amazon.com/',                  
                  'https://en.wikipedia.org/wiki/Lion',
                  'https://www.goodreads.com/quotes/tag/life-experience',
                  'https://www.rei.com/c/backpacks',
                  'https://www.patagonia.com/shop/luggage-travel-duffel-bags',
                  'https://www.randomactsofkindness.org/kindness-quotes',
                  'https://www.jewelosco.com/',
                  'https://www.ashleyfurniture.com/c/furniture/living-room/sofas/reclining-sofas/']

        # usigMock response object
        mock_response = Mock()

        # Call the parse method and check if links are followed
        for self.url in seed_urls:
            response = crawler.parse(mock_response)
            self.assertTrue(response)

class TestIndexer(unittest.TestCase):
    def test_indexing_documents(self):
        # Initialize the indexer
        indexer = Indexer()

        # Provide sample documents for testing
        sample_documents = [{'url': 'https://www.example.com/page1', 'content': 'Sample content 1'},
                            {'url': 'https://www.example.com/page2', 'content': 'Sample content 2'}]

        # Append documents to the indexer
        for doc in sample_documents:
            indexer.append_docs(doc['url'], doc['content'])

        # Create the inverted index
        indexer.create_inverted_index()

        # Check if the inverted index is constructed accurately
        self.assertIsNotNone(indexer.tfidf_matrix)

    def test_search_query(self):
        # Initialize the indexer
        indexer = Indexer()

        # Load sample inverted index (assuming it's already created)
        indexer.load_ind('inverted_index.pkl')

        # Provide a sample query for testing
        query = "sample query"

        # Execute the search
        results = indexer.search(query)

        # Check if relevant documents are returned with correct relevance scores
        self.assertTrue(results)

class TestQueryProcessor(unittest.TestCase):
    def test_submit_query(self):
        # Initialize the Flask app
        app.testing = True
        client = app.test_client()

        # Submit a sample query through the web interface
        response = client.post('/search', data={'query': 'sample query'})

        # Check if the response status code indicates success
        self.assertEqual(response.status_code, 200)

    def test_empty_query(self):
        # Initialize the Flask app
        app.testing = True
        client = app.test_client()

        # Submit an empty query through the web interface
        response = client.post('/search', data={'query': ''})

        # Check if an appropriate error message is displayed
        self.assertIn(b'Please enter a query', response.data)

if __name__ == '__main__':
    unittest.main()
