

from RAG.retrieval.DocArrayDB import DocArrayDB


class KnowledgeDBRetriever:

    DB_MAPPINGS = {

        'in_memory_docarray' : DocArrayDB
    }
    #
    def __init__(self, db_type):
        self.retriever = self.DB_MAPPINGS[db_type]().get_retriever()

    def get_retriever(self):
        return self.retriever

