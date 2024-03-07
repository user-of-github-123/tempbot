import os
from fastapi import FastAPI, Request
import requests
from dotenv import load_dotenv

load_dotenv()  # variables from .env
API_KEY = "6422329452:AFF_2jiXEE2Nqs9rAu7y2hZnM5CUh_B3bAk"

app = FastAPI()

@app.post("/webhook")
async def webhook(req: Request):
    print("something is detected")
    body = await req.json()
    if 'message' not in body:
        return print('No message found', body)
    bm = body['message']
    if 'text' not in bm:
        return print('No text found', body)
    print("valid text wow")
    chat_id = bm['chat']['id']
    text = bm['text']
    # Send echo message
    url = f"https://api.telegram.org/bot{6422329452:AFF_2jiXEE2Nqs9rAu7y2hZnM5CUh_B3bAk}/sendMessage"
    payload = {"chat_id": chat_id,
        "text": text}
    response = requests.post(url, json=payload)
    print("sent back")
    return response.json()