import ollama
import chromadb

# Connect to Chroma DB
chroma_client = chromadb.PersistentClient(path="ev_db")
collection = chroma_client.get_collection("ev_manuals")


def ask_question(query, model="qwen:0.5b", top_k=1, temperature=0.2):
    try:
        # 1️⃣ Create embedding for query
        query_embedding = ollama.embeddings(
            model="all-minilm",
            prompt=query
        )["embedding"]

        # 2️⃣ Retrieve similar documents
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        if not documents:
            return "No relevant information found in manuals.", []

        # 3️⃣ Build trimmed context
        context = ""
        sources = []

        for doc, meta in zip(documents, metadatas):
            trimmed_doc = doc[:500]  # limit context size
            context += f"\n\n{trimmed_doc}"

            source_info = f"{meta.get('source', 'Unknown')} - Page {meta.get('page', 'N/A')}"
            sources.append(source_info)

        # 4️⃣ Advanced Prompt Engineering
        prompt = f"""
You are an expert EV diagnostic assistant.

Use ONLY the context below to answer the question.
If answer is not found in context, say:
"The manuals do not contain enough information."

Provide:
- Clear explanation
- Bullet points if needed
- Technical but simple language

Context:
{context}

Question:
{query}

Answer:
"""

        # 5️⃣ Generate answer from LLM
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            options={
                "temperature": temperature
            }
        )

        answer = response["message"]["content"]

        return answer, sources

    except Exception as e:
        return f"Error: {str(e)}", []