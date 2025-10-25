import requests
from a import api
def classify_text(text):
  API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
  headers = {'Authorization': 'Bearer hf_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
  playload = {"inputs": text}
  response = requests.post(API_URL, headers=headers, json=playload)
  return response.json()
if __name__ == "__main__":
   text = "I love programming."
   result = classify_text(text)
   print(result)