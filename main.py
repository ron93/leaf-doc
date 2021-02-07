from fastapi import FastAPI


app = FastAPI()


@app.get("/analyze")
def analyze():
    return {"prediction": "Disease ditector!"}