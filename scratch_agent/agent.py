import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
messages=[]
while True:
    user_input=input("user:")
    if user_input.strip().lower()=="exit" or user_input.strip().lower()=="quit":
        break
    messages.append({"role":"user","content":user_input})
    response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=messages
    )
    reply= response.choices[0].message.content
    messages.append({"role":"assistant","content":reply})
    print("Agent",reply)