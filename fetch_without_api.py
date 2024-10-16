# import requests


def get_allergens_from_server(api_url):
    try:
        # response = requests.get(api_url)

        # response.raise_for_status()

        # allergens = response.json()

        allergens = ["shellfish"]
        return allergens

    # except requests.exceptions.RequestException as e:
    #     print(f"Error receiving allergens {e}")
    #     return []

    except:
        return []


def cook(ingredients, allergens):
    allergens = get_allergens_from_server(allergens)

    ingredients = set(ingredients).difference(allergens)

    print("cooking with ingredients - ", ingredients)


ingredients = ["wheat", "rice", "shellfish"]

allergens_api_url = "https://example.com/allergens"

cook(ingredients, allergens_api_url)
