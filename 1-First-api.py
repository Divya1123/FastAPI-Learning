from fastapi import FastAPI
import uvicorn

# creating instance
app = FastAPI()

# defining operations for root endpoint
@app.get('/')
def main():
    return {'message': 'Welcome to my First API'}

# define operation for /name endpoint
@app.get('/{name}')
def hello_name(name):
    return {'message': f'Welcome {name}, to my First API'}