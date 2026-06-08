from pypdf import PdfWriter
import os
os.chdir(r"C:\Users\sujan\OneDrive\Desktop\it is a random snake lang\excercises\ex8\hehe")
merger = PdfWriter()
files=[file for file in os.listdir() if file.endswith(".pdf")]
for pdf in files:
    merger.append(pdf)
os.chdir(r"C:\Users\sujan\OneDrive\Desktop\it is a random snake lang\excercises\ex8\merged_pdf")
merger.write("lab2_ics_213.pdf")
merger.close()

