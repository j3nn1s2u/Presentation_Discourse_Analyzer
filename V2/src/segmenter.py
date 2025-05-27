# src/segmenter.py

def segment_paragraphs(text: str, min_length: int = 10) -> list:
    """
    將清理後的文本分割成段落
    
    Args:
        text (str): 清理後的文本
        min_length (int): 段落最小長度，過短的段落會被過濾
        
    Returns:
        list: 段落列表
    """
    if not text:
        return []
    
    # 以雙換行分割段落，然後清理空段落
    raw_paragraphs = text.split('\n\n')
    
    # 進一步處理：以單換行分割，但保留有意義的段落
    all_lines = []
    for para in raw_paragraphs:
        lines = [line.strip() for line in para.split('\n') if line.strip()]
        all_lines.extend(lines)
    
    # 過濾掉過短的段落
    paragraphs = [p for p in all_lines if len(p.strip()) >= min_length]
    
    return paragraphs

def get_paragraph_stats(paragraphs: list) -> dict:
    """
    獲取段落統計資訊，用於分析
    
    Args:
        paragraphs (list): 段落列表
        
    Returns:
        dict: 統計資訊
    """
    if not paragraphs:
        return {"total": 0, "avg_length": 0, "min_length": 0, "max_length": 0}
    
    lengths = [len(p) for p in paragraphs]
    
    return {
        "total": len(paragraphs),
        "avg_length": sum(lengths) / len(lengths),
        "min_length": min(lengths),
        "max_length": max(lengths)
    }