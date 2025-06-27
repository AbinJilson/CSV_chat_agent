# 📊 CSV Chat Agent

<div align="center">
  <p>🤖 An intelligent chat interface that lets you interact with your CSV data using natural language queries powered by OpenAI's GPT models.</p>
  
  [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
  [![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
</div>

## ✨ Features

- **Natural Language Queries**: Ask questions about your data in plain English
- **Interactive Data Exploration**: Filter and explore your CSV files visually
- **Smart Data Analysis**: Get insights and summaries from your data
- **User-Friendly Interface**: Simple and intuitive web interface built with Streamlit
- **Secure**: Your API keys and data stay private on your machine

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AbinJilson/CSV_chat_agent.git
   cd CSV_chat_agent
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables:
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY='your-api-key-here'
     ```
     
     > 🔒 **Security Note**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

## 🖥️ Usage

1. Start the application:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

3. Upload your CSV file using the file uploader

4. Use the sidebar to apply filters to your data (optional)

5. Type your question in the chat interface and click "Get Answer"

## 📝 Example Queries

- "What are the top 5 highest values in column X?"
- "Show me the average of column Y grouped by column Z"
- "What is the correlation between columns A and B?"
- "Generate a summary of the data"
- "Find all rows where column C is greater than 100"

## 🛠️ Dependencies

- [Streamlit](https://streamlit.io/) - For the web interface
- [LangChain](https://python.langchain.com/) - For building the AI agent
- [OpenAI](https://openai.com/) - For natural language processing
- [Pandas](https://pandas.pydata.org/) - For data manipulation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with ❤️ using amazing open source tools
- Inspired by the need for more accessible data analysis tools
- Special thanks to the OpenAI and Streamlit communities
