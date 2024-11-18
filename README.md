# BreakOutAI

This project uses web scraping, Streamlit, and Gemini to create an AI-powered online insight generator. To provide insights based on online material, users can construct a query template, upload a CSV file, and choose a column to process.

Key features:
Uploading a CSV file allows users to add entities, such as company names, keywords, and so on.
Column Selection: Users have the option to pick a particular column from the CSV file to process after uploading it.
Prompt Template: The chosen object can be used to substitute a placeholder ({}) in a query template that users construct.
Web Search: The program does a Google search for every entity and obtains the top three search results (links).
Web scraping: To give context for creating insights, the application extracts material from the retrieved web pages, particularly paragraphs.
Gemini Insights: Based on the context and user-specified query prompt, the application integrates the scraped material and produces structured insights using Gemini's generative model.
Progress Indicator: The software displays real-time progress as it processes each object.
Results Display: Following the processing of every entity, the entity, query, web results, and created insights are shown in a table.
Downloadable CSV: The results are available to users as a CSV file.

Execution Flow: 
The user uploads a CSV file and selects a column.
They define a query template (e.g., "What is the latest news about {}?").
The app searches the web for the top results for each entity in the column.
It scrapes the content from these results and feeds the combined text into Gemini for insight generation.
After processing all entities, the results are displayed in a table.
The user can download the results in CSV format.

