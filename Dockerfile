# Basis-Image
FROM python:3.10-slim

# Installiere System-Abhängigkeiten inkl. Tesseract und deutscher Sprachdaten
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-deu \
    libtesseract-dev \
    poppler-utils \
    && apt-get clean

# Setze Arbeitsverzeichnis
WORKDIR /app

# Kopiere alle Dateien ins Image
COPY . .

# Installiere Python-Abhängigkeiten
RUN pip install --no-cache-dir -r requirements.txt

# Setze den Entry Point auf das Hauptskript
ENTRYPOINT ["python", "src/ocr_pipeline.py"]
