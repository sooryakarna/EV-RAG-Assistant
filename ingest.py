import os
import ollama
import chromadb
from pypdf import PdfReader

DATA_PATH = "data"
DB_PATH = "ev_db"

# Initialize Chroma persistent database
chroma_client = chromadb.PersistentClient(path=DB_PATH)
collection = chroma_client.get_or_create_collection(name="ev_manuals")


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    pages = []

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()
        if text and len(text.strip()) > 50:
            # Clean excessive newlines
            text = text.replace("\n", " ").strip()
            pages.append({
                "text": text,
                "page": page_number + 1,
                "source": os.path.basename(pdf_path)
            })

    return pages


def chunk_text(text, chunk_size=400, overlap=50):
    """
    Safe chunking to prevent embedding overflow.
    """
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end]

        if len(chunk.strip()) > 100:  # Ignore tiny garbage chunks
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


def main():
    print("🚀 Starting ingestion process...\n")

    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(DATA_PATH, file)
            print(f"📄 Processing: {file}")

            pages = extract_text_from_pdf(pdf_path)

            for page in pages:
                chunks = chunk_text(page["text"])

                for i, chunk in enumerate(chunks):
                    print(f"Embedding Page {page['page']} | Chunk {i+1}")

                    # HARD safety truncate
                    safe_chunk = chunk[:350]

                    try:
                        embedding = ollama.embeddings(
                            model="all-minilm",
                            prompt=safe_chunk
                        )["embedding"]

                        collection.add(
                            ids=[f"{file}_p{page['page']}_c{i}"],
                            embeddings=[embedding],
                            documents=[safe_chunk],
                            metadatas=[{
                                "source": page["source"],
                                "page": page["page"]
                            }]
                        )

                    except Exception as e:
                        print("⚠ Skipping chunk due to embedding error")
                        continue

    print("\n✅ Vector DB created successfully!")


if __name__ == "__main__":
    main()