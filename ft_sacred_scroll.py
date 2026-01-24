import alchemy


def main() -> None:
    print()
    print("=== Sacred Scroll Mastery ===")
    print()

    print("Testing direct module access:")

    fire_element: str = alchemy.elements.create_fire()
    print(f"alchemy.elements.create_fire(): {fire_element}")

    water_element: str = alchemy.elements.create_water()
    print(f"alchemy.elements.create_water(): {water_element}")

    earth_element: str = alchemy.elements.create_earth()
    print(f"alchemy.elements.create_earth(): {earth_element}")

    air_element: str = alchemy.elements.create_air()
    print(f"alchemy.elements.create_air(): {air_element}")

    print()
    print("Testing package-level access (controlled by __init__.py):")

    fire_element: str = alchemy.create_fire()
    print(f"alchemy.elements.create_fire(): {fire_element}")

    water_element: str = alchemy.create_water()
    print(f"alchemy.elements.create_water(): {water_element}")

    try:
        earth_element: str = alchemy.create_earth()
    except AttributeError:
        earth_element: str = "AttributeError - not exposed"
    print(f"alchemy.create_earth() {earth_element}")

    try:
        air_element: str = alchemy.create_air()
    except AttributeError:
        air_element: str = "AttributeError - not exposed"
    print(f"alchemy.create_air() {earth_element}")

    print()
    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
