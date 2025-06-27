from fpdf import FPDF
import os
from datetime import datetime

from app.config import GST_CONFIG, DISCOUNT_TYPE

class InvoicePDF:
    def __init__(self, client, item_list, quantities, prices, discount_type='none'):
        self.client = client
        self.item_list = item_list
        self.quantities = quantities
        self.prices = prices
        self.discount_type = discount_type.lower()
        self.filename = None
        self.filepath = None
        self.folder = "invoices"

    def generate_pdf(self):
        sub_total = 0 
        pdf = FPDF()
        pdf.add_page()

        watermark_path = os.path.join("static", "watermark.png")
        if os.path.exists(watermark_path):
            current_y = pdf.get_y()
            current_x = pdf.get_x()
            pdf.image(watermark_path, x=35, y=80, w=140)
            pdf.set_y(current_y)
            pdf.set_x(current_x)
        #setting an auto page break 
        pdf.set_auto_page_break(auto=True, margin=15)
        date_form = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        #PDF Header
        #Logo 
        pdf.set_font('Arial','B',22)
        pdf.cell(0, 10 , "SwiftBill Solutions", ln=True, align='C')
        pdf.set_font('Arial','B',16)
        pdf.cell(0, 10 , "Invoice", ln=True, align='C')
        pdf.ln(10)

        #Client details
        pdf.set_font('Arial','B',16)
        pdf.cell(0, 10 , f"Client Name : {self.client}", ln=True, align='C')
        pdf.cell(0, 10 , f"Date : {date_form} ", ln=True, align='C')
        pdf.ln(5)
        #Table Header
        pdf.set_font('Arial','B',14)
        pdf.cell(70, 10 , f"Item", border=1, align='C')
        pdf.cell(30, 10 , f"Quantity", border=1, align='C')
        pdf.cell(30, 10 , f"Price", border=1, align='C')
        pdf.cell(40, 10 , f"Cost", border=1, align='C')
        pdf.ln()
        #Table Row Content
        for item in range(len(self.item_list)):
            item_name = self.item_list[item]
            qty = self.quantities[item]
            price = self.prices[item]
            item_total = int(qty) * int(price)
            sub_total += item_total

            pdf.cell(70, 10 , item_name , border=1)
            pdf.cell(30, 10 , str(qty) , border=1)
            pdf.cell(30, 10 , f"{price}" , border=1)
            pdf.cell(40, 10 , f"{item_total}" , border=1)
            pdf.ln()
        #Tax Calculation
        sgst = sub_total*GST_CONFIG["SGST"]
        cgst = sub_total*GST_CONFIG["CGST"]
        total_tax = cgst + sgst
        #Discounts Calculations
        #get the discount rate and calculate the discount
        discount_rate = DISCOUNT_TYPE.get(self.discount_type, 0)
        total_discount = sub_total*discount_rate
        #Total section
        # add the sub totals and Taxes and Discounts
        pdf.ln()

        grand_total = sub_total + total_tax - total_discount

        pdf.set_font('Arial','B',12)
        pdf.cell(130, 10 , f"Sub total", border=0)
        pdf.cell(40, 10 , f"{sub_total}", ln=True, border=0)
        pdf.cell(130, 10 , f"SGST @ 9%", border=0)
        pdf.cell(40, 10 , f"{sgst:.2f}", ln=True, border=0)
        pdf.cell(130, 10 , f"CGST @ 9%", border=0)
        pdf.cell(40, 10 , f"{cgst:.2f}", ln=True, border=0)
        pdf.cell(130, 10 , f"Discount({self.discount_type})", border=0)
        pdf.cell(40, 10 , f"{total_discount:.2f}", ln=True, border=0)
        pdf.cell(130, 10 , f"Final Amount", border=0)
        pdf.cell(40, 10 , f"{grand_total}", ln=True, border=0)

        #footer
        pdf.ln(10)
        pdf.set_font("Arial", "I", 10)
        pdf.multi_cell(0,10, "Thank you for your Purchase!! \n Swift Bill Solutions | support@swiftbillsoultions.co.in \n GSTIN000112HNG98HAS")

        #save the PDF
        os.makedirs(self.folder, exist_ok=True)
        self.filename = f"INV_{self.client}_{datetime.now().strftime('%Y%m%d%H%M%S')}.pdf"
        self.filepath = os.path.join(self.folder, self.filename)
        pdf.output(self.filepath)


        return self.filepath, grand_total, self.filename
        