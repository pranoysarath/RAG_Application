from abc import ABC, abstractmethod
import os
os.environ["OPENAI_API_KEY"] = ""

class KnowledgeDB:

    def __init__(self, db):
        self.db = db

    @abstractmethod
    def get_retriever(self):
        pass

    @abstractmethod
    def add_documents(self):
        pass


    @abstractmethod
    def get_documents(self):
        pass


