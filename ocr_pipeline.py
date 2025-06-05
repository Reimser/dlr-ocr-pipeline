import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import mlflow
import json
import os
from sys import platform




pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# ==== KONFIGURATION ====
PDF_PATH = "pdf.pdf"
OUTPUT_JSON = "ocr_output.json"

if platform.startswith("win"):
    poppler_path = r"C:\Tools\poppler-23\poppler-24.08.0\Library\bin"
else:
    poppler_path = None  # unter Linux: kein Pfad nötig
# ==== PDF in Bilder umwandeln ====
print(f"📄 Lade PDF: {PDF_PATH}")
pages = convert_from_path(PDF_PATH, dpi=300, poppler_path=r"C:\Tools\poppler-23\poppler-24.08.0\Library\bin")

# ==== OCR auf jeder Seite ====
ocr_data = {
    "source_file": os.path.basename(PDF_PATH),
    "pages": []
}

for i, page in enumerate(pages):
    print(f"Verarbeite Seite {i+1}/{len(pages)}...")
    text = pytesseract.image_to_string(page, lang="deu")
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    
    ocr_data["pages"].append({
        "page_number": i + 1,
        "content": lines
    })

# ==== JSON speichern ====
with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(ocr_data, f, indent=2, ensure_ascii=False)

print(f"OCR-Ergebnis gespeichert unter: {OUTPUT_JSON}")

# ==== MLflow Logging ====
mlflow.start_run(run_name="pdf_ocr_run")
mlflow.log_param("ocr_tool", "pytesseract")
mlflow.log_param("pages", len(pages))
mlflow.log_artifact(OUTPUT_JSON)
mlflow.end_run()
