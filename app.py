from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (replace with your actual data source)
# Load the JSON data from a file (recommended for larger datasets)
import json
with open('q-vercel-python.json', 'r') as f:
    marks = json.load(f)

# Or, if the data is small, you can define it directly:
# marks = {  # ... your JSON data here ... }

@app.route('/api')
def api():
    names = request.args.getlist('name')
    results = []

    for name in names:
        if name in marks:
            results.append(marks[name]['marks'])  # Access the 'marks' value
        else:
            results.append(None)  # Or handle missing names differently

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
