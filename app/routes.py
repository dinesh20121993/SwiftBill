from flask import render_template, request, send_file, flash, abort
from fpdf import FPDF
import os
from datetime import datetime
from app.database import insert_invoice_details_DB, get_all_Invoices
from app.pdf_generator import InvoicePDF

INVOICE_FOLDER = "invoices"

def init_routes(app):

    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.route("/generate" , methods=["POST"])
    def generate_invoices():
        data = request.form

        #Get data from the form
        client_name = data.get('client')
        item_list = data.getlist('item[]')
        quantity = data.getlist('quantity[]')
        prices = data.getlist('price[]')

        discount_type = data.get("discount", "none")
        #Generate PDF
        pdf = InvoicePDF(client_name, item_list, quantity, prices, discount_type)
        save_file_path , total, save_file = pdf.generate_pdf()
        #insert into database
        insert_invoice_details_DB(client_name, total, save_file)

        #Generate a flash Message that Invoice was generated Succesfully
        flash('Invoice Generated Succesfully', 'success')
        return send_file(save_file_path, as_attachment=True , download_name = save_file)
    
    @app.route('/history')
    def get_invoice_History():
        invoice_data = get_all_Invoices()
        return render_template('history.html', invoices = invoice_data)




    
        
