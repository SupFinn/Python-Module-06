from . import elements

def healing_potion() -> str:
    fire_element: str = elements.create_fire()
    water_element: str = elements.create_water()
    return f"Healing potion brewed with {fire_element} and {water_element}"

def strength_potion() -> str:
    earth_element: str = elements.create_earth()
    fire_element: str = elements.create_fire()
    return f"Strength potion brewed with {earth_element} and {fire_element}"

def invisibility_potion() -> str:
    air_element: str = elements.create_air()
    water_element: str = elements.create_water()
    return f"Invisibility potion brewed with {air_element} and {water_element}"

def wisdom_potion() -> str:
    all_four_elements: str = ""
    all_four_elements += elements.create_fire()
    all_four_elements += elements.create_water()
    all_four_elements += elements.create_earth()
    all_four_elements += elements.create_air()

    return f"Wisdom potion brewed with all elements: {all_four_elements}"