# BreakOutAI

This project uses web scraping, Streamlit, and Gemini to create an AI-powered online insight generator. To provide insights based on online material, users can construct a query template, upload a CSV file, and choose a column to process.

**SETUP**:
* install streamlit, pandas, google-generativeai, requests, beautifulsoup4.
* An API key has be generated prior to the execution of the project(i.e., from Gemini API)

**USER GUIDE**:

1. Run the Streamlit App 
* After setting up the app on your local machine, launch it using the following command:
**"streamlit run app.py"**.
*This will open the app in your browser (usually at http://localhost:8501).

2. Upload Your CSV
Click the "Upload CSV" button to upload a CSV file containing the entities you want to process.
The CSV should have one or more columns, and you will select a specific column to process.

3. Select a Column
After uploading the CSV, choose a column from the dropdown list that contains the entities you want to process. Each row in the column will be treated as a separate entity (e.g., a company name, a keyword, etc.)

4. Define a Query Template
You need to define a query template where {} is a placeholder for the entity. For example:
Query Template: "What are the latest news about {}?"
If the selected entity is "Apple", the query would be: "What are the latest news about Apple?"

5.Click "Run"
After defining the query template, click the "Run" button to start processing.
Scrape the content from those search results.
Generate insights using Gemini based on the scraped content.
Display the results in a table with columns for entity, query, web results, and generated insights.

6. Review and Download Results
After processing is complete, you can review the generated insights in the table.
You can also download the results as a CSV file by clicking the "Download Results as CSV" button.


**THIRD-PARTY API'S AND TOOLS USED**:
1. Google Gemini API
Purpose: Used for generating AI-powered insights based on the context provided (scraped web content and query).
API Setup: You must create an account with Google Gemini and obtain an API key to use it in the app.
Sign up and get the API key from: Google Gemini

2.Requests Library
Purpose: Used for sending HTTP requests to scrape web pages and interact with APIs.

3.BeautifulSoup (from bs4)
Purpose: Used for parsing HTML content and extracting specific data (such as text in paragraphs) from web pages.

4.Pandas
Purpose: Used to handle and manipulate the CSV data (reading, selecting columns, storing results).

5.Streamlit
Purpose: Provides the web interface for uploading the CSV, defining the query, and displaying the results.

**KEY FEATURES**:
Uploading a CSV file allows users to add entities, such as company names, keywords, and so on.
Column Selection: Users have the option to pick a particular column from the CSV file to process after uploading it.
Prompt Template: The chosen object can be used to substitute a placeholder ({}) in a query template that users construct.
Web Search: The program does a Google search for every entity and obtains the top three search results (links).
Web scraping: To give context for creating insights, the application extracts material from the retrieved web pages, particularly paragraphs.
Gemini Insights: Based on the context and user-specified query prompt, the application integrates the scraped material and produces structured insights using Gemini's generative model.
Progress Indicator: The software displays real-time progress as it processes each object.
Results Display: Following the processing of every entity, the entity, query, web results, and created insights are shown in a table.
Downloadable CSV: The results are available to users as a CSV file.


