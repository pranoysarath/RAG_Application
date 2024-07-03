from flask import Flask, jsonify, request, Blueprint

from RAG.retrieval.DBFactory import DBFactory

api_bp = Blueprint('api', __name__)
app = Flask(__name__)


vector_db  = DBFactory.create_and_get_db('in_memory_docarray')
def query_documents(query):
    documents =  vector_db.get_documents(query)
    return [doc.page_content for doc in documents]


@api_bp.route("/")
def hello():
    return jsonify({"message": "Hello, World!"})

@api_bp.route("/query", methods=["GET"])
def get_documents():
    try:
        query = request.args.get("query")
        return jsonify(query_documents(query))
    except Exception as e:
        print(f"Error occurred during retrieving documents {e}")

@api_bp.route("/add_documents", methods=["POST"])
def add_documents():

    try:
        documents = request.get_json()
        print(documents)
        vector_db.add_documents(documents)
        print("Successfully added documents")
        response = {
            "status": "success",
            "message": "Documents added successfully",

        }
        return jsonify(response), 200

    except Exception as e:
        print(f"Error occurred during adding documents {e}")
        response = {
            "status": "error",
            "message": str(e)
        }
        return jsonify(response), 500



app.register_blueprint(api_bp, url_prefix = '/retriever')
if __name__ == "__main__":
    app.run()