from sentence_transformers import SentenceTransformer
from pdf_loader import load_documents
from chunking import chunk_text

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

def generate_embeddings():

    documents = load_documents()

    all_embeddings = []

    for filename, text in documents.items():

        chunks = chunk_text(text)

        print(f"\nProcessing {filename}")
        print(f"Total Chunks: {len(chunks)}")

        for chunk in chunks:

            embedding = model.encode(chunk)

            all_embeddings.append(
                {
                    "document": filename,
                    "chunk": chunk,
                    "embedding": embedding.tolist()
                }
            )

    return all_embeddings


if __name__ == "__main__":

    embeddings = generate_embeddings()

    print(f"\nTotal Embedded Chunks: {len(embeddings)}")