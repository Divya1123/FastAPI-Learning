'''
Business Requirement: Customer want to have a functionality that classifies the user ticket before reaching their helpdesk.
We will build a simple API for this functionality. Below would be the expected payload and response of our API.

Request Payload:
{
    "ticket_text": "I have received a damaged order. I need replacement."
}

Response Body expected:
{
    "category": "Replacement Ticket",
    "Summary": "Customer received a damaged product, they are requested replacement."
}
'''

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
