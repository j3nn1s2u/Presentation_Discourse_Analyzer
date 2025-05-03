# src/cleaner.py

def clean_text(text: str) -> str:
    import re
    # Remove multiple blank lines
    text = re.sub(r"\n{2,}", "\n", text)
    # Remove extra spaces
    text = re.sub(r"\s{2,}", " ", text)
    # Remove page numbers like "Page 1"
    text = re.sub(r"Page \d+", "", text)
    return text.strip()

