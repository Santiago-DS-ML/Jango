# 🤖 JANGO — AI Chatbot with Streamlit & Gemini

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue?logo=google)
![LLM](https://img.shields.io/badge/AI-Large%20Language%20Model-green)

JANGO is a conversational AI chatbot built with **Streamlit** and powered by **Google Gemini**. This project demonstrates how to integrate a Large Language Model (LLM) into a web application while maintaining conversation history and providing a smooth streaming user experience.

---

# 🚀 Features

- 💬 Interactive chatbot interface
- 🧠 Google Gemini integration
- ⚡ Real-time response streaming
- 📝 Conversation history management
- ⚙️ Adjustable generation parameters
  - Temperature
  - Maximum output tokens
- 🗑️ One-click conversation reset
- 🎨 Clean and responsive Streamlit interface

---

# 🛠 Technologies

- Python
- Streamlit
- Google Gemini API
- google-genai SDK

---

# 🔑 Configuration

Create a `.streamlit/secrets.toml` file:

```toml
GEMINI_API_KEY="YOUR_API_KEY"
```

---

# ▶️ Run locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run chatbot_2.py
```

---

# 🎯 Learning Objectives

This project helped me understand how to:

- Build a conversational interface with Streamlit
- Integrate an LLM through an API
- Manage chat history using `st.session_state`
- Stream responses token by token
- Configure generation parameters
- Design a user-friendly chatbot interface

---

# 🚀 Next Steps

Future improvements include:

- 📄 Retrieval-Augmented Generation (RAG)
- 📚 PDF knowledge base
- 🔎 Semantic search with embeddings
- 🗃️ Vector database integration
- 🌐 Multi-document support
- 🖼️ Image understanding (Multimodal AI)

---

## 👨‍💻 Author

**APPIA ELIE**

AI • Machine Learning • Data Science • Computer Vision • NLP

Passionate about building practical AI solutions that solve real-world problems.
