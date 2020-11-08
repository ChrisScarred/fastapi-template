from fastapi import FastAPI
import requests
import sys
from addresses import *

app = FastAPI()


@app.get("/")
async def main():
    return {"message": "Hello World; API"}

@app.get("/web")
async def web():
    return requests.get(WEB_ADDRESS).json()