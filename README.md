# EV-RAG-Assistant
AI-powered EV Diagnostic Assistant using RAG (Retrieval-Augmented Generation) to analyze electric vehicle manuals and provide intelligent troubleshooting support.
🚗 EV RAG Assistant
AI-Powered Electric Vehicle Diagnostic Chatbot

The EV RAG Assistant is an intelligent chatbot system built using Retrieval-Augmented Generation (RAG) that helps diagnose and troubleshoot electric vehicle (EV) issues by analyzing technical manuals and documentation.

It allows users (technicians, students, EV users) to ask questions in natural language and receive accurate, context-aware answers extracted from EV manuals.

📌 Features
🔍 Semantic Search over EV Manuals
🤖 AI Chatbot for EV Diagnostics
📄 Supports multiple PDF manuals (service, training, OEM docs)
⚡ Fast retrieval using vector database (ChromaDB)
🧠 Context-aware responses using LLM
💬 Interactive chat interface
🛠️ Modular design (ingestion + chatbot + UI)
🏗️ Project Structure
ev_rag_assistant/
│── app.py                # Main application (UI / entry point)
│── chatbot.py           # Chatbot logic with RAG pipeline
│── ingest.py            # Data ingestion & embedding generation
│── requirements.txt     # Dependencies
│
├── data/                # EV manuals (PDFs)
│   ├── ev_service_manual.pdf
│   ├── ev_training_manual.pdf
│   ├── tata_ev_manual.pdf
│
├── db/                  # Vector database (ChromaDB)
├── ev_db/               # Secondary DB (if used)
└── venv/                # Virtual environment (ignore in GitHub)
⚙️ How It Works (RAG Pipeline)
📥 Data Ingestion
EV manuals (PDFs) are loaded
Text is split into chunks
Embeddings are generated
🗄️ Vector Storage
Stored in ChromaDB
Enables fast semantic retrieval
❓ User Query
User asks a question (e.g., battery issue)
🔎 Retriever
Finds relevant document chunks
🤖 LLM Response
Combines retrieved data + AI model
Generates accurate answer
🧪 Example Use Cases
🔋 Battery not charging diagnosis
⚠️ Error code explanations
🔧 Maintenance procedures
📘 Understanding EV components
🎓 Learning EV technology
🚀 Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/ev-rag-assistant.git
cd ev-rag-assistant
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
3️⃣ Install Dependencies
pip install -r requirements.txt
📥 Data Ingestion

Run the ingestion script to process EV manuals:

python ingest.py
▶️ Run the Application
python app.py
📦 Requirements
Python 3.8+
LangChain
ChromaDB
OpenAI / LLM API
PyPDF / document loaders
🔐 Environment Variables

Create a .env file:

OPENAI_API_KEY=your_api_key_here
📊 Tech Stack
Python
LangChain
ChromaDB
LLM (OpenAI / compatible)
Streamlit / CLI (based on your app.py)
🎯 Future Improvements
🌐 Web deployment (Streamlit Cloud / Flask)
📱 Mobile-friendly UI
🧾 More EV datasets
🧠 Fine-tuned EV model
🔊 Voice-based assistant
🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

📜 License

This project is for educational and research purposes.

👨‍💻 Author

SOORYA
B.E. CSE | AI & ML Enthusiast
