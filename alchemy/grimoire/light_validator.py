def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    in_hand = ingredients.lower().replace(",", " ").split()
    found = set(in_hand).intersection(light_spell_allowed_ingredients())
    if found:
        return f"({list(found)} -VALID)"
    return f"({ingredients} -INVALID)"
