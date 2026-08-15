print("1. retrieval.py started")

import chromadb
print("2. chromadb imported")

from backend.LLM import generate_answer
print("3. LLM imported")

from sentence_transformers import SentenceTransformer
print("4. sentence-transformers imported")

model = SentenceTransformer("BAAI/bge-small-en-v1.5")
print("5. Embedding model loaded")

client = chromadb.PersistentClient(path="medical_db")
print("6. Chroma client created")

collection = client.get_collection("medical_documents")
print("7. Collection loaded")


def retrieve_answer(question):

    query_embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=1
    )

    print("\n========== Retrieved Documents ==========\n")

    for i, doc in enumerate(results["documents"][0]):
        print(f"\nDocument {i+1}\n")
        print(doc)

    # Create the context
    documents = results["documents"][0]

    if not documents:
        return "no relevant medical information found"

    context = "\n\n".join(documents)

    print("\n========== Context Sent to LLM ==========\n")
    print(context)

    answer = generate_answer(question, context)

    return answer

    print("reached eof")


if __name__ == "__main__":
    print("inside main")

    question = input("Ask a medical question: ")

    answer = retrieve_answer(question)

    print("\n====================")
    print("Medical AI Answer")
    print("====================\n")
    print(answer)