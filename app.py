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

if __name__ == '__main__':
  app.run(debug=True)

client = OpenAI()

@app.route("/")
def hello_world():
  return "<div style='min-height: 100vh; display: flex; justify-content: center; align-items: center; font-size: 20'>SmartAssistant Backend</div>"

@app.route("/chat", methods=["POST"])
def chat(): 
  prompt = request.json.get("prompt")
  if prompt is None:
    return json.dumps({'error': 'No prompt provided'}), 400
  
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": prompt}
    ]
  )
  print(completion.choices[0].message.content)
  return completion.choices[0].message.content

@app.route("/chat/assistant", methods=["POST"])
def chatAssistant():
  prompt = request.json.get("prompt")
  if prompt is None:
    return json.dumps({'error': 'No prompt provided'}), 400
  
  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": os.environ.get("ASSISTANT_INSTRUCTIONS")},
    {"role": "user", "content": prompt}
  ]
  )
  print(completion.choices[0].message.content)
  return completion.choices[0].message.content
  
  
  