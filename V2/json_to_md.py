# json_to_md.py - 將分類結果轉換為 Markdown 格式的工具
import json
import os
from pathlib import Path

def convert_json_to_markdown(json_file_path: str, output_dir: str = "output"):
    """
    將單個分類 JSON 檔案轉換為 Markdown
    
    Args:
        json_file_path (str): JSON 檔案路徑
        output_dir (str): 輸出目錄
    """
    json_path = Path(json_file_path)
    
    if not json_path.exists():
        print(f"❌ File not found: {json_file_path}")
        return
    
    # 讀取 JSON 資料
    with json_path.open("r", encoding="utf-8") as f:
        classified = json.load(f)
    
    # 產生 Markdown 內容
    md_lines = []
    md_lines.append(f"# {json_path.stem.replace('_classified', '').title()} - Classification Report\n")
    
    current_label = None
    for item in classified:
        label = item["label"]
        paragraph = item["paragraph"].strip()
        
        # 如果標籤改變，新增標題
        if label != current_label:
            md_lines.append(f"## {label}\n")
            current_label = label
        
        md_lines.append(f"{paragraph}\n")
    
    # 儲存 Markdown 檔案
    output_path = Path(output_dir) / f"{json_path.stem.replace('_classified', '')}_report.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with output_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    
    print(f"✅ Markdown report saved: {output_path}")

def batch_convert_to_markdown(input_dir: str = "output", output_subdir: str = "reports"):
    """
    批次轉換所有 JSON 檔案為 Markdown
    
    Args:
        input_dir (str): JSON 檔案所在目錄
        output_subdir (str): Markdown 輸出子目錄
    """
    input_path = Path(input_dir)
    output_dir = input_path / output_subdir
    
    if not input_path.exists():
        print(f"❌ Input directory not found: {input_dir}")
        return
    
    json_files = list(input_path.glob("*_classified.json"))
    
    if not json_files:
        print(f"❌ No classified JSON files found in {input_dir}")
        return
    
    print(f"📋 Converting {len(json_files)} files to Markdown...")
    
    for json_file in json_files:
        convert_json_to_markdown(str(json_file), str(output_dir))
    
    print(f"🎉 Batch conversion completed! Check {output_dir} for reports.")

if __name__ == "__main__":
    # 可以選擇單檔轉換或批次轉換
    batch_convert_to_markdown()