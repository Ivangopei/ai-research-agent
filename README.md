# Private AI Research Agent

Always wondered how you search something on Google and then this exact topic appears in one of your FYP videos on TikTok?

The reason is simple, you are being tracked no matter what and where you search any information. This **Private** AI Research Agent solved my problem, and will solve many other people's data privacy issues once I deploy this app for people to use for free.

## Why I Built This?
As a CS student I am very interested in how AI operates under the hood. Particularly, I’ve always been curious about applications where an AI isn't just a chatbot, but a very useful tool for whatever purpose.

Working on this project helped me understand how eyes are given to AI through search API and how to handle data between different services.

## Features


## Tech Stack
* **Python 3.11** - for glueing the code.
* **Streamlit** - for interactive dashboard.
* **Llama 3.2** - local AI.
* **Tavily API** - generated my own API key.
* **FPDF** - for PDF generation.

## How to Run
**NOTE:** You will need to install Ollama and the llama3.2 to be able to run this app.
1. **Clone the repo**
   ```bash

   git clone https://github.com/Ivangopei/ai-research-agent.git
   cd ai-research-agent

2. **Install Dependencies**
   ```bash
   
   pip install -r requirements.txt

3. **API Key**
Open app.py in IDE and find the line where the API key goes. Replace the "PASTE YOUR OWN API KEY HERE" with the API key you will generate for yourself:
   ```bash

   TAVILY_API_KEY = "PASTE YOUR OWN API KEY HERE"

 4. **Launch**
    ```bash

    streamlit run app.py



