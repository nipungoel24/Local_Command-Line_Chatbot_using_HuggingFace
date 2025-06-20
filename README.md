Absolutely, Nipun! Here's your **final `README.md`** for the internship chatbot project using **Mistral-7B-Instruct**, formatted professionally and clearly for reviewers or GitHub submission.

---

# 🤖 CLI Chatbot using Mistral-7B-Instruct (Hugging Face Transformers)

This project is a command-line chatbot that uses the [mistralai/Mistral-7B-Instruct-v0.1](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1) model from Hugging Face. The chatbot supports **multi-turn dialogue**, maintains short-term memory, and runs efficiently using **4-bit quantization** with `bitsandbytes`.

---

## 📌 Features

- 🧠 **Instruction-tuned model** (Mistral-7B-Instruct)
- 🔄 **Multi-turn memory** (last 5 Q&A pairs)
- 💻 **Command-line interface (CLI)**
- ⚡️ **Quantized for fast GPU inference (4-bit)**
- ✅ **Modular Python structure**: clean, extendable code
- 🔗 **Fully Hugging Face-integrated**

---

## 🛠️ Project Structure

```

chatbot-mistral/
├── model\_loader.py      # Loads the quantized Hugging Face model
├── chat\_memory.py       # Handles turn-based memory (deque)
├── interface.py         # Command-line interface for chatting
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

````

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/chatbot-mistral.git
cd chatbot-mistral
````

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # For Mac/Linux
venv\Scripts\activate         # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> ✅ Dependencies: `transformers`, `accelerate`, `bitsandbytes`, `sentencepiece`

---

## 🔐 Hugging Face Token Setup (Important)

Since Mistral is a **gated model**, you must:

1. Create an account on [https://huggingface.co](https://huggingface.co)
2. Accept the terms for [mistralai/Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)
3. Get your token from [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
4. Log in in Colab or terminal:

```python
from huggingface_hub import login
login()  # Paste your token when prompted
```

---

## ▶️ Run the Chatbot

```bash
python interface.py
```

Then chat naturally:

```
You: What is the capital of India?
Bot: The capital of India is New Delhi.

You: And of France?
Bot: The capital of France is Paris.
```

Exit anytime with:

```
You: /exit
```

---

## 💬 Prompt Style (Mistral Format)

The chatbot uses the \[INST]...\[/INST] token format to simulate conversation:

```text
[INST] What is the capital of France? [/INST] Paris
```

Context builds from recent turns using `deque`.

---

## 🎥 Demo Walkthrough

You can record a short video showing:

* Model loading
* Chat interaction (3–5 Q\&A)
* Real-time CLI behavior
* Brief explanation of code + structure

---

## 📄 License

Open-source and free to use under the **MIT License**.

---

## 👨‍💻 Author

Made by [Nipun Goel](https://github.com/nipungoel24)
Internship project powered by Hugging Face + Mistral
