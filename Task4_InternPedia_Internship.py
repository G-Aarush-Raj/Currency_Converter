import requests

def fetch():
    try:
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        response.raise_for_status()
        return response.json()['rates']
    except requests.exceptions.RequestException as e:
        print("Error fetching exchange rates: ",e)
        return None

def convert(amount, source, target, exchange):
    if source not in exchange or target not in exchange:
        print("Invalid currency.")
        return None
    return amount*exchange[target]/exchange[source]

def display(amount, source, target, converted):
    print(amount," of ",source," converted to ",target," equals ","{:.2f}".format(converted))

exchange = fetch()
while True:
    try:
        source=input("Enter source currency: ").upper()
        target=input("Enter target currency: ").upper()
        amount=float(input("Enter amount to convert: "))
        converted=convert(amount,source,target,exchange)
        if converted is not None:
            display(amount,source,target,converted)
    except ValueError:
        print("Invalid input. Please enter a valid number")
    next=input("Do you want to convert another currency? (yes/no): ").lower()
    if next!='yes':
        break