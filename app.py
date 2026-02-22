# print("Hello, I am a text summarizer. Please provide the text you want to summarize.")

import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"

def summarize_text(text):
    """
    Uses deepseek Ai to summarize the given text.
    """
    payload = {
        "model": "deepseek-r1:1.5b",
        "prompt": f"Summarize the following text:\n\n{text}",
        "stream": False,
    }
    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No summary generated.")
    else:
        return f"Error: {response.text}"
    
#creating Gradio interface
interface = gr.Interface(
    fn = summarize_text,
    inputs = gr.Textbox(lines = 10, placeholder = "Enter text to summarize"),
    outputs = gr.Textbox(label = "Summarizer Text"),
    title = "AI-Powered Text Summarizer",
    description = "Enter a block of text and get a concise summary using deepseek Ai."
)

#Lanching the web app
if __name__ == "__main__":
    interface.launch()



# #Test Summarization
# if __name__ == "__main__":
#     sample_text =  """Artificial intelligence (AI) is a branch of computer science that aims to create 
#                     machines capable of performing tasks that typically require human intelligence. These tasks include
#       learning, reasoning, problem-solving, understanding natural language, and perception. AI can be
#         categorized into narrow AI, which is designed for specific tasks, and general AI, which has the 
#         potential to perform any intellectual task that a human can do. The development of AI has led to 
#         advancements in various fields such as healthcare, finance, and transportation, but it also raises 
#         ethical concerns regarding privacy, job displacement, and decision-making transparency."""
#     print("### Summary ###")
#     print(summarize_text(sample_text))