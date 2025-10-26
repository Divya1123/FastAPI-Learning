from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pickle

# load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

class_names = ["setosa", "versicolor", "virginica"]

# define request and response body structure using Pydantic BaseModel
class request_body(BaseModel):
    sepal_length : float
    sepal_width : float
    petal_length : float
    petal_width : float

# Output schema
class IrisOutput(BaseModel):
    class_name: str
    class_index: int

app = FastAPI()

@app.get('/')
def main():
    return {'message': 'Welcome to my First API'}

@app.post('/predict', response_model= IrisOutput)
def predict(data: request_body):
    test_data = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    class_idx = model.predict(test_data)[0]
    return {"class_name": class_names[class_idx], "class_index": class_idx} # this is the response body - must follow response structure
