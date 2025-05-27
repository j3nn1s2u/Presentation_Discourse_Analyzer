# src/cleaner.py
import re

def clean_text(text: str) -> str:
    """
    清理原始文本，移除不必要的格式和標記
    
    Args:
        text (str): 原始文本
        
    Returns:
        str: 清理後的文本
    """
    if not text:
        return ""
    
    # 1. 統一換行符號
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    
    # 2. 移除頁碼和時間戳
    text = re.sub(r"Page \d+", "", text)
    text = re.sub(r"\[\d{1,2}:\d{2}(:\d{2})?\]", "", text)
    
    # 3. 移除講者標記（支援中英文）
    # 中文講者標記：（張三）: 或 (李四):
    text = re.sub(r"[（(]?[一-龥]{2,4}[)）]?\s*[:：]?", "", text)
    # 英文講者標記：(John): 或 Mary:
    text = re.sub(r"[（(]?[A-Z][a-z]{1,15}[)）]?\s*[:：]?", "", text)
    
    # 4. 修復標點符號後缺少空格的問題
    text = re.sub(r"([.,!?])([^\s])", r"\1 \2", text)    # 英文標點
    text = re.sub(r"([。！？])([^\s\n])", r"\1 \2", text)  # 中文標點
    
    # 5. 合併錯誤的換行（非句號結尾的行與下一行合併）
    text = re.sub(r"(?<![.。!?！？])\n(?=\S)", " ", text)
    
    # 6. 移除全大寫的標題行（通常是章節標題）
    text = re.sub(r"^\s*[A-Z\s]{6,}$", "", text, flags=re.MULTILINE)
    
    # 7. 清理多餘的空白
    text = re.sub(r"\n{3,}", "\n\n", text)  # 多個連續換行改為雙換行
    text = re.sub(r"[ \t]+", " ", text)     # 多個空格/Tab改為單一空格
    
    # 8. 移除每行開頭和結尾的空白，並重組文本
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    text = "\n".join(lines)
    
    return text.strip()

def preview_cleaning(text: str, preview_length: int = 500) -> str:
    """
    預覽清理結果，用於除錯
    
    Args:
        text (str): 原始文本
        preview_length (int): 預覽長度
        
    Returns:
        str: 清理後的預覽文本
    """
    cleaned = clean_text(text)
    return cleaned[:preview_length] + ("..." if len(cleaned) > preview_length else "")