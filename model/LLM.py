import os
from langchain_openai import ChatOpenAI


os.environ["OPENAI_API_KEY"] = "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"

class LLMModel:

    def __init__(self, name):
        self.model = ChatOpenAI(model=name)

    def get_model(self):
        return self.model


