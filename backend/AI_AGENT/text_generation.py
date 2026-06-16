from transformers import AutoModelForCausalLM, AutoTokenizer

try:
    model_name = "Qwen/Qwen3.6-27B" 
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
    print("Model loaded successfully")
except Exception as e:
    print(e)
    
