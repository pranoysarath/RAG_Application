from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route("/query", methods=["GET"])
def get_items():
    query = request.args.get("query")
    k = request.args.get("k", type=int)

    return jsonify(['My name is Pranoy Sarath','Pranoy worked at ServiceNow'])

if __name__ == "__main__":
    app.run(debug=True)