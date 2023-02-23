import pandas 
from fpdf import FPDF
import os

pdf = FPDF(orientation='P',unit='mm',format='A4')
pdf.set_auto_page_break(auto=False, margin=0)


df = pandas.read_csv("data.csv")



for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style= 'B', size= 24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row['Topic'],align='L',ln=1)
    #underlined pages
    for y in range(20,298,10):
        pdf.line(10,y,200,y)
        
    
    
    
    pdf.ln(265)
    
    pdf.set_font(family='Times', style= 'I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0,h=8,txt= row['Topic'],align='R')
    
    for i in range(1,row['Pages']):
        pdf.add_page()
        pdf.ln(265)
    
        pdf.set_font(family='Times', style= 'I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0,h=8,txt= row['Topic'],align='R')
        
        for y in range(20,298,10):
            pdf.line(10,y,200,y)
        
pdf.output("output.pdf")
