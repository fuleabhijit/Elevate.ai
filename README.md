# Elevate.ai
# AI Analyst Chat Assistant

A multi-agent AI assistant that leverages advanced LLMs (Groq/OpenAI) and specialized tools to provide web search, financial data, and analysis in a structured, markdown-rich format.

---

## Features

- **Multi-Agent Architecture:**  
  - **Web Agent:** Searches the web and summarizes information with sources.
  - **Finance Agent:** Fetches and analyzes financial data (stock prices, fundamentals, analyst recommendations).
- **LLM Powered:** Uses Groq's Llama-3.3-70b-versatile model for high-quality responses.
- **Tool Integration:**  
  - DuckDuckGo for web search.
  - Yahoo Finance for real-time financial data.
- **Markdown Output:** All responses are formatted in markdown for readability.
- **Environment Variable Support:** Secure API key management via `.env`.
- **Streamlit Web App:** User-friendly web interface for interactive Q&A.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/fuleabhijit/AI-Analyst-Chat.git
cd AI-Analyst-Chat
```

### 2. Create and Activate a Virtual Environment (Recommended)

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r Backend/requirements.txt
pip install streamlit python-dotenv  # If not already in requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the root or `Backend/` directory with the following content:

```
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here  # If using OpenAI
```

---

## Usage

### Run the Streamlit Web App

From the project root or the `Backend/` directory, run:

```bash
streamlit run Backend/main.py
```

- The app will open in your browser.
- Enter your question in the text area and click "Get Answer" to receive a detailed, markdown-formatted response.

### Run the Multi-Agent Assistant (CLI)

```bash
cd Backend
python multiagents.py
```

The script will execute a sample query comparing Apple and Microsoft in terms of stock fundamentals and public sentiment.

### Customizing Queries (CLI)

Edit the last line in `Backend/multiagents.py` to change the query, for example:

```python
agent_team.print_response("Analyze companies like Tesla, Apple and suggest which to buy for long term")
```

---

## Project Structure

```
Agno Project/
│
├── app.py
├── Backend/
│   ├── main.py         # Streamlit web app
│   ├── multiagents.py  # Multi-agent CLI script
│   └── requirements.txt
└── venv/
```

---

## Example Output (Web App)

- Enter a question like:
  > What is data science? Tell me its advantages, uses, and future.

- The app will display a detailed, exam-ready answer in markdown format.

---

## Example Output (CLI)

```
## Stock Fundamentals Comparison

| Metric      | Apple | Microsoft |
|-------------|-------|-----------|
| ...         | ...   | ...       |

## Public Sentiment (Last Month)

- Apple: Mostly positive, driven by ...
- Microsoft: Mixed, due to ...

## Sources

- [Yahoo Finance](https://finance.yahoo.com)
- [DuckDuckGo Search](https://duckduckgo.com)
```

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License

[MIT](LICENSE) (or specify your license)

---

## Acknowledgements

- [Groq](https://groq.com/)
- [OpenAI](https://openai.com/)
- [DuckDuckGo](https://duckduckgo.com/)
- [Yahoo Finance](https://finance.yahoo.com/)
