import json
from pathlib import Path
from typing import Callable, Dict, List, Optional, Union
import os
from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader
from langchain_community.document_loaders import BSHTMLLoader
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma

class JSONLoader(BaseLoader):
    def __init__(
        self,
        file_path: Union[str, Path],
        content_key: Optional[str] = None,
        ):
        self.file_path = Path(file_path).resolve()
        self._content_key = content_key
        
    def load(self) -> List[Document]:
        """Load and return documents from the JSON file."""

        docs=[]
        # Load JSON file
        with open(self.file_path,encoding="utf8") as file:
            data = json.load(file)

            # Iterate through 'pages'
            for page in data:
                pagetitle = page['SchemeName']
                snippets = page['Information']

                
                metadata = dict(
                    title=pagetitle)

                docs.append(Document(page_content=snippets, metadata=metadata))
        return docs

def create_collection_local(client, collection_name, embedding_function):
    collection = client.create_collection(
        name=collection_name, embedding_function=embedding_function
    )
    return collection


def add_documents_local(collection, document, id):
    collection.add_documents(documents=document, ids=id)
    collection.persist()


def query_documents_local(collection, question):
    results = collection.similarity_search_with_score(query=question, k=1)
    return results


embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
# BAAI/bge-large-en-v1.5

file_path='data.json'
loader = JSONLoader(file_path=file_path)
documents = loader.load()


persist_directory = "./db"
if not os.path.exists(persist_directory):
    os.makedirs(persist_directory)

collection = Chroma(
    collection_name="farmer-schemes-govi",
    embedding_function=embedding_function,
    persist_directory=persist_directory,
)


# def split_documents(documents, chunk_size=20):
#     return [documents[i : i + chunk_size] for i in range(0, len(documents), chunk_size)]


# split_docs = split_documents(documents)
# print("total split doc length - ",len(split_docs))
def generate_number_ids(length):
    return [str(i) for i in range(1, length + 1)]

length = 27
number_ids = generate_number_ids(length)
add_documents_local(collection, documents, number_ids)


query = "what is fasal bima yojna"
print(query_documents_local(collection, query))
