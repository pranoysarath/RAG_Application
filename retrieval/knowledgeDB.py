from abc import ABC, abstractmethod
import os

from RAG.configuration.ConfigParser import ConfigParser

os.environ["OPENAI_API_KEY"] = ConfigParser.get_key_value('open_ai')

class KnowledgeDB(ABC):

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


