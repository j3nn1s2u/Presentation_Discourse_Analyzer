# json_to_md.py

import json
from pathlib import Path

json_path = Path("outputs/classified_paragraphs.json")
markdown_path = Path("outputs/sample_output.md")

with json_path.open("r", encoding="utf-8") as f:
    classified = json.load(f)

md_output = []
for item in classified:
    label = item["label"]
    paragraph = item["paragraph"].strip()
    md_output.append(f"### [{label}]\n{paragraph}\n")

markdown_path.write_text("\n".join(md_output), encoding="utf-8")
print(f"✅ Markdown file saved to: {markdown_path}")
