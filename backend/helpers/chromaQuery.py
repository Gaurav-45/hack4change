import os
import json
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma

def query_documents_local(collection, question):
    results = collection.similarity_search_with_score(query=question, k=1)
    return results


def chroma_init():
    embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    persist_directory = "./db"
    if not os.path.exists(persist_directory):
        os.makedirs(persist_directory)

    collection = Chroma(
        collection_name="farmer-schemes-govi",
        embedding_function=embedding_function,
        persist_directory=persist_directory,
    )

    return collection


query = "what is fasal bima yojna"
collection = chroma_init()
resp = query_documents_local(collection, query)
final_resp = f"title - {resp[0][0].metadata['title']}, content - {resp[0][0].page_content}"
print(final_resp)