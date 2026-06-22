camps = {
    1: {"name": "Cultural Immersion", "days": 5, "Cost": 800},
    2: {"name": "Kayaking and Pancakes", "days": 3, "Cost": 400},
    3: {"name": "Mountain Biking", "days": 4, "Cost": 900},
}

for number, camp in camps.items():
    print(f"{number}. {camp['name']} - costs ${camp['Cost']}")

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
        
def get_age():
    while True:
        age = input("Enter camper age: ").strip()

        if age == "":
            print("Age cammpt be blank")
        elif not age.replace(" ", "").isdigit():
            print("Age must contain numbers only.")
        else:
            return int(age)

def get_camp():
    while True:
        print("\nAvailable Camps:")
        
        for key, camp in camps.items():
            print(f"{key}. {camp['name']} ({camp['days']} days) - ${camp['Cost']}")

        choice = input("Choose a camp number: ").strip()

        if choice.isdigit():
            choice = int(choice)

            if choice in camps:
                return choice

        print("Please enter a valid camp number.")

def get_shuttle():
    while True:
        shuttle = input("Do you need the shuttle? (yes/no): ").strip().lower()

        if shuttle in ["yes", "y"]:
            return True
        elif shuttle in ["no", "n"]:
            return False
        else:
            print("Please enter yes or no.")

def get_meal():