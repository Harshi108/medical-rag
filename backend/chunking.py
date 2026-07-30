from pdf_loader import load_documents
def chunk_text(text, chunk_size = 300, overlap = 50):

    words = text.split()
    chunks = []
    start = 0
    
    while start < len(words):
        end = start + chunk_size
        chunk =  " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks    

if __name__ == "__main__":

    documents = load_documents()

    for filename, text in documents.items():
        chunks = chunk_text(text)
        print("=" * 60)
        print(filename)
        print("number of chunks", len(chunks))

        print("\n first chunk: \n")
        print(chunks[0][:500])

        print("=" * 60)
