## Overview

This program is designed to provide a command-line interface for managing a product purchase system. It allows users to select products from an Excel spreadsheet, add them to a shopping cart, and generate an invoice in PDF format upon checkout. The program utilizes the openpyxl library to read Excel files, the tabulate library to display data in a tabular format, and the pdfkit library to generate PDF documents.

## Prerequisites

- Python 3.x installed
- Required Python libraries: `openpyxl`, `tabulate`, `pdfkit`
  Install them from the **requirements.txt** file:

```
pip install -r requirements.txt
```

## Usage

1. Ensure the Excel file named **products_list.xlsx** is present in the same directory as the program.
2. Run the program using the command:

```
app.py
```

## Program Flow

1. Loading Excel File

- The program starts by loading the Excel file `products_list.xlsx` using the `openpyxl` library.

2. Main Functionality

- Users are presented with a list of product categories (sheets in the Excel file).
- They can choose a product category or proceed to checkout.

3. Display Product Options

- The available product categories are displayed, along with their corresponding indices.

4. Process Product Choice

- When a product category is selected, the program displays the products within that category in a tabular format using the `tabulate` library.
- Users can choose a product by entering its number.
- The selected product's details (name, price, etc.) are displayed.
- Users enter the quantity they want to buy.

5. Checkout

- Users can choose to proceed to checkout.
- The program calculates the total price for each item in the shopping cart and generates an invoice in HTML format using `tabulate`.
- The HTML invoice is converted into a PDF using the `pdfkit` library and saved as `invoice.pdf` in the program's directory.
- The shopping cart is emptied.

6. Termination

- Users can exit the program after checkout.

## Notes

- Ensure that the Excel file `products_list.xlsx` is correctly formatted with product information and category sheets.
- The `tabulate` library is used for tabular data formatting in both the terminal and the invoice PDF.
- The `pdfkit` library requires an external tool called wkhtmltopdf to be installed for PDF generation to work. Make sure it is installed and accessible.You can install wkhtmltopdf on your system using the following command:

```
sudo apt-get install wkhtmltopdf
```
## Author
**Ahnaf Tahmid Zaman**

<a href="https://www.linkedin.com/in/ahnaf-tahmid-zaman/">
    <img src="https://dl.dropboxusercontent.com/scl/fi/6wwu1stsm3hki3vsxl5c0/linkedin.png?rlkey=4nfdo2u3tmoaxo9xwkxh6t5to&dl=0" alt="Linkedin" width="67px">
</a>
<a href="https://github.com/AHNAF14924">
    <img src="https://dl.dropboxusercontent.com/scl/fi/bys8mwgtmsjobu6uk0d15/GitHub-Symbol-2149346605.png?rlkey=memfqto1ygr91gja8t3cpwwbx&dl=0" alt="GitHub" width="100px">
</a>