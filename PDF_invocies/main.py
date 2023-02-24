import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    print(filepath)
    pdf = FPDF(orientation="P", unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=16)
    pdf.set_text_color(100,100,100)
    filename = Path(filepath).stem
    inv_no, date = filename.split('-')
    pdf.cell(w=50, h=8, txt=f'Invoice nr.{inv_no}',ln = 1, align ='L')
    pdf.cell(w=50, h=8, txt=f'Date {date}',ln = 2, align ='L')
    
    pdf.output(f"PDFs/Invoice-{filename}.pdf")