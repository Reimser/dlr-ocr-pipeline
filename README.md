# DLR OCR Pipeline

This project implements an OCR (Optical Character Recognition) pipeline for document processing.

## Setup

1. Install dependencies :
```bash
pip install -r requirements.txt
```

2. Install Tesseract OCR:
- Windows: Download and install from https://github.com/UB-Mannheim/tesseract/wiki
- Linux: `sudo apt-get install tesseract-ocr`
- macOS: `brew install tesseract`

## Usage

Run the pipeline:
```bash
python ocr_pipeline.py
```

## Docker

Build and run with Docker:
```bash
docker build -t dlr-ocr-pipeline .
docker run dlr-ocr-pipeline
``` 