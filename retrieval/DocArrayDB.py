from RAG.retrieval.knowledgeDB import KnowledgeDB
from langchain_community.vectorstores import DocArrayInMemorySearch
from langchain_openai import OpenAIEmbeddings



class DocArrayDB(KnowledgeDB):

    def __init__(self):
        vectorstore = DocArrayInMemorySearch.from_texts([],embedding=OpenAIEmbeddings())
        super(DocArrayDB, self).__init__(vectorstore)

        self.add_documents(['Pranoy Sarath is studing in Rutgers', 'Previously hw worked at ServiceNow'])
        return None

    def get_retriever(self):
        return self.db.as_retriever()

    # assume for now they are texts
    def add_documents(self, texts):
        self.db.add_texts(texts)

    # get docs and select and send it back
    def get_documents(self, search_text):
        docs = self.db.similarity_search(search_text)
        return docs

# db = DocArrayDB()
# db.add_documents(['Prnaoy Sarath'])
# print(db.get_documents('sarath'))





