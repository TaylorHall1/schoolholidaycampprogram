camps = {
    1: {"name": "Cultural Immersion", "days": 5, "Cost": 800},
    2: {"name": "Kayaking and Pancakes", "days": 3, "Cost": 400},
    3: {"name": "Mountain Biking", "days": 4, "Cost": 900},
}

meal_options = ["standard", "vegetarian", "vegan"]
SHUTTLE_COST = 80


def get_name():
    while True:
        name = input("Enter camper name: ").strip()

        if name == "":
            print("Name cannot be blank.")
        elif not name.replace(" ", "").isalpha():
            print("Name must contain letters only.")
        else:
            return name.title()
