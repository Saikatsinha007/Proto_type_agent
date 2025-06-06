# 🧠 Multi-Agent Query Handler System

A lightweight, modular multi-agent system in Python + Streamlit that classifies and handles user queries (bugs, features, questions) with an orchestrator pattern — powered by rule-based logic and a Google Gemini-compatible API.

---

## 🚀 Features

* 🧠 Classifies queries into bugs, features, or questions
* 🔄 Orchestrator agent routes to appropriate handlers
* 💬 Developer agent simulates bug/feature resolution
* 🖥️ Interactive Streamlit UI
* 🪵 Centralized logging via utility function

---



## 📁 Project Structure

All core logic is implemented modularly but kept flat:

```
.
├── app.py                  # Streamlit UI
├── test_orchestrator.py    # CLI test runner
├── catalog_agent.py        # Classifies the query
├── developer_agent.py      # Handles bugs/features
├── orchestrator_agent.py   # Coordinates agents
├── utils.py                # Logging utility
└── README.md
```

---

## 🔑 API Configuration

Works with a Gemini-compatible OpenAI-style API.

Credentials used:

* API Key: "YOUR_API_KEY"
* Base URL: [https://generativelanguage.googleapis.com/v1beta/openai/](https://generativelanguage.googleapis.com/v1beta/openai/)

Already pre-configured in app.py and orchestrator\_agent.py

---

## 🧪 Run from CLI

```bash
python test_orchestrator.py
```

Sample Output:

```
Response: 🔧 Acknowledged bug: 'There's an error when I try to save the file.'. Generating fix...
```

---

## 🌐 Run Streamlit App

```bash
streamlit run app.py
```

Paste queries in the UI and see responses.

---

## 🧠 Example Inputs

| Input                                             | Type     | Agent Response                      |
| ------------------------------------------------- | -------- | ----------------------------------- |
| There's an error when I try to save the file.     | bug      | 🔧 Acknowledged bug...              |
| Please add dark mode support to the app.          | feature  | 🚀 Feature request noted...         |
| Can you help me set up two-factor authentication? | question | 🤖 Answering question (placeholder) |

---

## 🔧 What utils.py Does

The log\_action(agent, action, details) method prints structured logs with timestamps. Helps trace agent behavior.

---

## 🧱 How It Works

1. Orchestrator receives a user query.
2. CatalogAgent classifies it using rule-based keywords.
3. DeveloperAgent handles bugs or features.
4. Logs are printed for every step.

---

## 👥 Contributors

This system was built with the collaboration and contributions of:

* Adarsh Tiwari
* Dhyan Yajnik
* Nishant Naresh Dhotre
* Oppangi Poojita
* S Rajadhurai
* Sundram Jha
* Saikat Sinha
* Shyamli Thekke Cheriya

Thank you all for your help building this 🙌

