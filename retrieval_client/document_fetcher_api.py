import requests

class DocumentFetcher:

    # configure it
    RETRIEVER_BASE_URL = "http://127.0.0.1:5000/"
    RETRIEVER_GET_DOCUMENT_URL = f"{RETRIEVER_BASE_URL}/retriever/query"
    @staticmethod
    def get_documents(query, top_k):
        try:
            params = {"query": query, "k": top_k}
            response = requests.get(DocumentFetcher.RETRIEVER_GET_DOCUMENT_URL, params=params)
            print(response.json())
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print("Error:", response.text)
                return None
        except Exception as e:
            print(f"Error occured while getting similar documents {e}")

    # # Example usage:
    # query = "example"
    # k = 5
    # result = get_documents(query, k)
    # if result:
    #    print(result)