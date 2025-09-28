from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Handles requests to the root URL and returns a JSON message.
    """
    return jsonify({"message": "Hello, World!"})

if __name__ == '__main__':
    app.run(host='0,0,0,0',debug=True)
    