def classify_document(text):
    if "beneficial owner" in text.lower():
        return "UBO Declaration"
    elif "memorandum" in text.lower():
        return "Memorandum of Association"
    elif "articles of association" in text.lower():
        return "Articles of Association"
    else:
        return "Unknown"

def check_missing_documents(doc_types):
    required = {"UBO Declaration", "Memorandum of Association", "Articles of Association"}
    return list(required - set(doc_types))
