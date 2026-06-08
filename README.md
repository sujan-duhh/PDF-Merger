# PDF Merger

A simple and portable Python application that merges multiple PDF files into a single PDF document using the `pypdf` library.

## Features

* Merge multiple PDF files into one document
* Automatically detects PDF files in the project directory
* Cross-platform support (Windows, Linux, and macOS)
* Uses `pathlib` for portable file handling
* Automatically creates the output directory if it doesn't exist
* Lightweight and easy to use

## Technologies Used

* Python
* pypdf
* pathlib

## Project Structure

```text
pdf-merger/
│
├── ex8.py
├── pdf1.pdf
├── pdf2.pdf
├── pdf3.pdf
└── merged_pdf/
```

## How It Works

1. The script scans the project directory for PDF files.
2. All detected PDFs are merged in sorted order.
3. The merged document is saved inside the `merged_pdf` folder.

## Learning Outcomes

* File handling with Python
* Working with PDFs using `pypdf`
* Cross-platform path management using `pathlib`
* Basic automation and scripting
* Writing portable and maintainable Python code
