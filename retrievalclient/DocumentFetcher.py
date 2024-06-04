import requests

def get_documents(query, k):
    url = "http://127.0.0.1:5000/query"
    params = {"query": query, "k": k}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.text)
        return None

# # Example usage:
# query = "example"
# k = 5
# result = get_documents(query, k)
# if result:
#    print(result)