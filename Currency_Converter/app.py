import requests

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'].get(target_currency)

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def main():
    base_currency = input("Enter the base currency: ").upper()
    target_currency = input("Enter the target currency: ").upper()
    amount = float(input("Enter the amount to convert: "))

    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate is None:
        print("Invalid currency code or API error. Please try again later.")
    else:
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"{amount:.2f} {base_currency} is equivalent to {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
    main()
