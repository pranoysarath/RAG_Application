import os
from langchain_openai import ChatOpenAI
from RAG.configuration.ConfigParser import ConfigParser

os.environ["OPENAI_API_KEY"] = ConfigParser.get_key_value('open_ai')

class LLMModel:

    def __init__(self, name):
        self.model = ChatOpenAI(model=name)

    def get_model(self):
        return self.model


