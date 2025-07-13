# json_to_md.py - Convert classified JSON results into Markdown format

import json
import os
from pathlib import Path

def convert_json_to_markdown(json_file_path: str, output_dir: str = "output"):
    json_path = Path(json_file_path)
    
    if not json_path.exists():
        print(f"File not found: {json_file_path}")
        return
    
    with json_path.open("r", encoding="utf-8") as f:
        classified = json.load(f)
    
    md_lines = []
    md_lines.append(f"# {json_path.stem.replace('_classified', '').title()} - Classification Report\n")
    
    current_label = None
    for item in classified:
        label = item["label"]
        paragraph = item["paragraph"].strip()
        
        if label != current_label:
            md_lines.append(f"## {label}\n")
            current_label = label
        
        md_lines.append(f"{paragraph}\n")
    
    output_path = Path(output_dir) / f"{json_path.stem.replace('_classified', '')}_report.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with output_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    
    print(f"Markdown report saved: {output_path}")

def batch_convert_to_markdown(input_dir: str = "output", output_subdir: str = "reports"):
    input_path = Path(input_dir)
    output_dir = input_path / output_subdir
    
    if not input_path.exists():
        print(f"Input directory not found: {input_dir}")
        return
    
    json_files = list(input_path.glob("*_classified.json"))
    
    if not json_files:
        print(f"No classified JSON files found in {input_dir}")
        return
    
    print(f"Converting {len(json_files)} files to Markdown...")
    
    for json_file in json_files:
        convert_json_to_markdown(str(json_file), str(output_dir))
    
    print(f"Batch conversion completed. Check {output_dir} for reports.")

if __name__ == "__main__":
    batch_convert_to_markdown()
