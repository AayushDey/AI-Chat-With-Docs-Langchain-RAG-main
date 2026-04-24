from langchain_huggingface import HuggingFaceEmbeddings
from langchain.evaluation import load_evaluator
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def main():
    # Get embedding for a word using HuggingFace (no API key needed).
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector = embedding_function.embed_query("apple")
    print(f"Vector for 'apple': {vector}")
    print(f"Vector length: {len(vector)}")

    # Compare vector of two words
    evaluator = load_evaluator("pairwise_embedding_distance", embeddings=embedding_function)
    words = ("apple", "iphone")
    x = evaluator.evaluate_string_pairs(prediction=words[0], prediction_b=words[1])
    print(f"Comparing ({words[0]}, {words[1]}): {x}")


if __name__ == "__main__":
    main()
