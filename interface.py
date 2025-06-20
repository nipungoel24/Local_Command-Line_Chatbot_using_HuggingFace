# interface.py
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def main():
    print("[*] Loading DialoGPT model...\n")
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-small")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-small")

    # Chat loop
    chat_history_ids = None
    step = 0
    print("[*] Chatbot is ready! Type your message below.")
    print("Type '/exit' to end the chat.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "/exit":
            print("Bot: Exiting chatbot. Goodbye! 👋")
            break

        # Encode user input
        new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

        # Append to chat history
        bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1) if step > 0 else new_input_ids

        # Generate response
        chat_history_ids = model.generate(
            bot_input_ids,
            max_new_tokens=100,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.75
        )

        # Decode response
        bot_output = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        print(f"Bot: {bot_output}")
        step += 1

if __name__ == "__main__":
    main()
