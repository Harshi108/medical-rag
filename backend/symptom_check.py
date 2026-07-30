import chromadb 
from sentence_transformers import SentenceTransformer
from LLM import generate_answer

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

client = chromadb.PersistentClient(path = "medical_db")
collection = client.get_collection("medical_documents")

print("------Medical Symptom Checker-------\n")

symptoms = input("enter the symptoms(comma separated):")

query_embedding = model.encode(symptoms).tolist()

results = collection.query(
    query_embeddings = [query_embedding],
    n_results = 1,
    max_new_tokens = 150,
    do_sample=False
)

context = "\n\n".join(results["documents"][0])
context = context[:1500]

prompt = f"""
You are a Medical AI assistant

the patient reports these symptoms:
{symptoms}

using only the medical context below, identfy the possible diseases

for each disease provide:
1.Disease name
2.Why it matches these symptomes
3.Common symptoms
4.Advise the user to consult a healthcare professional

Do not make a definitive diagnosis.

Medical COntext:
{context}
"""
answer = generate_answer(prompt = prompt)

print("\n==================")
print("possible dieases")
print("====================")
print(answer)