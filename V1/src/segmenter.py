# src/segmenter.py

def segment_paragraphs(text: str) -> list:
    # Split the text by newlines and remove empty lines
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    paragraphs = [p.strip() for p in text.splitlines() if p.strip()]
    return paragraphs
