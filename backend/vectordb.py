import chromadb
from embeddings import generate_embeddings

client = chromadb.PersistentClient(path="medical_db")

collection = client.get_or_create_collection(
    name="medical_documents"
)

all_embeddings = generate_embeddings()

for i, item in enumerate(all_embeddings):

    collection.add(
        ids=[str(i)],
        documents=[item["chunk"]],
        embeddings=[item["embedding"]],
        metadatas=[{"source": item["document"]}]
    )

print("\nTotal vectors stored:", collection.count())