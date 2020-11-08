from fastapi import FastAPI
import requests
import sys
from addresses import *

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Hello World; WEB"}

@app.get("/api")
async def api():
    return requests.get(API_ADDRESS).json()