'''
Building a small endpoint
When hit, it shows hello world in the output. 

'''

from fastapi import FastAPI

# app object 
app = FastAPI()

# define endpoint
# define route for endpoint 
# get signifies that this endpoint will respond to GET requests
# to fetch data from server you do get request, if you want to send data to server you do POST request

@app.get("/") # if anyone hits this endpoint, it will return the message (route with decorator)
# create endpoint function 
def hello():
    return {"message": "Hello, World!"}

# execute  : uvicorn main:app --reload and click on the URL to see the output

'''
Make one more endpoint called about.
Create one more get request and route will be /about

'''

@app.get("/about")  # create one more get request and route will be /about
def about():
    return {"message": "Every business has an origin story worth telling, and usually one that justifies why you do business and have clients.\
        Some centennial enterprises have pages of content that can fit in this section, while startups can tell the story of how the company was born, its challenges, and its vision for the future."}

# execute  : uvicorn main:app --reload and click on the URL to see the output
