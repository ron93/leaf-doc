from fastapi import FastAPI


app = FastAPI()


@app.post("/analyze")
def analyze():
    return {"prediction": "Disease ditector!"}

@app.get("/info")
def get_disease():
    return {"Info": "Disease information"}