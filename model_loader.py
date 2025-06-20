# model_loader.py

from transformers import AutoTokenizer, AutoModelForCausalLM

def load_chatbot_model(model_id="mistralai/Mistral-7B-Instruct-v0.1"):
    print(f"[*] Loading model: {model_id}")

    tokenizer = AutoTokenizer.from_pretrained(model_id)

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        device_map="auto",
        torch_dtype="auto",
        load_in_4bit=True
    )

    return model, tokenizer
