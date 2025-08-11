from docx import Document

def insert_comments(doc_path, comments, output_path):
    doc = Document(doc_path)
    for para in doc.paragraphs:
        for comment in comments:
            if comment['text'] in para.text:
                para.text += f"  [Comment: {comment['comment']}]"
    doc.save(output_path)
