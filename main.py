from fastapi import FastAPI, Request, Query, HTTPException  # Import Request
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
import json
from typing import List, Dict, Optional

app = FastAPI()
# Add CORS middleware
origins = ["*"]  # Allow all origins (for development).  **IMPORTANT:** Restrict in production!

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/api")
async def read_api_root(request: Request, name: List[str] = Query(..., description="List of names")): # Use Request object
    print("api")
    try:
        with open('q-vercel-python.json', 'r') as f:
            marks: Dict[str, Dict[str, int]] = json.load(f)  # Type hint for marks
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="q-vercel-python.json not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON in q-vercel-python.json")


    

    results: List[Optional[int]] = []
    print(name)
    print(marks)
    for name_val in name:
        print(name_val)
        for mark in marks:
            if mark["name"]==name_val:
                results.append(mark["marks"])
       

    return { "marks": results } # Return directly, FastAPI handles JSON conversion
