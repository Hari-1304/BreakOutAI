import streamlit as st
import pandas as pd
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup
from io import BytesIO
import time

# Configure Gemini API
genai.configure(api_key="")  # Add your Gemini API key here
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to perform a web search and get top results
def web_search(query, num_results=3):
    search_url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }
    try:
        response = requests.get(search_url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            links = []
            for g in soup.find_all("div", class_="tF2Cxc")[:num_results]:
                title = g.find("h3").text if g.find("h3") else "No Title"
                link = g.find("a")["href"] if g.find("a") else "No Link"
                links.append({"title": title, "link": link})
            return links
    except Exception as e:
        st.write(f"Error during web search: {e}")
    return []

# Function to scrape the content of a webpage
def scrape_page_content(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")
            content = " ".join([p.get_text() for p in paragraphs])
            return content
    except Exception as e:
        return f"Error scraping {url}: {e}"
    return "No content found."

# Function to get structured insights from Gemini
def get_insights_with_gemini(context, prompt):
    try:
        full_prompt = f"Using the following context:\n{context}\n{prompt}"
        response = model.generate_content(full_prompt)
        return response.text if response else "Failed to generate insights."
    except Exception as e:
        return f"Error generating insights: {e}"

# Streamlit App
st.title("AI-Powered Web Insight Generator")
st.write("Upload a CSV, select a column, define a query prompt, and generate insights using web data and Gemini.")

# File Upload
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded File Preview:")
        st.dataframe(df)

        # Select column
        column_name = st.selectbox("Select the column to process", df.columns)

        # Define Prompt
        prompt_template = st.text_input("Enter a generic query template (use `{}` for entity)")

        # Process and Fetch Results
        if st.button("Run"):
            results = []
            progress = st.progress(0)

            for idx, entity in enumerate(df[column_name]):
                st.write(f"Processing: {entity}")
                query = prompt_template.format(entity)

                # Get Top 3 Results
                top_links = web_search(query)
                combined_content = ""
                if top_links:
                    for link in top_links:
                        page_content = scrape_page_content(link["link"])
                        combined_content += f"\nContent from {link['title']} ({link['link']}):\n{page_content}\n"

                # Generate Insights with Gemini
                insights = get_insights_with_gemini(combined_content, query)
                results.append({
                    "Entity": entity,
                    "Query": query,
                    "Web Results": combined_content if combined_content else "No results found",
                    "Gemini Insights": insights if insights else "No insights generated"
                })

                # Update progress bar
                progress.progress((idx + 1) / len(df[column_name]))

            # Create Results DataFrame
            result_df = pd.DataFrame(results)

            # Ensure no truncation of fields in DataFrame
            pd.set_option('display.max_colwidth', None)

            # Display Results
            st.write("Generated Results:")
            st.dataframe(result_df)

            # Save Results to CSV
            csv_data = BytesIO()
            result_df.to_csv(csv_data, index=False, quoting=1, escapechar='"', encoding="utf-8")
            csv_data.seek(0)

            # Streamlit Download Button
            st.download_button(
                label="Download Results as CSV",
                data=csv_data,
                file_name="insights_results.csv",
                mime="text/csv"
            )
    except Exception as e:
        st.write(f"Error processing file: {e}")
