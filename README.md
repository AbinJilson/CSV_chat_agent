# CSV Question Answering App

This application allows you to upload a CSV file, apply filters, and ask questions about your data in natural language.

## Setup

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Set up your OpenAI API Key:**
    *   Create a file named `.env` in the root of the project directory.
    *   Add your OpenAI API key to the `.env` file like this:
        ```
        OPENAI_API_KEY='your_api_key_here'
        ```

## How to Run

1.  Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2.  Open your web browser and navigate to the URL provided by Streamlit.

3.  Upload your CSV file.

4.  Use the sidebar to filter your data.

5.  Type your question in the text area and click "Get Answer".
