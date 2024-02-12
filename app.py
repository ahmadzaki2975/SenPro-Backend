from flask import Flask, request
from openai import OpenAI
import os
import json

from dotenv import load_dotenv
load_dotenv()
print(os.environ.get("OPENAI_API_KEY"))
if not os.environ.get("OPENAI_API_KEY"):
  raise ValueError("API Key not found.")  

app = Flask(__name__)

client = OpenAI()

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

@app.route("/chat", methods=['POST'])
def chat(): 
  prompt = request.json.get('prompt')
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": prompt}
    ]
  )
  print(completion.choices[0].message.content)
  return completion.choices[0].message.content