from RAG.retrieval.KnowledgeDBRetreiever import KnowledgeDBRetriever
from RAG.model.LLM import LLMModel
from RAG.QA import MovieQA
from RAG.retrievalclient.remoteretriever import RemoteRetriever

# retriever = KnowledgeDBRetriever('in_memory_docarray').get_retriever()

llm = LLMModel('gpt-3.5-turbo-0301').get_model()

qa = MovieQA(llm, RemoteRetriever())

print(qa.answer_query('who is pranoy sarath. where does he work'))




