from fastapi import FastAPI

from app.model import model

app = FastAPI()


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(payload: dict):

    prompt = payload["prompt"]

    result = model.predict(prompt)

    return result