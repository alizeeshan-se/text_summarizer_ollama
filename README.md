AI-Powered Text Summarizer (Local LLM)

This project is an AI-powered text summarization web application built using:

 DeepSeek-R1 (1.5B) LLM

 Ollama (Local LLM runtime)

 Gradio (Web Interface)

 Python

It summarizes long text into concise summaries without requiring internet access, as the model runs locally using Ollama.

 Features

✅ Fully offline AI summarization

✅ Uses DeepSeek-R1:1.5B model locally

✅ Simple and clean Gradio UI

✅ Fast inference

✅ Lightweight and beginner-friendly

 Technologies Used

Python

Gradio

Requests

Ollama

DeepSeek-R1:1.5B

 Installation & Setup
 Install Ollama

Download from:
 https://ollama.com

Then pull the model:

ollama pull deepseek-r1:1.5b
2️⃣ Clone the Repository
git clone https://github.com/alizeeshan-se/text_summarizer_ollama.git
cd text-summarizer-ollama
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Application

Make sure Ollama is running:

ollama run deepseek-r1:1.5b

Then in another terminal:

python app.py

The Gradio interface will open in your browser.

 How It Works

User enters text in Gradio UI.

Text is sent to Ollama local server (localhost:11434).

DeepSeek model generates a summary.

Summary is displayed in UI.

 Project Objective

This project demonstrates:

Integration of Local LLMs

API communication using requests

Building AI web apps using Gradio

Running AI models without cloud dependency


 Author

Zeeshan Ali
Aspiring AI & Machine Learning Engineer
