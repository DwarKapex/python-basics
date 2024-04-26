from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.get("/ping/")
def ping():
    return {"message": "pong"}


@app.get("/greet/")
def make_greeting(name: str = "Guest"):
    return {"message": f"Hello {name}!"}

