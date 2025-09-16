import requests

# API URL (CoinGecko)
url = "https://api.coingecko.com/api/v3/simple/price"

# Ask user which crypto they want
crypto = input("Enter the cryptocurrency (e.g., bitcoin, ethereum, dogecoin): ").lower()

# Params for API
parameters = {
    "ids": crypto,
    "vs_currencies": "usd",
    "include_market_cap": "true",
    "include_24hr_change": "true"
}

# Get Data
response = requests.get(url, params=parameters)

if response.status_code == 200:
    data = response.json()

    if crypto in data:
        price = data[crypto]["usd"]
        market_cap = data[crypto]["usd_market_cap"]
        change_24h = data[crypto]["usd_24h_change"]

        print(f"\n💰 {crypto.capitalize()} Price: ${price:,.2f}")
        print(f"📊 Market Cap: ${market_cap:,.0f}")
        print(f"📉 24h Change: {change_24h:.2f}%\n")
    else:
        print("⚠️ Cryptocurrency not found! Try another one.")
else:
    print("❌ Failed to fetch data. Please try again later.")
