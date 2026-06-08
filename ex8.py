from pypdf import PdfWriter
from pathlib import Path

# Folder where this script is located
base_dir = Path(__file__).resolve().parent

# Output folder
output_dir = base_dir / "merged_pdf"
output_dir.mkdir(exist_ok=True)

# Output file
output_file = output_dir / "merged-pdf.pdf"

merger = PdfWriter()

pdf_files = sorted(base_dir.glob("*.pdf"))

for pdf in pdf_files:
    merger.append(str(pdf))

merger.write(str(output_file))
merger.close()

print(f"Merged PDF saved to: {output_file}")

