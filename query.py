from RAG.llm_model.LLM import LLMModel
from RAG.langchain_chaining.prompt_chaining import ShowQA
from RAG.retrieval_client.remote_retriever import RemoteRetriever


llm = LLMModel('gpt-3.5-turbo-0301').get_model()
qa = ShowQA(llm, RemoteRetriever())

print(qa.answer_query('What is the rating of episode 8 of Dark Matter. give me a summary also'))





