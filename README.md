# 🤖 Local Command-Line Chatbot using Hugging Face

A lightweight, terminal-based chatbot built using Hugging Face's `distilgpt2` model. It supports context-aware, multi-turn conversations using a sliding window memory buffer — all running locally without any GPU or external API.

---

## 📌 Features

- 🔄 **Multi-turn memory** (last 3 user-bot interactions)
- ⚡ **Fast and lightweight** – uses `distilgpt2`
- 💻 **Fully local** – no need for internet or API keys
- 🧩 **Modular code structure** for readability and maintainability
- 💬 **Command-line interface (CLI)** with graceful `/exit` support

---

## 🛠️ Project Structure

```

chatbot-project/
├── model\_loader.py      # Loads the Hugging Face model and tokenizer
├── chat\_memory.py       # Sliding window memory logic
├── interface.py         # Main CLI interface
├── README.md            # This file
└── .gitignore           # Git ignore rules (optional)

````

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/chatbot-project.git
cd chatbot-project
````

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate      # On Linux/Mac
venv\Scripts\activate         # On Windows
```

### 3. Install Required Packages

```bash
pip install transformers
```

---

## ▶️ Running the Chatbot

Simply run the CLI using:

```bash
python interface.py
```

You'll see:

```
🤖 Chatbot is ready! Type your message below.
Type '/exit' to end the chat.
```

---

## 💡 Example Interaction

```
You: What is the capital of France?
Bot: The capital of France is Paris.

You: And what about Italy?
Bot: The capital of Italy is Rome.

You: /exit
Bot: Exiting chatbot. Goodbye! 👋
```

---

## 🎥 Demo Video

📽️ [Watch the 2-minute demo](https://your-demo-link-here.com)
Includes a walkthrough of:

* Project files & structure
* Running the bot
* Explanation of design decisions

---

## 📚 Model Used

* [`distilgpt2`](https://huggingface.co/distilgpt2) – a smaller, faster version of GPT-2, ideal for local inference

---

## 🧠 Tech Stack

* Python 3.8+
* Hugging Face Transformers

---

## 📄 License

This project is open-source and free to use under the MIT License.

---

## 🙋‍♂️ Author

Made with ❤️ by [Nipun Goel](https://github.com/nipungoel24)

✅ Let me know if you'd like:
- A **demo video script**
- To test or extend the chatbot
- Help uploading to GitHub with all assets

Want to include a badge section too?
