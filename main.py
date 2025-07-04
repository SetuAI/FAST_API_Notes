'''
Building a small endpoint
When hit, it shows "hello world" in the output. 
And then another endpoint that shows "about" the business.
And then building couple of other endpoints as well.

'''
import json
from fastapi import FastAPI,Path,HTTPException

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

# you can go to the URL : http://127.0.0.1:8000/about and you can see the output of the about endpoint
# you can go to the URL : http://127.0.0.1:8000 and you can see the output of the hello endpoint

# if you go to http://127.0.0.1:8000/docs you can see the documentation of the API that is generated by FastAPI


def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data

# create an endpoint called "View"
# as soon as someone hits the endpoint, it will return all the records of the patients (records from the patients.json file)

@app.get("/view")
def view():
    data = load_data() # fetch data using load_Data function
    return data

@app.get("/patient/{patient_id}")  # adding dynamic segment called {patient_id}
def view_patient(patient_id: str=Path(..., description='ID of the patient in DB',
                                      example = 'P001')): # if you look at patient id , it is a string "P001" , hence we take str
    # load all the patients data
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

# Once executed this code, check : http://127.0.0.1:8000/patient/P001
# checking the data here for 1st patient.
# you can also go to /docs and see the documentation 