# src/classifier.py

def classify_paragraph(paragraph: str, index: int, total: int) -> str:
    lower = paragraph.lower()

    if index == 0 or any(word in lower for word in ["introduction", "opening"]):
        return "Opening"
    elif any(word in lower for word in ["history", "background", "founded", "origin"]):
        return "Background"
    elif any(word in lower for word in [
        "interview", "survey", "insight", "value", "data",
        "capture hearts", "emotion", "engagement", "authenticity", "brand loyalty"
    ]):
        return "Research & Value Creation"
    elif any(word in lower for word in [
        "product", "price", "place", "promotion",
        "4ps", "marketing mix", "strategy", "media", "execution", "message",
        "you can't stop us", "campaign breakdown", "ad strategy", "why this campaign"
    ]):
        return "Marketing 4Ps Analysis"
    elif any(word in lower for word in ["suggest", "recommend", "action", "strategy", "call to action"]):
        return "Action Ideas"
    elif index >= total - 2:
        return "Closing"
    else:
        return "Background"

def classify_paragraphs(paragraphs: list) -> list:
    total = len(paragraphs)
    return [
        {"paragraph": p, "label": classify_paragraph(p, i, total)}
        for i, p in enumerate(paragraphs)
    ]
