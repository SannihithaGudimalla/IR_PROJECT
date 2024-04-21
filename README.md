**INFORMATION RETRIEVAL (CS-429)**

**PROJECT - Submitted by Sannihitha Gudimalla (A20560248)**

This project aims to develop a sophisticated search engine leveraging Python technologies. It includes components for web crawling, indexing, and query processing, providing users with a scalable, efficient, and user-friendly search solution capable of retrieving relevant information.

**Abstract**
The project utilizes Python technologies such as Scrapy for web crawling, Scikit-Learn for indexing, and Flask for query processing. The primary objectives include scalability, efficiency, user experience, and accuracy in search results.

**Objectives**
Scalability: Developed a system capable of handling large-scale web crawling and indexing operations.
Efficiency: Implemented algorithms and techniques for indexing and retrieval to optimize resource utilization.
User Experience: Designed a user-friendly interface for submitting queries and viewing search results.
Accuracy: Ensured highly relevant search results ranked according to similarity to the user's query.

**Development Process**
The development process follows a systematic approach, including requirements gathering, design, implementation, testing, and deployment.

**Key Features**
Web Crawling: Scrapy-based crawler for fetching web pages and extracting content.
Indexing: Scikit-Learn-based indexer constructs an inverted index for efficient search.
Query Processing: Flask-based processor handles user queries and retrieves relevant documents.
User Interface: Provides a user-friendly interface with features such as autocomplete and result pagination.

**Future Directions**
Semantic Search: Explore advanced techniques like word embeddings and neural network-based models.
Personalization: Implement personalized search functionality based on user preferences.
Multimedia Search: Extend the search engine to support multimedia content.
Integration: Integrate with external APIs, databases, and services.
Feedback Mechanism: Implement a feedback mechanism for continuous improvement.

**Architecture**
The system comprises web crawler, indexer, and query processor components, which interact through well-defined APIs.

**Operation**
Commands for running the web crawler, indexer, query processor, and unit tests are provided. Python 3.10+ and dependencies such as Scrapy, Scikit-Learn, and Flask are required for installation.
**Commands to run this project**: 
•	Running the web crawler: **scrapy crawl WebSpider**
•	Running the web crawler and saving the crawled results into a json file:
    **scrapy crawl WebSpider -o JSONOutput.json**
•	Running the indexer: **python inverted_indexer.py**
•	Running the query processor: **python app.py**
•	Running unit tests: **python testcases.py**


**Conclusion**
The project demonstrates the effectiveness of Scrapy, Scikit-Learn, and Flask in building a scalable and robust search system. Further enhancements and optimizations can be explored for improved performance and scalability.

**Data Sources**
Web pages crawled from various domains across the internet serve as the primary source of content for indexing and query processing.

**Test Cases**
A comprehensive suite of unit tests covers functionalities of the web crawler, indexer, and query processor modules which are written in testcases.py file.

**Source Code**
The source code comprises modules and files for the web crawler, indexer, query processor, and unit tests.

**Bibliography**
References and resources used in the development process are listed in the project report.

