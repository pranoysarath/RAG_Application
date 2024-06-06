from flask import Flask, jsonify, request

from RAG.retrieval.DBFactory import DBFactory


app = Flask(__name__)

vector_db  = DBFactory.create_and_get_db('in_memory_docarray')
def query_documents(query):
    documents =  vector_db.get_documents(query)
    return [doc.page_content for doc in documents]


@app.route("/")
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route("/query", methods=["GET"])
def get_documents():
    query = request.args.get("query")
    return jsonify(query_documents(query))

@app.route("/add_documents", methods=["POST"])
def add_documents():
    documents = request.get_json()
    vector_db.add_documents(documents)
    return "Successfully added"

if __name__ == "__main__":
    app.run(debug=True)