# Private AI Research Agent

This project is an AI agent made to automate market research while keeping data private. I built this to solve a specific problem: How can we use the power of the live web without sending sensitive research data to the cloud?A local-first AI Agent that automates market research. It creates a privacy-preserving pipeline by integrating the **Tavily Search API** with a locally hosted **Llama 3.2** model.

## Features
* **Agentic Workflow:** The AI autonomously searches the live web for real-time data, connecting Python logic to external tools.
* **Privacy-First Architecture:** Summarization and inference happen 100% locally on-device using Ollama. No sensitive data is sent to cloud AI providers.
* **Automated Reporting:** Generates downloadable, professional-grade PDF research briefs using FPDF.
* **Resource Optimization:** Optimized for consumer hardware using quantized 3B parameter models (Llama 3.2) and context trimming.

## Tech Stack
* **Python 3.11**
* **Streamlit** 
* **Ollama**
* **Tavily API**
* **FPDF**

## How to Run

1. **Clone the repo**
   ```bash

   git clone [https://github.com/Ivangopei/private-research-agent.git](https://github.com/Ivangopei/private-research-agent.git)


