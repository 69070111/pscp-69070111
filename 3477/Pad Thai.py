"""Pad Thai"""
def padthai():
    """Pad Thai"""
    required = {
        "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp", "Bean Sprouts",
        "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts"
    }
    required_tastes = {"Sweet", "Sour", "Salty"}

    ingredients = set()
    extra = False
    while True:
        line = input().strip()
        if line == "Cook":
            break
        ingredients.add(line)
        if line not in required:
            extra = True

    tastes = set()
    while True:
        line = input().strip()
        if line == "End":
            break
        tastes.add(line)

    if extra:
        print("This is not Pad Thai!!!")
    elif ingredients != required:
        print("This is bad!")
    elif tastes != required_tastes:
        print("Not Bad...")
    else:
        print("Delicious!")
padthai()
