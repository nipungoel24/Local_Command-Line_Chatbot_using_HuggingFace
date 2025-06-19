# model_loader.py
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

def load_chatbot_model(model_name="distilgpt2"):
    print("Loading model...")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    chatbot = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=100,
        pad_token_id=tokenizer.eos_token_id
    )

    return chatbot, tokenizer
