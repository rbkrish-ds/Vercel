from fastapi import FastAPI, Request, Query, HTTPException, jsonify  # Import Request
import json
from typing import List, Dict, Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/api")
async def read_api_root(request: Request, names: List[str] = Query(..., description="List of names")): # Use Request object
    print("api")
    try:
        with open('q-vercel-python.json', 'r') as f:
            marks: Dict[str, Dict[str, int]] = json.load(f)  # Type hint for marks
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="q-vercel-python.json not found")
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Invalid JSON in q-vercel-python.json")


    print(names)
    print(marks) # No need to json.dumps, FastAPI handles it

    results: List[Optional[int]] = []

    for name in names:
        mark_data = marks.get(name)
        if mark_data:
            results.append(mark_data.get('marks'))  # safer way to access the marks

        else:
            results.append(None)

    return results # Return directly, FastAPI handles JSON conversion
