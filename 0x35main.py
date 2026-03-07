from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def create_sales_receipt(filename="sales_receipt.pdf"):
    doc = SimpleDocTemplate(filename,
        pagesize=letter,
        rightMargin=0.5*inch,
        leftMargin=0.5*inch,
        topMargin=0.5*inch,
        bottomMargin=0.5*inch
    )
    
    elements = []
    styles = getSampleStyleSheet()
    title_style = styles['Heading1']
    title_style.alignment = 1
    normal_style = styles['Normal']
    
    elements.append(Paragraph("SALES RECEIPT", title_style))
    elements.append(Spacer(1, 0.25*inch))
    
    # Add Date
    date_data = [["Date: ", ""]]
    date_table = Table(date_data, colWidths=[6.2*inch])
    date_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
    ]))
    elements.append(date_table)
    elements.append(Spacer(1, 0.25*inch))
    
    # Receipt table
    table_data = [["Qty.", "Description", "Price", "Amount"]]
    for i in range(10):
        table_data.append(["", "", "", ""])
    
    receipt_table = Table(table_data, colWidths=[0.5*inch, 3.5*inch, 1*inch, 1*inch])
    
    # Table Style
    receipt_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('ALIGN', (0, 1), (0, -1), 'CENTER'),
        ('ALIGN', (2, 1), (3, -1), 'RIGHT'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BACKGROUND', (0, 0), (-1, 0), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ]))
    
    elements.append(receipt_table)
    elements.append(Spacer(1, 0.25*inch))
    
    # Totals Section
    totals_data = [
        ["", "Subtotal:", ""],
        ["", "Tax:", ""],
        ["", "Total:", ""]
    ]
    
    totals_table = Table(totals_data, colWidths=[4*inch, 1*inch, 1*inch])
    totals_table.setStyle(TableStyle([
        ('ALIGN', (1,0), (1,-1), 'RIGHT'),
        ('GRID', (2,0), (2,-1), 0.5, colors.black),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('FONTNAME', (1,2), (1,2), 'Helvetica-Bold'),
    ]))
    
    elements.append(totals_table)
    elements.append(Spacer(1, 0.25*inch))
    
    # Payment Method
    elements.append(Paragraph("Sale Made with:", normal_style))
    elements.append(Spacer(1, 0.1*inch))
    
    payment_data = [
        ["Cash"],
        ["Credit Card"],
        ["Check, No. _____"],
        ["Other _____"]
    ]
    
    payment_table = Table(payment_data, colWidths=[7.5*inch])
    payment_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('FONTSIZE', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (0,-1), 0.1*inch),
    ]))
    
    elements.append(payment_table)
    
    # Build Document
    doc.build(elements)
    print(f"Receipt created successfully: {filename}")

if __name__ == "__main__":
    create_sales_receipt()