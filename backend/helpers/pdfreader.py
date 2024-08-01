# from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader("AR_English_2023_24.pdf")
# pages = loader.load_and_split()
# print(type(pages[0]))

# from langchain_community.document_loaders import BSHTMLLoader
# loader = BSHTMLLoader("Press ReleaseI_Press information Bureau.html", open_encoding="utf8")
# data = loader.load()
# print(data)

import json
from pathlib import Path
from typing import Callable, Dict, List, Optional, Union

from langchain.docstore.document import Document
from langchain.document_loaders.base import BaseLoader


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

file_path='data.json'
loader = JSONLoader(file_path=file_path)
data = loader.load()
print(data[0])