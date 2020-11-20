from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
input_url = "https://punchng.com"
URL = input_url
headers = {"user-agent" : 'Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'}
page = requests.get(URL,headers=headers)
soup = BeautifulSoup(page.content,'html.parser')

app = FastAPI()
@app.get("/api/v1/news")

async def root():
    b = None
    title = soup.find_all("h3")
    l = (soup.find_all('section'))[3]
    link = l.find_all ('a')
    u = [s.get('href') for s in link]
    b = [a.get_text() for a in title]
    return {"news":b, "url":u}