
🌸 Introduction

Anime has seen explosive growth in India and across the globe, becoming more than just entertainment—it's a culture. With platforms like MyAnimeList and Crunchyroll gaining millions of users, the demand for instant and intelligent anime information has skyrocketed. But with so much data spread across websites, getting accurate answers quickly isn't always easy.

AnimeSensei is here to change that.

## Watch the Demo 📺
[![YouTube Video](https://img.shields.io/badge/YouTube-Watch%20Video-red?logo=youtube&logoColor=white&style=for-the-badge)](https://youtu.be/iOMw1ATTVio)

🤖 AnimeSensei: AI-Powered Anime Chatbot using RAG, FAISS, and LLMs

![Banner](your_image.png)

📚 What is AnimeSensei?

AnimeSensei is an AI-powered chatbot that uses Retrieval-Augmented Generation (RAG) to provide meaningful, real-time responses about your favorite anime—powered by advanced language models, intelligent web search, and semantic retrieval from actual web pages.

Just provide a URL (e.g., from MyAnimeList), and ask your question. The bot will:
- Scrape and chunk data from the anime webpage.
- Search the web using DuckDuckGo for real-time info.
- Use both sources to generate an accurate, LLM-based answer.

🚀 Tech Stack

| Component              | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 🧠 LLM                 | LLaMA 3.3 70B via Groq API                                                   |
| 📦 Embeddings          | HuggingFace Transformers - MiniLM (sentence-transformers/all-MiniLM-L6-v2) |
| 🧩 Vector Store        | FAISS - Facebook AI Similarity Search                                       |
| 🔎 Search Engine       | DuckDuckGo - Real-time web search API                                       |
| 🧱 Framework           | LangChain for chaining and orchestration                                   |
| 🌐 Web Scraping        | langchain_community.WebBaseLoader                                           |
| 🎨 Frontend            | Streamlit - Interactive Web UI                                              |

🛠️ Features

✅ Ask questions about any anime by just pasting a URL  
✅ Combines web search and page scraping for better context  
✅ Accurate, bullet-pointed responses with source references  
✅ User-friendly UI with zero coding required  
✅ Powered by open-source libraries and Hugging Face models  

📷 Preview

![Image](https://github.com/user-attachments/assets/97e77384-acb2-4a3e-b7b5-d8fcf6bca803)

🧪 How It Works

1. User inputs a URL (like a MyAnimeList anime page)
2. rag.py:
   - Loads the webpage
   - Chunks content using RecursiveCharacterTextSplitter
   - Creates embeddings via Hugging Face
   - Stores them in a FAISS vector store
3. app.py:
   - Takes a user query
   - Uses retriever + DuckDuckGo for dual-context
   - Feeds both into a Groq-powered LLaMA 3.3 70B model
   - Returns a bullet-pointed, context-based answer

📂 File Structure

├── Rag.py                # Handles DuckDuckGo search, RAG setup, FAISS store  
├── app.py                # Streamlit UI, integrates LLM and all backend logic  
├── requirements.txt      # All dependencies  
├── your_image.png        # Homepage banner

🧑‍💻 Getting Started

1. Clone the repo
   git clone https://github.com/DataScientist00/AI-Anime-Chatbot-with-RAG.git
   
   cd AI-Anime-Chatbot-with-RAG

3. Install dependencies
   pip install -r requirements.txt

4. Setup environment
   - Create a .env file and add your GROQ API key:
     GROQ_API_KEY=your_groq_api_key

5. Run the app
   streamlit run app.py

💡 Example Usage

🔗 URL: https://myanimelist.net/anime/5114/Fullmetal_Alchemist__Brotherhood  
❓ Question: "Who are the main characters and their powers?"  
✅ Response:
- Edward Elric is a skilled alchemist who lost his arm and leg in a failed transmutation. [RAG]
- Alphonse Elric is Edward's brother, whose soul is bound to a suit of armor. [RAG]
- Roy Mustang is a Flame Alchemist and a key figure in the military. [Search]

🌍 Why AnimeSensei?

AnimeSensei brings cutting-edge AI to anime fans, helping you explore, research, and understand characters, storylines, and lore in a fun and interactive way.

Whether you're a curious newbie or an anime veteran, this chatbot makes information more accessible, contextual, and instant.

🧠 Future Ideas

- Add support for manga URLs
- Integrate YouTube trailer summaries via API
- Save chat history
- Add voice-based query support

🧾 License

MIT License

🙌 Acknowledgements

- LangChain
- Hugging Face Transformers
- FAISS by Facebook
- DuckDuckGo Search
- Groq Cloud
- Streamlit

## 📞 Contact
For any questions or feedback, reach out to:
- **Email**: nikzmishra@gmail.com
- **YouTube**: [Channel](https://www.youtube.com/@DataScienceSensei/videos)

---

⚡️ Built with love by an anime fan for anime fans.  
Follow the repo and ⭐ it if you found it useful!
