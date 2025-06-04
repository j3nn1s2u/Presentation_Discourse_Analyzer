# src/classifier.py

def classify_paragraph(paragraph: str, index: int, total: int) -> str:
    lower = paragraph.lower()

    # First check for Opening (first paragraph or explicit opening words)
    if index == 0 or any(word in lower for word in ["hello everyone", "introduction", "opening", "let’s dive in"]):
        return "Opening"

    # Then check for Closing (last paragraph or explicit closing words)
    if index == total - 1 or any(word in lower for word in ["conclusion", "sum up", "to sum up", "in conclusion", "finally"]):
        return "Closing"

    # Check for Marketing 4Ps (stronger keywords and patterns)
    if any(phrase in lower for phrase in [
        "4p marketing model", "4ps", "marketing mix", "product", "price", "place", "promotion"
    ]):
        return "Marketing 4Ps Analysis"

    # Check for Background information
    if any(word in lower for word in [
        "background", "history", "founded", "origin", "campaign goal", "key timing", "results"
    ]):
        return "Background"

    # Check for Research & Value Creation
    if any(phrase in lower for phrase in [
        "capture hearts", "core message", "visual innovation", "cultural resonance",
        "emotional connection", "viral sharing", "emotional impact", "meeting needs",
        "brand connection", "content value"
    ]):
        return "Research & Value Creation"

    # Check for Action Ideas
    if any(word in lower for word in [
        "suggest", "recommend", "action", "call to action", "next steps", "what should", "how to improve"
    ]):
        return "Action Ideas"

    # Default fallback based on position
    if index <= 2:
        return "Background"
    elif index >= total - 2:
        return "Closing"
    else:
        return "Research & Value Creation"


def classify_paragraphs(paragraphs: list) -> list:
    total = len(paragraphs)
    return [
        {"paragraph": p, "label": classify_paragraph(p, i, total)}
        for i, p in enumerate(paragraphs)
    ]
