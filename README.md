# DLR OCR Pipeline

This project implements an OCR (Optical Character Recognition) pipeline for document processing using Python, Tesseract, and MLflow. It includes Docker support and a full CI/CD pipeline via GitHub Actions.

![CI](https://github.com/<your-username>/dlr-ocr-pipeline/actions/workflows/ci.yml/badge.svg)

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install Tesseract OCR:
- Windows: https://github.com/UB-Mannheim/tesseract/wiki
- Linux: `sudo apt-get install tesseract-ocr poppler-utils`
- macOS: `brew install tesseract poppler`

3. Optional: Install the German language model for OCR:
```bash
sudo apt-get install tesseract-ocr-deu
```

## Usage

Run the pipeline locally:
```bash
python ocr_pipeline.py
```

- Input file: `pdf.pdf`
- Output file: `ocr_output.json`
- MLflow logs are stored in the `mlruns/` directory

To launch the MLflow UI:
```bash
mlflow ui
```

## Docker

Build and run the pipeline inside Docker:
```bash
docker build -t dlr-ocr-pipeline .
docker run -v ${PWD}:/app dlr-ocr-pipeline
```

Note: On Windows PowerShell, use `"$PWD"` or the full path instead of `${PWD}`.

## CI/CD

This project includes a GitHub Actions workflow. Each push triggers:
- Dependency installation
- System package setup
- OCR execution
- Basic output validation

View build history and logs under the Actions tab of the repository:
https://github.com/<your-username>/dlr-ocr-pipeline/actions

## Output Format

The OCR pipeline produces a structured JSON file:
```json
{
  "source_file": "pdf.pdf",
  "pages": [
    {
      "page_number": 1,
      "content": [
        "Line 1 text",
        "Line 2 text"
      ]
    }
  ]
}
```