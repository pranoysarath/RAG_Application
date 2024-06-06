from RAG.retrieval.DocArrayDB import DocArrayDB


class DBFactory:

    DB_MAPPINGS = {

        'in_memory_docarray': DocArrayDB
    }
    @staticmethod
    def create_and_get_db(type):
        return DBFactory.DB_MAPPINGS[type]()