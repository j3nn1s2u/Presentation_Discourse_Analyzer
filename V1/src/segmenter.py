# src/segmenter.py

def segment_paragraphs(text: str) -> list:
    # Split the text by newlines and remove empty lines
    paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
    return paragraphs