# src/segmenter.py

def segment_paragraphs(text: str, min_length: int = 10) -> list:
    if not text:
        return []
    
    raw_paragraphs = text.split('\n\n')
    
    all_lines = []
    for para in raw_paragraphs:
        lines = [line.strip() for line in para.split('\n') if line.strip()]
        all_lines.extend(lines)
    
    paragraphs = [p for p in all_lines if len(p.strip()) >= min_length]
    
    return paragraphs

def get_paragraph_stats(paragraphs: list) -> dict:
    if not paragraphs:
        return {"total": 0, "avg_length": 0, "min_length": 0, "max_length": 0}
    
    lengths = [len(p) for p in paragraphs]
    
    return {
        "total": len(paragraphs),
        "avg_length": sum(lengths) / len(lengths),
        "min_length": min(lengths),
        "max_length": max(lengths)
    }
