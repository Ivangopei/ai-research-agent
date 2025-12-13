import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_pdf

def test_pdf_creation():
    # 1. Setup dummy data
    fake_query = "Test Query"
    fake_report = "This is a test report.\nIt has two lines."
    fake_sources = ["http://google.com", "http://example.com"]

    # 2. Run the function
    pdf_bytes = create_pdf(fake_query, fake_report, fake_sources)

    # 3. Verify the result (Assert)
    assert pdf_bytes is not None
    assert len(pdf_bytes) > 0
    assert b"%PDF" in pdf_bytes  # Checks if the binary data actually looks like a PDF