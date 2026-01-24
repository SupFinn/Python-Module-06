
def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    validation_result: str = validate_ingredients(ingredients)
    if validation_result == ingredients + " - VALID":
        return f"Spell recorded: {spell_name} ({validation_result})"
    elif validation_result == ingredients + " - INVALID":
        return f"Spell rejected: {spell_name} ({validation_result})"
    return ""
