from langchain_core.embeddings import Embeddings
import google.generativeai as genai
import numpy as np
from typing import List

class GeminiEmbeddings(Embeddings):
    def __init__(self, model_name="models/text-embedding-004", task_type="semantic_similarity", api_key=None):
        self.model_name = model_name
        self.task_type = task_type
        genai.configure(api_key=api_key)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [
            genai.embed_content(model=self.model_name, content=text, task_type=self.task_type)["embedding"]
            for text in texts
        ]

    def embed_query(self, text: str) -> List[float]:
        return genai.embed_content(model=self.model_name, content=text, task_type=self.task_type)["embedding"]
