import os
from langchain_openai import ChatOpenAI


os.environ["OPENAI_API_KEY"] = ""

class LLMModel:

    def __init__(self, name):
        self.model = ChatOpenAI(model=name)

    def get_model(self):
        return self.model


