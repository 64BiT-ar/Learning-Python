# Api key = cd0db4feccd19c34e084812974bf7cde5082cf374360abaec6e344e849cac38b
# https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey

import requests
import sys
import json

if len(sys.argv) <= 1:
    print("Missing command-line argument")
    sys.exit()
elif len(sys.argv) == 2:
    try:
        qty = float(sys.argv[1])

        api = "cd0db4feccd19c34e084812974bf7cde5082cf374360abaec6e344e849cac38b"
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" + api)
        obj = response.json()
        btc_price = obj["data"]["priceUsd"]

        price = float(btc_price) * qty
        print(f"${price:,.4f}")

    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        sys.exit("Request failed")
