from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to my API2"}


@app.get("/posts/")
def get_posts():
    return {"data": "This is a post"}

@app.post("/create/")
def create_post(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"Title: {payLoad['title']}, Content: {payLoad['content']}"}
