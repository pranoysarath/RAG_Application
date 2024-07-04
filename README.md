# Dynamically Updated TV show Information retriever
Utilized LangChain to build a RAG framework, incorporating GPT, and a knowledge database with daily
scheduled updates to provide up-to-date TV show information

## Architecture

![TV Show RAG architecture](https://github.com/pranoysarath/RAG_Application/assets/21723195/ce9d0303-b144-4abd-9e34-1a6bef937bb8)

## Components

Three individual systems are present

1. Remote Knowledge based Server - Remotely hosted knowledge database that could be scaled separately. 
    1. Have endpoints exposed to add and retrieve documents
2. ETL pipeline orchestrated using apache airflow It composes of 3 individual tasks
    1. Fetch Tv-show information from TVMaze based on the 'To-be-processed' list
    2. Process the data and format it into documents. Send documents to remote Server
    3. Perform cleanup post processing
3.  LLM which combines user based query  and retrieved documents from knowledge database and provides formatted output
