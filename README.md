# 📬 Email Assistant using GenAI

An intelligent email assistant that connects to your email inbox, reads emails from a specified date range, and generates a concise summary and useful insights using Generative AI frameworks. Designed to help you stay on top of important conversations and reduce email overload.

Developed by [Sachin Verma](https://github.com/sacvik)

---

## 🚀 Features

- 🔗 Connects to your email inbox (e.g., Gmail, Outlook) via IMAP  
- 📅 Fetches emails from a user-defined number of past days  
- 🧠 Uses GenAI (LLM frameworks like OpenAI, Hugging Face, etc.) to:  
  - Summarize email content  
  - Extract action items, meetings, and follow-ups  
  - Identify key contacts and topics  
  - Highlight unread or high-priority threads  
- 📊 Provides a structured and user-friendly report  

---

## 🧰 Tech Stack

- **Python 3.8+**
- **IMAPClient / IMAPlib** – for reading emails
- **email / mailparser / bs4** – for parsing email content
- **LangChain / LlamaIndex** – for integrating LLMs
- **OpenAI / Hugging Face Transformers** – for generating summaries
- **Streamlit / Gradio**  – for a simple UI (optional)
- **Docker** – for containerized deployment (optional)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/email-assistant-genai.git
cd email-assistant-genai
pip install -r requirements.txt
```

---

## 🔑 Setup

1. **Environment Variables:**

Create a `.env` file in the root directory and add:

```env
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_app_password_or_token
IMAP_SERVER=imap.gmail.com
OPENAI_API_KEY=your_openai_key

```

> 💡 For Gmail users: Make sure IMAP is enabled in your Gmail settings and use an App Password if 2FA is enabled.

---

## 🛠️ Usage

```bash
python main.py --days 7
```

This will:

- Connect to your inbox
- Read emails from the last 7 days
- Generate summaries and insights
- Save the report to `output/report_<timestamp>.md`

You can also launch a UI:

```bash
streamlit run app.py
```

---

## 🧠 GenAI Models Used

- Summarization: `gpt-4` / `mistral-7b` / `bart-large-cnn`
- Insight Extraction: Prompt-based LLM reasoning via LangChain
- Optional vector store for semantic email search (e.g., FAISS)

---

## ✅ To-Do

- [ ] OAuth 2.0 support for secure login
- [ ] Daily/weekly scheduled reports
- [ ] Multi-account support
- [ ] Export to PDF or Notion

---

## 🛡️ Security & Privacy

- No email data is stored permanently
- All processing is done locally or securely on the cloud
- Credentials are kept in `.env` and never hard-coded

---

## 🤝 Contributing

Pull requests and suggestions are welcome! To contribute:

```bash
git checkout -b feature/your-feature
git commit -m "Add new feature"
git push origin feature/your-feature
```

## ⚙️ GenAI Backend Options

To keep this project open-source and free to run, the default setup uses a **local Ollama server** with models like `mistral`, `llama3`, or `phi` for email summarization and insight generation.

```bash
ollama run mistral
```

However, if preferred or for better performance, the summarization engine can be switched to cloud-based LLMs like **OpenAI's GPT-4** or **Anthropic's Claude** by configuring the relevant API keys in the `.env` file.

Simply modify the model provider section in your config or code as follows:

```python
# Example switch
use_openai = True  # set to False to use Ollama locally
```

> 🔁 This modular design allows seamless switching between local and cloud models depending on your needs.
