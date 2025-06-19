# interface.py
from model_loader import load_chatbot_model
from chat_memory import ChatMemory

def main():
    print("🧠 Loading chatbot, please wait...\n")
    chatbot, tokenizer = load_chatbot_model()
    memory = ChatMemory(max_turns=3)

    print("🤖 Chatbot is ready! Type your message below.")
    print("Type '/exit' to end the chat.\n")

    while True:
        user_input = input("You: ")

        if user_input.strip().lower() == "/exit":
            print("Bot: Exiting chatbot. Goodbye! 👋")
            break

        # Combine past context + current input
        context = memory.get_context()
        prompt = context + f"\nUser: {user_input}\nBot:"

        # Generate response
        response = chatbot(prompt, do_sample=True, temperature=0.7)[0]["generated_text"]
        
        # Extract bot's latest response only
        bot_reply = response[len(prompt):].strip().split("\n")[0]

        print(f"Bot: {bot_reply}")
        memory.add_exchange(user_input, bot_reply)

if __name__ == "__main__":
    main()
