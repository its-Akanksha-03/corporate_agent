import json

def generate_summary(documents, missing, comments, output_path="summary.json"):
    summary = {
        "documents": documents,
        "missing_documents": missing,
        "comments": comments
    }
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)
