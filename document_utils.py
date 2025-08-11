import fitz  # PyMuPDF

def extract_text(pdf_path):
    """
    Extracts text from a PDF file using PyMuPDF.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        str: Extracted text from all pages.
    """
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        print(f"Error reading PDF: {e}")
    return text
