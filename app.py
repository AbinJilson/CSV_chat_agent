import streamlit as st
import pandas as pd
from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

def main():
    st.set_page_config(page_title="Ask questions to your CSV", page_icon="🤖")
    st.title("Ask questions to your CSV 🤖")

    # Load API key from .env file
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        st.error("OpenAI API key not found. Please create a .env file and add your OPENAI_API_KEY.")
        return

    # Initialize session state variables
    if "df" not in st.session_state:
        st.session_state.df = None
    if "last_uploaded_filename" not in st.session_state:
        st.session_state.last_uploaded_filename = None
    if "filters" not in st.session_state:
        st.session_state.filters = {}

    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

    # Process file only if it's new
    if uploaded_file is not None:
        if uploaded_file.name != st.session_state.last_uploaded_filename:
            try:
                st.session_state.df = pd.read_csv(uploaded_file)
                st.session_state.last_uploaded_filename = uploaded_file.name
                st.session_state.filters = {}  # Reset filters for new file
            except Exception as e:
                st.error(f"Error reading CSV file: {e}")
                st.session_state.df = None

    if st.session_state.df is not None:
        df = st.session_state.df
        st.write("**Data Preview:**")
        with st.expander("Click to expand/collapse"):
            st.dataframe(df, use_container_width=True)

        categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
        numerical_cols = df.select_dtypes(include=['number']).columns.tolist()

        st.sidebar.header("Filter Data")
        
        current_filters = {}
        for col in categorical_cols:
            unique_values = df[col].unique().tolist()
            default_selection = st.session_state.filters.get(col, [])
            selected_values = st.sidebar.multiselect(f"Filter by {col}", unique_values, default=default_selection)
            current_filters[col] = selected_values

        for col in numerical_cols:
            min_val, max_val = float(df[col].min()), float(df[col].max())
            default_range = st.session_state.filters.get(col, (min_val, max_val))
            selected_range = st.sidebar.slider(f"Filter by {col}", min_val, max_val, value=default_range)
            current_filters[col] = selected_range
        
        st.session_state.filters = current_filters

        # Apply filters
        filtered_df = df.copy()
        for col, values in st.session_state.filters.items():
            if col in categorical_cols and values:
                filtered_df = filtered_df[filtered_df[col].isin(values)]
            elif col in numerical_cols:
                min_val, max_val = float(df[col].min()), float(df[col].max())
                if values != (min_val, max_val):
                    filtered_df = filtered_df[(filtered_df[col] >= values[0]) & (filtered_df[col] <= values[1])]

        st.write("**Filtered Data Preview:**")
        with st.expander("Click to expand/collapse"):
            st.dataframe(filtered_df, use_container_width=True)

        user_question = st.text_area("Ask your question:")

        if st.button("Get Answer"):
            if not user_question:
                st.error("Please enter a question.")
                return

            with st.spinner("Thinking..."):
                try:
                    temp_csv_path = "temp_filtered_data.csv"
                    filtered_df.to_csv(temp_csv_path, index=False)

                    llm = ChatOpenAI(model="gpt-4.1", temperature=0, openai_api_key=openai_api_key)
                    agent = create_csv_agent(
                        llm,
                        temp_csv_path,
                        verbose=True,
                        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                        allow_dangerous_code=True
                    )
                    
                    # Get the response from the agent
                    response = agent.invoke(user_question)
                    
                    # Format the response for better display
                    st.subheader("Answer:")
                    if isinstance(response, dict) and 'output' in response:
                        # If response is a dictionary with an 'output' key
                        st.write(response['output'])
                    elif isinstance(response, str):
                        # If response is a string
                        st.write(response)
                    else:
                        # For any other response type, convert to string
                        st.write(str(response))
                    
                    # Show the agent's thought process if available
                    if hasattr(agent, 'intermediate_steps') and agent.intermediate_steps:
                        with st.expander("View reasoning steps"):
                            for i, step in enumerate(agent.intermediate_steps, 1):
                                st.write(f"**Step {i}:**")
                                st.json(step)  # Display each step as JSON for better readability

                    os.remove(temp_csv_path)

                except Exception as e:
                    st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
