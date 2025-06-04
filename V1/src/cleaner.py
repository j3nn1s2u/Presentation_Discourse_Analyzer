# src/cleaner.py

def clean_text(text: str) -> str:
    import re
    # Preserve paragraph breaks to avoid accidental removal
    text = re.sub(r"\n{2,}", "\n||PARAGRAPH_BREAK||\n", text)
    # Remove extra spaces
    text = re.sub(r"\s{2,}", " ", text)
    # Remove page numbers
    text = re.sub(r"Page \d+", "", text)
    # Restore paragraph breaks
    text = text.replace("||PARAGRAPH_BREAK||", "\n")
    return text.strip()
