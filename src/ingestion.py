import pymupdf as fitz  # PyMuPDF
from pathlib import Path

def extract_pages(pdf_path):
    """Return a list of {source, page, text} for each non-empty page."""
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc, start=1):
        text = page.get_text().strip()
        if text:
            pages.append({
                "source": Path(pdf_path).name,
                "page": i,
                "text": text,
            })
    return pages

def load_all(folder="data/pdfs"):
    all_pages = []
    for pdf in Path(folder).glob("*.pdf"):
        pages = extract_pages(pdf)
        print(f"{pdf.name}: {len(pages)} pages with text")
        all_pages.extend(pages)
    return all_pages

if __name__ == "__main__":
    pages = load_all()
    print(f"\nTotal pages: {len(pages)}")
    print(pages[0]["text"][:500])