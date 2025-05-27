# src/classifier.py

def classify_paragraph(paragraph: str, index: int, total: int) -> str:
    """
    基於關鍵字和位置的規則分類段落
    
    Args:
        paragraph (str): 段落內容
        index (int): 段落在文檔中的索引（從0開始）
        total (int): 文檔總段落數
        
    Returns:
        str: 分類標籤
    """
    lower = paragraph.lower()
    
    # 定義各類別的關鍵字
    keywords = {
        "Opening": [
            "introduction", "opening", "welcome", "today", "present", 
            "hello", "good morning", "good afternoon", "start", "begin"
        ],
        "Background": [
            "history", "background", "founded", "origin", "established", 
            "company", "brand", "story", "started", "began", "since"
        ],
        "Research & Value Creation": [
            "interview", "survey", "insight", "value", "data", "research",
            "capture hearts", "emotion", "engagement", "authenticity", 
            "brand loyalty", "customer", "target audience", "findings"
        ],
        "Marketing 4Ps Analysis": [
            "product", "price", "place", "promotion", "4ps", "marketing mix", 
            "strategy", "media", "execution", "message", "campaign", 
            "advertisement", "ad strategy", "marketing", "distribution"
        ],
        "Action Ideas": [
            "suggest", "recommend", "action", "strategy", "proposal", 
            "call to action", "next steps", "implementation", "plan",
            "should", "could", "would recommend", "opportunity"
        ],
        "Closing": [
            "conclusion", "closing", "thank you", "thanks", "questions",
            "summary", "end", "finally", "wrap up", "any questions"
        ]
    }
    
    # 位置權重：開頭和結尾段落的特殊處理
    if index == 0:
        # 第一段很可能是開場
        if any(word in lower for word in keywords["Opening"]):
            return "Opening"
    
    if index >= total - 2:
        # 最後兩段很可能是結論或結尾
        if any(word in lower for word in keywords["Closing"]):
            return "Closing"
        if any(word in lower for word in keywords["Action Ideas"]):
            return "Action Ideas"
    
    # 依序檢查各類別關鍵字
    for category, words in keywords.items():
        if any(word in lower for word in words):
            return category
    
    # 預設分類：如果沒有明確關鍵字，依據位置推測
    if index == 0:
        return "Opening"
    elif index >= total - 2:
        return "Closing"
    else:
        return "Background"  # 中間段落預設為背景資訊

def classify_paragraphs(paragraphs: list) -> list:
    """
    對段落列表進行批次分類
    
    Args:
        paragraphs (list): 段落列表
        
    Returns:
        list: 包含段落內容和分類標籤的字典列表
    """
    if not paragraphs:
        return []
    
    total = len(paragraphs)
    classified = []
    
    for i, paragraph in enumerate(paragraphs):
        label = classify_paragraph(paragraph, i, total)
        classified.append({
            "index": i,
            "paragraph": paragraph.strip(),
            "label": label,
            "length": len(paragraph)
        })
    
    return classified

def get_classification_summary(classified_paragraphs: list) -> dict:
    """
    獲取分類結果摘要，用於 V2 結構完整性分析
    
    Args:
        classified_paragraphs (list): 分類結果
        
    Returns:
        dict: 各類別統計資訊
    """
    summary = {}
    
    for item in classified_paragraphs:
        label = item["label"]
        if label not in summary:
            summary[label] = {"count": 0, "indices": []}
        
        summary[label]["count"] += 1
        summary[label]["indices"].append(item["index"])
    
    return summary