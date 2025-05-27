# batch_run.py
import os
import json
from src.cleaner import clean_text
from src.segmenter import segment_paragraphs
from src.classifier import classify_paragraphs

def main():
    print("=== Starting Presentation Discourse Analyzer V2 ===")
    
    INPUT_DIR = "data_cleaned"
    OUTPUT_DIR = "output"
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if not os.path.exists(INPUT_DIR):
        print(f"Error: Input directory '{INPUT_DIR}' not found.")
        return

    txt_files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".txt")]

    if not txt_files:
        print(f"No .txt files found in {INPUT_DIR}.")
        return

    print(f"Found {len(txt_files)} files to process:")
    for file in txt_files:
        print(f"  - {file}")

    for filename in txt_files:
        print(f"\nProcessing: {filename}")
        input_path = os.path.join(INPUT_DIR, filename)

        try:
            with open(input_path, "r", encoding="utf-8") as file:
                raw_text = file.read()

            print(f"Original text length: {len(raw_text)} characters")

            cleaned = clean_text(raw_text)
            paragraphs = segment_paragraphs(cleaned)
            classified = classify_paragraphs(paragraphs)

            print(f"Segmented into {len(paragraphs)} paragraphs")

            output_filename = filename.replace(".txt", "_classified.json")
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            with open(output_path, "w", encoding="utf-8") as out_file:
                json.dump(classified, out_file, indent=2, ensure_ascii=False)

            print(f"Saved to: {output_path}")

            label_counts = {}
            for item in classified:
                label = item["label"]
                label_counts[label] = label_counts.get(label, 0) + 1

            print("Classification result:")
            for label, count in label_counts.items():
                print(f"  - {label}: {count} paragraphs")

        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
            continue

    print("\nBatch processing completed. Check the 'output' folder for results.")

if __name__ == "__main__":
    main()
