# main.py
from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/api")
def read_api_root():
    with open('q-vercel-python.json', 'r') as f:
        marks = json.load(f)
    names = request.args.getlist('name')
    results = []

    for name in names:
        if name in marks:
            results.append(marks[name]['marks'])  # Access the 'marks' value
        else:
            results.append(None)  # Or handle missing names differently

    return jsonify(results)
