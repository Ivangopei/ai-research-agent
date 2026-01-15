import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from app import generate_pdf_report

def test_pdf_creation():
    # "DUMMY" DATA
    fake_query = "Test Research Topic"
    fake_report = "This is a simulated research report.\nIt contains multiple lines for testing."
    fake_sources = ["https://google.com", "https://example.com"]

    # CALL THE FUNCTION
    pdf_bytes = generate_pdf_report(fake_query, fake_report, fake_sources)

    # CHECK THE RESULTS
    assert pdf_bytes is not None, "The PDF output should not be None"
    assert len(pdf_bytes) > 0, "The PDF output should not be empty"
    
    # LOOKS LIKE PDF?
    assert b"%PDF" in pdf_bytes, "The output data does not look like a valid PDF"

    print("✅ PDF Generation Test Passed!")

if __name__ == "__main__":
    test_pdf_creation()
