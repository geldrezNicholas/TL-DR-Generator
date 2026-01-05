import torch
from transformers import BartForConditionalGeneration, BartTokenizer

class Summarizer:
    def __init__(self):
        self.model_name = "facebook/bart-large-cnn"
        print(f"Loading {self.model_name}...")

        #maps every word to a unique token(numbers)
        self.tokenizer = BartTokenizer.from_pretrained(self.model_name)

        #pytorch neural network
        self.model = BartForConditionalGeneration.from_pretrained(self.model_name)

    def summarize(self, text, max_length=150, min_length=40):
        #Pre-processing
        inputs = self.tokenizer(
            text, #Pasted Text
            max_length=1024, 
            return_tensors="pt", #PyTorch Tensor
            truncation=True #Cut off if text is too long
        )
        
        #Inference
        summary_ids = self.model.generate(
            inputs['input_ids'], #Tensor containing unique word tokens
            max_length=max_length, 
            min_length=min_length, 
            length_penalty=2.0, 
            num_beams=4, #Explores 4 "future sentences" and keep the best one
            early_stopping=True
        )
        
        #Post-processing
        #Turn tokens to english and return
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary