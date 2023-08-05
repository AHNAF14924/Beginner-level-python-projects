# Introduction
The Product Purchase Management System is a Python program that allows users to browse through a list of products categorized in different sheets of an Excel file, add selected products to their cart, specify quantities, and finally generate an invoice upon checkout.

## Prerequisites
1. Python 3.x installed.
2. Required libraries: `openpyxl`, `tabulate`. You can install these libraries using the following commands:
```
pip install openpyxl
pip install tabulate
```
## Usage
1.**Program Execution**: Run the program by executing the Python script.
```
python app.py
```
2.**Main Menu**: The program will display the main menu with a list of available product categories.

3.**Product Selection**:

Select a product category by entering the corresponding number.
View the list of products in the selected category.
Enter the number of the desired product to add it to the cart.
Specify the quantity for the selected product.

4.**Cart Management**:

The selected products and their quantities will be added to the cart.
The total price for each selected product will be displayed.

6.**Checkout**:

To proceed to checkout, select the option to "Checkout" from the main menu.
An invoice will be displayed with the product names, quantities, unit prices, and total prices.
The grand total of the purchase will be calculated and shown.

## Exiting the Program:
After checkout, the program will display a thank you message and exit.

## Program Structure
The program consists of the following components:

1.**Loading Excel File**: The program loads an Excel file named `products_list.xlsx`.

2.**Loading Sheet Options**: The program loads available sheet names as product categories.

3.**Display Product Options**: Displays a menu with available product categories for user selection.

4.**Process Product Choice**: Processes the user's choice by displaying products, capturing user selections, and calculating prices.

5.**Checkout**: Generates an invoice based on the user's selections and calculates the grand total.

6.**Main Function (main)**: The main loop of the program where user interactions take place.