# Real-Time Currency Converter

A simple and efficient Python program to perform real-time currency conversion. This program fetches the latest exchange rates from an external API and allows users to convert an amount from one currency to another.

## How to Use

1. Ensure you have Python installed on your system.

2. Clone or download the script to your local machine.

3. Install the required library:

```
pip install requests
```

4. Run the program in a terminal or command prompt:

```
python app.py
```

5. The program will prompt you to enter the base currency, target currency, and the amount to be converted.

6. The converted amount will be displayed, or an error message will appear if an invalid currency code is provided or an API error occurs.

## Functionality

- `get_exchange_rate(base_currency, target_currency)`: Fetches the exchange rate for the target currency against the base currency from the "ExchangeRate-API."

- `convert_currency(amount, exchange_rate)`: Performs the currency conversion based on the amount and exchange rate.

- The user is prompted to enter the base and target currencies as well as the amount to be converted.

- The program validates the provided currency codes and performs the currency conversion.

## Note

- The program uses the "ExchangeRate-API" to fetch the latest exchange rates. Make sure you have an internet connection while running the program.

- The API may have rate limits or usage restrictions for free versions.

- This is a basic currency converter and does not provide additional features like historical data or advanced currency analytics.

# Author
**Ahnaf Tahmid Zaman**

<a href="https://www.linkedin.com/in/ahnaf-tahmid-zaman/">
    <img src="https://dl.dropboxusercontent.com/scl/fi/6wwu1stsm3hki3vsxl5c0/linkedin.png?rlkey=4nfdo2u3tmoaxo9xwkxh6t5to&dl=0" alt="Linkedin" width="67px">
</a>
<a href="https://github.com/AHNAF14924">
    <img src="https://dl.dropboxusercontent.com/scl/fi/bys8mwgtmsjobu6uk0d15/GitHub-Symbol-2149346605.png?rlkey=memfqto1ygr91gja8t3cpwwbx&dl=0" alt="GitHub" width="100px">
</a>