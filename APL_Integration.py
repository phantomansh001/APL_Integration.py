# APL Integration: Fetch and display cryptocurrency prices from an API
import requests

def fetch_crypto_price(symbol="bitcoin"):
	url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
	try:
		response = requests.get(url)
		response.raise_for_status()
		data = response.json()
		if symbol in data and 'usd' in data[symbol]:
			price = data[symbol]['usd']
			print(f"Current price of {symbol.capitalize()}: ${price}")
		else:
			print("Invalid response format or symbol not found.")
	except requests.RequestException as e:
		print(f"Error fetching data: {e}")
	except ValueError:
		print("Error: Could not parse JSON response.")

if __name__ == "__main__":
	symbol = input("Enter cryptocurrency symbol (e.g., bitcoin, ethereum): ").lower()
	fetch_crypto_price(symbol)
