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

from fastapi import FastAPI, Request, HTTPException

# creating instance/application
app = FastAPI(title="Ticket Classifier")

# defining operations for root endpoint
@app.get('/')
def welcome():
    return {'message': 'Welcome to my First API'}

# endpoint to check api health
@app.get("/health")
def health():
    return {"status": "ok"}

# classification endpoint
@app.post("/ticket-classify")
async def ticket_classifier(request: Request):
    body = await request.json()
    ticket_text = str(body.get("ticket_text", "")).strip()

    if not ticket_text:
        raise HTTPException(
            status_code = 400,
            detail = "ticket_text is required"
        )

    lower_text = ticket_text.lower()

    if "replacement" in lower_text:
        category = "Replacement Ticket"
    elif "return" in lower_text:
        category = "Return Ticket"
    else:
        category = "General Support"

    return {
        "category": category,
        "summary": ticket_text[:50]
    }


'''
How to run in local:
1. Install requirment - pip install fastapi uvicorn
2. Run uvicorn in terminal - uvicorn main:app --reload --port 8000  (here main is file name having app)
3. Your application will be running at http://127.0.0.1:8000
You can check in browser or via postman
'''