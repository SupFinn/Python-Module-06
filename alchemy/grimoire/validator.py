
def validate_ingredients(ingredients: str) -> str:
    valid_ingredients: list = ["fire", "water", "earth", "air"]

    all_ingredients = ingredients.split()
    for element in all_ingredients:
        if element not in valid_ingredients:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
