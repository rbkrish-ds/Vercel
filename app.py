# app.py (main application file)
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (replace with your actual data source)
marks = {
    "X": 95,
    "Y": 88,
    "Z": 72,
    "A": 90,
    "B": 85,
}

@app.route('/api')
def api():
    names = request.args.getlist('name')  # Get all 'name' parameters
    results = []

    for name in names:
        if name in marks:
            results.append(marks[name])
        else:
            results.append(None)  # Or handle missing names differently (e.g., return an error)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000) # Only for local development. Vercel will handle the port.