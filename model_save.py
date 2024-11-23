from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "sachinoholic/my_T5_finetuned_model"

# Download the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# Save locally
model.save_pretrained("model")
tokenizer.save_pretrained("model")
