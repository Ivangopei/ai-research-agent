import streamlit as st
from tavily import TavilyClient
import requests
from fpdf import FPDF
import os # Added for better security

# API KEY - MAKE SURE TO HIDE IT
TAVILY_API_KEY = "YOUR_API_KEY_HERE"

def generate_pdf_report(query, report_content, sources):
    """Simplified PDF generation - looks more like student-written code"""
    pdf = FPDF()
    pdf.add_page()
    
    # TITLE
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"Research Report: {query}", ln=True, align='C')
    pdf.ln(10)
    
    # BODY
    pdf.set_font("Arial", size=12)
    safe_text = report_content.replace('\u2013', '-').replace('\u2014', '-') 
    pdf.multi_cell(0, 10, safe_text)
    
    # SOURCES
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Sources:", ln=True)
    pdf.set_font("Arial", size=10)
    for url in sources:
        pdf.write(5, f"- {url}\n")
    
    return pdf.output(dest='S').encode('latin-1')

# APP SETUP
st.set_page_config(page_title="AI Research Agent", page_icon="🔍")
st.title("🔍 Private Research Agent")
st.write("This agent uses Tavily to search the web and a local Llama 3.2 model to summarize the findings.")

user_query = st.text_input("Enter your research topic:", placeholder="e.g. Future of AI in 2026")

if st.button("Generate Report"):
    if not user_query:
        st.warning("Please enter a topic first!")
    else:
        # SEARCHING
        with st.spinner("Step 1: Searching the web..."):
            try:
                tavily = TavilyClient(api_key=TAVILY_API_KEY)
                search_data = tavily.search(query=user_query, search_depth="basic")
                
                # FEED THE RESULT INTO LLM
                context = ""
                urls = []
                for result in search_data['results']:
                    context += f"\nSource: {result['url']}\nContent: {result['content']}\n"
                    urls.append(result['url'])
            except Exception as e:
                st.error(f"Search Error: {e}")
                st.stop()

        # LLM  ANALYSIS
        with st.spinner("Step 2: Local AI is analyzing the data..."):
            prompt = f"Summarize this research into a professional report with an executive summary and bullet points:\n\n{context}"
            
            try:
                # COMMUNICATING TO LLAMA
                response = requests.post(
                    "http://localhost:11434/api/generate",
                    json={"model": "llama3.2", "prompt": prompt, "stream": False}
                )
                
                if response.status_code == 200:
                    final_report = response.json()["response"]
                    
                    st.success("Report Generated!")
                    st.markdown("### Final Report")
                    st.write(final_report)
                    
                    # PUT RESULTS INTO A PDF FILE
                    report_bytes = generate_pdf_report(user_query, final_report, urls)
                    st.download_button(
                        label="Download PDF",
                        data=report_bytes,
                        file_name="research_report.pdf",
                        mime="application/pdf"
                    )
                else:
                    st.error("Ollama failed to respond. Make sure the server is running.")
            except Exception as e:
                st.error(f"Connection Error: {e}")
