from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


class MovieQA:

    def __init__(self, llm, retriever):

        self.llm = llm
        self.retriever = retriever

    def construct_prompt(self):
        template = """Answer the question based only on the following context:
        {context}

        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)
        return prompt

    def answer_query(self, query):
        setup_and_retrieval = RunnableParallel(
            {"context": self.retriever, "question": RunnablePassthrough()}
        )
        chain = setup_and_retrieval | self.construct_prompt() | self.llm | StrOutputParser()

        answer =  chain.invoke(query)
        return  answer