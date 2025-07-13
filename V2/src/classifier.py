# src/classifier.py

def classify_paragraph(paragraph: str, index: int, total: int) -> str:
    lower = paragraph.lower()

    if index == 0 or any(word in lower for word in ["hello everyone", "introduction", "opening", "let’s dive in"]):
        return "Opening"

    if index == total - 1 or any(word in lower for word in ["conclusion", "sum up", "to sum up", "in conclusion", "finally"]):
        return "Closing"

    if any(phrase in lower for phrase in [
        "4p marketing model", "4ps", "marketing mix", "product", "price", "place", "promotion"
    ]):
        return "Marketing 4Ps Analysis"

    if any(word in lower for word in [
        "background", "history", "founded", "origin", "campaign goal", "key timing", "results"
    ]):
        return "Background"

    if any(phrase in lower for phrase in [
        "capture hearts", "core message", "visual innovation", "cultural resonance",
        "emotional connection", "viral sharing", "emotional impact", "meeting needs",
        "brand connection", "content value"
    ]):
        return "Research & Value Creation"

    if any(word in lower for word in [
        "suggest", "recommend", "action", "call to action", "next steps", "what should", "how to improve"
    ]):
        return "Action Ideas"

    if index <= 2:
        return "Background"
    elif index >= total - 2:
        return "Closing"
    else:
        return "Research & Value Creation"

def classify_paragraphs(paragraphs: list) -> list:
    total = len(paragraphs)
    return [
        {
            "index": i,
            "paragraph": p.strip(),
            "label": classify_paragraph(p, i, total),
            "length": len(p)
        }
        for i, p in enumerate(paragraphs)
    ]

def get_classification_summary(classified_paragraphs: list) -> dict:
    summary = {}
    for item in classified_paragraphs:
        label = item["label"]
        if label not in summary:
            summary[label] = {"count": 0, "indices": []}
        summary[label]["count"] += 1
        summary[label]["indices"].append(item["index"])
    return summary
