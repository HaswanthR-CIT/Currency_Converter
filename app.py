from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Expanded list of currencies
CURRENCIES = [
    "USD", "EUR", "JPY", "GBP", "INR", "AUD", "CAD", "CHF", "CNY", "SEK",
    "NZD", "MXN", "SGD", "HKD", "NOK", "KRW", "TRY", "RUB", "BRL", "ZAR",
    "DKK", "PLN", "THB", "IDR", "HUF", "CZK", "ILS", "CLP", "PHP", "AED"
]

# API setup (replace with your key from currencyapi.com)
API_KEY = "cur_live_WS1yUBEMR4IBycYL9zl4kFwM9jkZukOQ9xYe8Wmj"
API_URL = "https://api.currencyapi.com/v3/latest"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]

        # Fetch exchange rate
        response = requests.get(
            API_URL,
            params={"apikey": API_KEY, "base_currency": from_currency}
        )
        data = response.json()
        rate = data["data"][to_currency]["value"]
        converted_amount = amount * rate
        result = f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"

    return render_template("index.html", currencies=CURRENCIES, result=result)

if __name__ == "__main__":
    app.run(debug=True)