# corporate_agent
# 🧾 Corporate Agent – ADGM Legal Assistant

This tool reviews corporate legal documents for compliance with ADGM regulations using simulated Retrieval-Augmented Generation (RAG).

## 🚀 Features

- Upload `.docx` files for review
- Detect red flags like incorrect jurisdiction, missing clauses, and structural issues
- Simulate RAG using reference documents
- Output reviewed `.docx` with comments
- Generate a JSON summary of issues

## 📂 Folder Structure

corporate-agent-adgm/
├── main.py
├── checklist.json
├── reference_docs/
│   ├── ADGM_Regulations_2020.pdf
│   └── Document_Upload_Categories.txt
├── reviewed.docx
├── summary.json
├── README.md
├── requirements.txt

## 🧪 How to Use
1. Run the app:
   ```bash
   python main.py
Upload .docx files via the Gradio interface.

Download:

reviewed.docx with comments

summary.json with issue breakdown


### 6. **RAG Simulation Explanation**
```markdown
## 🧠 RAG Simulation
Reference documents in `reference_docs/` are used to simulate retrieval-based validation. The app checks uploaded documents against these for compliance.

## 📌 Requirements
Install dependencies:
```bash
pip install -r requirements.txt

### 8. **Author Info**
```markdown
## 📝 Author
Akanksha 
