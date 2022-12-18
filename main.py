from fastapi import FastAPI, HTTPException
import math
from PIL import Image
import PIL.ImageOps
import requests
import io
from base64 import b64encode
from datetime import datetime

app = FastAPI()

@app.get("/prime/{number}")
async def isprime(number: int):
    try:
        val = int(number)
    except ValueError:
        return "Wpisz liczbę®"
    x = 2
    while x <= math.sqrt(number):
        if number % x < 1:
            return {"Czy jest pierwsza liczba? Nie"}
        x = x + 1
    return {"Czy jest pierwsza liczba? Tak"}

@app.get("/picture/invert")
async def invert(link):
    response = requests.get(link)
    image_bytes = io.BytesIO(response.content)
    img = PIL.Image.open(image_bytes).convert('RGB')
    img2 = PIL.ImageOps.invert(img)
    return Response(content="<img src="+link+"></img>")
@app.get("/time")
def basic_auth(username, password):
    token_valid = 'YWRtaW46YWRtaW4xMjM='  # admin admin123
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    if (token_valid == token):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print()
        return "<h2>Current Time =" + current_time +"</h2>"
    else:
        return "<h2>Nie udane logowanie</h2>"
