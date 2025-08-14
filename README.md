# 🎓 GenAI Final Project — RAG-Based Q&A Chatbot for MSADS

This repository contains the **front-end UI** for a Retrieval-Augmented Generation (RAG) chatbot, built as part of the GenAI final project at the University of Chicago. The chatbot provides conversational Q&A about the **MS in Applied Data Science (MSADS)** program.

This front-end is developed using **Streamlit**, and supports API integration with back-end retrieval and LLM modules.

> 📁 Project name: `genai-final`  
> 🧠 Role: UI & Integration Lead — Jiawei Yuan  
> 📅 Course: Generative AI, 2025 Summer

---

## 🚀 Features

- ✅ Streamlit web UI
- ✅ Multi-turn Q&A with conversation history
- ✅ Display citation links for retrieved answers
- ✅ “Clear conversation” button to reset
- ✅ Integrated with back-end API (or mock fallback)
- ✅ Deployable on [Streamlit Cloud](https://streamlit.io/cloud)

---

## 📂 Project Structure

```bash
genai-final/
├── genai_ui.py            # Main Streamlit front-end
├── requirements.txt       # Python dependencies
├── README.md              # This documentation
└── assets/                # (Optional) Demo screenshots


## 🖥️ Front-End UI Development: Role & Responsibilities

As the **UI & Integration Lead**, my responsibility was to develop a front-end interface for our RAG-based chatbot using **Streamlit**, enabling seamless interaction between users and the system.

### 🔑 Key Features

The interface was designed with user experience and modular integration in mind, and includes the following core functionalities:

- **User Input Field**: A minimal and accessible text input component where users can submit questions about the MSADS program.
- **Loading Animation**: A real-time visual indicator (`st.spinner`) to simulate the LLM’s "thinking process" while waiting for a response.
- **Answer Display with Citations**: Generated answers are clearly presented, along with citation links referencing the original content source (e.g., program webpages).
- **Clear Conversation Button**: A reset button is included to allow users to clear prior queries and restart the conversation at any time.
- **Multi-Turn Dialogue History**: Recent Q&A pairs are stored using `st.session_state` and displayed using collapsible components to simulate an ongoing chat experience.

### 🔌 API Integration Ready

The UI was engineered to support both **mock data** for testing and **live API responses** for full system integration. This enables a seamless transition from development to production, once the back-end retrieval and LLM modules are deployed.

### 🧱 Technical Stack

- **Language**: Python  
- **Framework**: Streamlit  
- **HTTP Requests**: `requests` library  
- **State Management**: `st.session_state`  
- **Deployment**: Compatible with [Streamlit Cloud](https://streamlit.io/cloud)

### 📦 Reusability & Deployment

The interface is modular, lightweight, and fully documented, with dependencies listed in `requirements.txt`. It is designed for easy deployment and reproducibility, allowing the team or future collaborators to launch the app locally or in the cloud with minimal setup.

### 🎯 Impact

The front-end transforms the back-end’s retrieval and generation capabilities into a practical, usable tool for real users — enabling interactive, conversational exploration of the MSADS program through a clean and intuitive web experience.

