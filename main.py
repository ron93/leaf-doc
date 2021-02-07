from fastapi import FastAPI
import pickle

app = FastAPI()

#pickle model
model_file = open("model.pkl","rb")
model = pickle.load(model_file)

@app.post("/analyze")
def analyze():
    return {"prediction": "Disease ditector!"}

@app.get("/info")
def get_disease():
    return {"Info": "Disease information"}