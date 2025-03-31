from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = \"FinGPT/fingpt-fraud-detection\"  # Example model name; update as needed
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def detect_fraud_risk(text: str) -> int:
    inputs = tokenizer(text, return_tensors=\"pt\", truncation=True)
    outputs = model(**inputs)
    risk_level = int(torch.argmax(outputs.logits).item())
    return risk_level
