from fpdf import FPDF
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!')
pdf.output('tuto1.pdf', 'F')