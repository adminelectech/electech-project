import os
import re
import json
from html.parser import HTMLParser

class TitleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title = data

def sync_search():
    root_dir = "."
    search_index = []
    
    # Folders to scan
    folders = ["", "Tech 1", "diplomes", "emploi", "utilisateur"]
    
    for folder in folders:
        folder_path = os.path.join(root_dir, folder)
        if not os.path.exists(folder_path):
            continue
            
        for file in os.listdir(folder_path):
            if file.endswith(".html") and "login" not in file:
                file_path = os.path.join(folder, file).replace("\\", "/")
                full_path = os.path.join(folder_path, file)
                
                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        parser = TitleParser()
                        parser.feed(content)
                        
                        # Extract "main" content text
                        # Simple approach: remove tags, script, style
                        text_content = re.sub(r'<(script|style|header|footer)[^>]*>.*?</\1>', '', content, flags=re.DOTALL | re.IGNORECASE)
                        text_content = re.sub(r'<[^>]+>', ' ', text_content)
                        text_content = re.sub(r'\s+', ' ', text_content).strip()
                        
                        title = parser.title.replace(" - Electech", "").strip()
                        if not title: title = file.replace(".html", "").capitalize()
                            
                        search_index.append({
                            "url": file_path,
                            "title": title,
                            "content": text_content[:5000] # Cap content for size
                        })
                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")

    # Save as JS file for local protocol compatibility
    output_path = os.path.join(root_dir, "js", "search_index.js")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("window.SEARCH_DATA = ")
        json.dump(search_index, f, indent=4, ensure_ascii=False)
        f.write(";")
    
    print(f"Search index updated with {len(search_index)} pages (JS format).")

if __name__ == "__main__":
    sync_search()
