# Private AI Research Agent

Always wondered how you search something on Google and then this exact topic appears in one of your FYP videos on TikTok? The reason is simple, you are being tracked no matter what and where you search any information. This **Private** AI Research Agent solved my problem, and will solve many other people's data privacy issues. 

This project is an AI agent made to automate market research while keeping data private. I built this to solve a specific problem: A local-first AI Agent that automates market research. It creates a privacy-preserving pipeline by integrating the **Tavily Search API** with a locally hosted **Llama 3.2** model.

## Features
* **Agentic Workflow:** The AI autonomously searches the live web for real-time data, connecting Python logic to external tools.
* **Privacy-First Architecture:** Summarization and inference happen 100% locally on-device using Ollama. No sensitive data is sent to cloud AI providers.
* **Automated Reporting:** Generates downloadable, professional-grade PDF research briefs using FPDF.
* **Resource Optimization:** Optimized for consumer hardware using quantized 3B parameter models (Llama 3.2) and context trimming.

## Tech Stack
* **Python 3.11** 
* **Streamlit** 
* **Llama 3.2**
* **Tavily API**
* **FPDF**

## How to Run
**NOTE:** You will need Ollama and the llama3.2 model installed to be able to run this app.
1. **Clone the repo**
   ```bash

   git clone https://github.com/Ivangopei/ai-research-agent.git
   cd ai-research-agent



