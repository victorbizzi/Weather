import requests
import random


def get_random_capital_city():
    # REST Countries API endpoint for all countries
    url = "https://restcountries.com/v3.1/all"

    # Make the API request
    response = requests.get(url)

    # Check if the request was successful
    if response.ok:
        countries = response.json()

        # Select a random country from the list
        random_country = random.choice(countries)

        # Extract the capital city (if it exists)
        capital = random_country.get('capital', ['No capital found'])[0]
        return capital
    else:
        return "Failed to fetch country data."


# Fetch a random capital city name
capital_city = get_random_capital_city()
print(f"Random capital city: {capital_city}")
