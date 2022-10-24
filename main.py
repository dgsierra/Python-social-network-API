from fastapi import FastAPI # Import FastAPI
from fastapi.params import Body # <-- Import Body
from pydantic import BaseModel # <-- Import BaseModel

app = FastAPI()
x = ''

@app.get("/")
async def root():
    return {"message": "Welcome to my API2"}


@app.get("/posts/")
def get_posts():
    return {"data": "This is a post"}

@app.post("/create/")
def create_post(payLoad: dict = Body(...)):
    print(payLoad)
    x = payLoad['extra']
    return {"new_post": f"Title: {payLoad['title']}, Content: {payLoad['content']} and Extra: {x}"}
