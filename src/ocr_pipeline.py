import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import mlflow
import json
import os
import platform

# OCR-Konfiguration
OCR_LANG = "deu"
INPUT_PDF = "data/pdf.pdf"
OUTPUT_JSON = "data/ocr_output.json"

# Poppler-Konfiguration je nach Betriebssystem
poppler_path = None
if platform.system() == "Windows":
    poppler_path = r"C:\Tools\poppler-23\poppler-24.08.0\Library\bin"
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    os.environ["TESSDATA_PREFIX"] = r"C:\Program Files\Tesseract-OCR\tessdata"

# Lade PDF
print(f"📄 Lade PDF: {INPUT_PDF}")
pages = convert_from_path(INPUT_PDF, dpi=300, poppler_path=poppler_path)

# OCR durchlaufen
ocr_data = {"source_file": INPUT_PDF, "pages": []}

for i, page in enumerate(pages):
    print(f"🔍 Verarbeite Seite {i+1}/{len(pages)}...")
    text = pytesseract.image_to_string(page, lang=OCR_LANG)
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    ocr_data["pages"].append({"page_number": i+1, "content": lines})

# JSON speichern
with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
    json.dump(ocr_data, f, indent=2, ensure_ascii=False)

print(f"✅ OCR-Ergebnis gespeichert unter: {OUTPUT_JSON}")

# MLflow Logging
mlflow.start_run()
mlflow.log_param("pages", len(pages))
mlflow.log_artifact(OUTPUT_JSON)
mlflow.end_run()
