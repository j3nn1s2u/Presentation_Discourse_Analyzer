# src/cleaner.py
import re

def clean_text(text: str) -> str:
    if not text:
        return ""
    
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"Page \d+", "", text)
    text = re.sub(r"\[\d{1,2}:\d{2}(:\d{2})?\]", "", text)
    text = re.sub(r"[（(]?[一-龥]{2,4}[)）]?\s*[:：]?", "", text)
    text = re.sub(r"[（(]?[A-Z][a-z]{1,15}[)）]?\s*[:：]?", "", text)
    text = re.sub(r"([.,!?])([^\s])", r"\1 \2", text)
    text = re.sub(r"([。！？])([^\s\n])", r"\1 \2", text)
    text = re.sub(r"(?<![.。!?！？])\n(?=\S)", " ", text)
    text = re.sub(r"^\s*[A-Z\s]{6,}$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    text = "\n".join(lines)
    
    return text.strip()

def preview_cleaning(text: str, preview_length: int = 500) -> str:
    cleaned = clean_text(text)
    return cleaned[:preview_length] + ("..." if len(cleaned) > preview_length else "")
