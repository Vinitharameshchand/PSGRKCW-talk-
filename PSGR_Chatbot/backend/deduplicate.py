import json

def deduplicate_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    seen = set()
    new_data = []
    for entry in data:
        # Create a unique key based on reply and sorted keywords
        keywords_str = ",".join(sorted(entry.get('keywords', [])))
        key = (entry.get('reply'), keywords_str)
        if key not in seen:
            seen.add(key)
            new_data.append(entry)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(new_data, f, indent=4, ensure_ascii=False)
    
    print(f"Deduplicated {file_path}: {len(data)} -> {len(new_data)} entries.")

if __name__ == "__main__":
    deduplicate_json('data/faqs_merged.json')
