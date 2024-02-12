from flask import Flask, request
from openai import OpenAI
import os
import json

from dotenv import load_dotenv
load_dotenv()
if not os.environ.get("OPEN_API_KEY"):
  raise ValueError("API Key not found.")  

app = Flask(__name__)

client = OpenAI()

# assistant = client.beta.assistants.create(
#     name="SmartAssistant",
#     instructions="You are named SmartAssistant, made by Group 17 for their Senior Project. You will act as a smart customer service that can be personalized by each company for their needs by feeding you information through files or texts. Refrain from answering questions that may be beyond your role as a customer service.",
#     tools=[],
#     model="gpt-3.5-turbo"
# )

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