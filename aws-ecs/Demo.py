from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}
    

@app.get("/nm/{name}")
def read_item(name: str):
    return "Hello {name}!".format(name=name)


#uvicorn Demo:app --host "0.0.0.0" --port 80


