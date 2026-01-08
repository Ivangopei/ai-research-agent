import streamlit as st
from tavily import TavilyClient
import requests
from fpdf import FPDF

# API KEY (HIDDEN FOR SECURITY & PRIVACY PURPOSES)
TAVILY_API_KEY = "THE KEY GOES HERE"

# --- PDF GENERATION CLASS ---
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Private Research Agent Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_pdf(query, report_text, sources):
    pdf = PDF()
    pdf.add_page()
    
    # Title (The Query)
    pdf.set_font("Arial", "B", 16)
    pdf.multi_cell(0, 10, f"Research: {query}")
    pdf.ln(5)
    
    # The Report Content
    pdf.set_font("Arial", "", 12)
    # Basic cleanup for PDF encoding
    clean_text = report_text.encode('latin-1', 'ignore').decode('latin-1')
    pdf.multi_cell(0, 10, clean_text)
    pdf.ln(10)
    
    # Sources Section
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Sources Used:", 0, 1)
    pdf.set_font("Arial", "I", 10)
    for source in sources:
        clean_source = source.encode('latin-1', 'ignore').decode('latin-1')
        pdf.multi_cell(0, 8, f"- {clean_source}")
        
    return pdf.output(dest='S').encode('latin-1')

# --- PAGE SETUP ---
st.set_page_config(page_title="Private Research Agent", page_icon="🕵️")

st.title("🕵️ Private Research Agent")
st.caption("Powered by Tavily & Llama 3.2 | Export to PDF")

# --- USER INPUT ---
topic = st.text_input("What do you want to research?")

# --- MAIN LOGIC ---
if st.button("Start Research") and topic:
    with st.spinner("Searching the live internet..."):
        try:
            tavily = TavilyClient(api_key=TAVILY_API_KEY)
            response = tavily.search(query=topic, search_depth="basic", max_results=3)
            
            # Optimization: Limit content to speed up CPU
            context_text = "\n\n".join([
                f"Source: {result['url']}\nContent: {result['content'][:1000]}" 
                for result in response['results']
            ])
            
            # Save sources for the PDF later
            source_urls = [result['url'] for result in response['results']]

        except Exception as e:
            st.error(f"Search failed: {e}")
            st.stop()

    with st.spinner("Writing report..."):
        prompt = f"""
        You are a research assistant. Summarize the following data into a professional report.
        
        DATA:
        {context_text}
        
        INSTRUCTIONS:
        - Start with an Executive Summary.
        - Use bullet points for key findings.
        - Be concise.
        """

        try:
            ollama_response = requests.post(
                "http://localhost:11434/api/generate", 
                json={"model": "llama3.2", "prompt": prompt, "stream": False}
            )
            
            if ollama_response.status_code == 200:
                report_content = ollama_response.json()["response"]
                
                # --- DISPLAY REPORT ---
                st.subheader("📝 Research Report")
                st.markdown(report_content)
                
                # --- PDF EXPORT BUTTON ---
                pdf_data = create_pdf(topic, report_content, source_urls)
                
                st.download_button(
                    label="📄 Download Report as PDF",
                    data=pdf_data,
                    file_name=f"research_report.pdf",
                    mime="application/pdf"
                )
                
            else:
                st.error(f"Ollama Error: {ollama_response.text}")

        except Exception as e:

            st.error(f"Connection failed: {e}")

