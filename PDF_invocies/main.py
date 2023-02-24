import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob('invoices/*.xlsx')

for filepath in filepaths:    
    pdf = FPDF(orientation="P", unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=16)
    pdf.set_text_color(100,100,100)
    
    filename = Path(filepath).stem
    inv_no, date = filename.split('-')
    
    pdf.cell(w=50, h=8, txt=f'Invoice nr.{inv_no}',ln = 1, align ='L')
    pdf.cell(w=50, h=8, txt=f'Date {date}',ln = 1, align ='L')
    pdf.ln(4)
    
    #Add header
    pdf.set_font(family='Times', style='B', size=10)
    pdf.set_text_color(50,50,50)
    pdf.cell(w=30, h=8, txt='Product Id', border=True)
    pdf.cell(w=50, h=8, txt='Product Name', border=True)
    pdf.cell(w=40, h=8, txt='Amount Purchased', border=True)
    pdf.cell(w=30, h=8, txt='Price per unit', border=True)
    pdf.cell(w=30, h=8, txt='Total price', border=True,ln=1)
    
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    for index, row in df.iterrows():
        pdf.set_font(family='Times', size=10)
        pdf.set_text_color(80,80,80)
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=True)
        pdf.cell(w=50, h=8, txt=str(row['product_name']), border=True)
        pdf.cell(w=40, h=8, txt=str(row['amount_purchased']), border=True)
        pdf.cell(w=30, h=8, txt=str(row['price_per_unit']), border=True)
        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=True,ln=1)
    
    total_sum = df['total_price'].sum()
    pdf.set_font(family='Times', size=10)
    pdf.set_text_color(50,50,50)
    pdf.cell(w=30, h=8, txt='', border=True)
    pdf.cell(w=50, h=8, txt='', border=True)
    pdf.cell(w=40, h=8, txt='', border=True)
    pdf.cell(w=30, h=8, txt='', border=True)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=True,ln=1)
    pdf.ln(2)
    pdf.set_font(family='Times',style='B', size=15)
    pdf.cell(w=30, h=8, txt=f'The total price is {total_sum} rupees')

    pdf.output(f"PDFs/Invoice-{filename}.pdf")