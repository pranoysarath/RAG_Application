from typing import List

from langchain_core.callbacks import CallbackManagerForRetrieverRun
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever

from RAG.retrieval_client.document_fetcher_api import DocumentFetcher


class RemoteRetriever(BaseRetriever):


    # make it async
    def _get_relevant_documents(
            self, query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        """Sync implementations for retriever."""
        docs = DocumentFetcher.get_documents(query,5)
        from langchain.docstore.document import Document
        documents = [Document(page_content=docs[i], metadata={"source": "local"}) for i in range(len(docs))]
        return [documents]