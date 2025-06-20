# interface.py

from transformers import pipeline
from model_loader import load_chatbot_model
from chat_memory import ChatMemory

def build_prompt(context, user_input):
    system_prompt = "[INST] You are a helpful, honest, and concise assistant. [/INST]"
    user_prompt = f"[INST] {user_input} [/INST]"
    return f"{system_prompt}\n{context}\n{user_prompt}".strip()

def main():
    print("[*] Loading Mistral chatbot, please wait...\n")
    model, tokenizer = load_chatbot_model()
    chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

    memory = ChatMemory(max_turns=5)
    print("[*] Chatbot is ready! Type your questions below.")
    print("Type '/exit' to end the chat.\n")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "/exit":
            print("Bot: Exiting chatbot. Goodbye! 👋")
            break

        context = memory.get_context()
        prompt = build_prompt(context, user_input)

        output = chatbot(
            prompt,
            max_new_tokens=256,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.9,
            return_full_text=False
        )[0]["generated_text"].strip()

        print(f"Bot: {output}")
        memory.add_turn(user_input, output)

if __name__ == "__main__":
    main()
