# main.py

import json
from pathlib import Path
from src.cleaner import clean_text
from src.segmenter import segment_paragraphs
from src.classifier import classify_paragraphs

def main():
    input_path = Path("data/nike_raw.txt")
    output_path = Path("outputs/classified_paragraphs.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        print("[ERROR] Input file not found: data/nike_raw.txt")
        return

    with input_path.open("r", encoding="utf-8") as f:
        raw_text = f.read()

    print(f"-> Original character count: {len(raw_text)}")

    cleaned = clean_text(raw_text)
    paragraphs = segment_paragraphs(cleaned)
    print(f"-> Number of paragraphs detected: {len(paragraphs)}")

    if not paragraphs:
        print("[WARNING] No paragraphs found. Please check the input format.")
        return

    classified = classify_paragraphs(paragraphs)

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(classified, f, indent=2, ensure_ascii=False)

    print(f"YES! Classification completed. Output saved to {output_path}")
    for i, item in enumerate(classified[:5]):
        print(f"[{item['label']}] {item['paragraph'][:60]}...")

if __name__ == "__main__":
    main()
