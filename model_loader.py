# model_loader.py
from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer

def load_chatbot_model(model_name="microsoft/DialoGPT-small"):
    print("Loading model...")

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Set pad token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    chatbot = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=100,
        pad_token_id=tokenizer.pad_token_id
    )

    return chatbot, tokenizer
