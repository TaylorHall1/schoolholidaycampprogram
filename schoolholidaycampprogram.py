camps = [
    {"name": "Cultural Immersion", "days": 5, "cost": 800},
    {"name": "Kayaking and Pancakes", "days": 3, "cost": 400},
    {"name": "Mountain Biking", "days": 4, "cost": 900},
]

meal_options = ["standard", "vegetarian", "vegan"]
shuttle_cost = 80

def get_name():
    while True:
        name = input("enter camper name: ").strip()

        if name == "":
            print("name cannot be blank.")
        elif not name.replace(" ", "").isalpha():
            print("name must contain letters only.")
        else:
            return name.title()
        
def get_age():
    while True:
        age = input("enter camper age: ").strip()

        if age == "":
            print("age cammpt be blank")
        elif not age.replace(" ", "").isdigit():
            print("age must contain numbers only.")
        else:
            return int(age)

def get_camp():
    while True:
        print("available Camps:")

        for number, camp in enumerate(camps, start=1):
            print(f"{number}. {camp['name']} ({camp['days']} days) - ${camp['cost']}")

        choice = input("choose a camp number: ").strip()

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(camps):
                return choice - 1

        print("please enter a valid camp number.")

def get_shuttle():
    while True:
        shuttle = input("do you need the shuttle? (yes/no): ").strip()

        if shuttle in ["yes"]:
            return True
        elif shuttle in ["no"]:
            return False
        else:
            print("please enter yes or no.")

def get_meal():
    print("Meal Options:")
    print("1. standard")
    print("2. vegetarian")
    print("3. vegan")

    while True:
        choice = input("Choose a meal option (1-3): ")

        if choice in ["1", "2", "3"]:
            return meal_options[int(choice) - 1]

        print("Invalid choice. Please enter 1, 2, or 3.")

def attendence_confirm():
    while True:
        confirm = input ("would you like to confirm the attendence? (yes/no):")

        if confirm == "yes":
            return True
        elif confirm == "no":
            return False
        
        print ("enter yes or no")

campers = []

while True:
    print("Welcome to the camp holiday program")

    name = get_name()
    age = get_age()
    camp_choice = get_camp()
    shuttle = get_shuttle()
    meal = get_meal()

    selected_camp = camps[camp_choice]

    total_cost = selected_camp["cost"]
    if shuttle:
        total_cost += shuttle_cost
    
    print("\nregistratyion suumary")
    print(f"name : {name}")
    print(f"age : {age}")
    print(f"camp : {selected_camp['name']}")
    print(f"days spent : {selected_camp['days']}")
    print(f"food : {meal}")
    print(f"shuttle : {'yes' if shuttle else 'no'}")
    print(f"total price : ${total_cost}")

    if attendence_confirm():

        camper = {
            "name": name,
            "age": age,
            "camp": selected_camp["name"],
            "days": selected_camp["days"],
            "meal": meal,
            "shuttle": shuttle,
            "total_cost": total_cost
        }

        campers.append(camper)

        print("attendence confirmed and saved")
    else: print("attendence unfonfirmed and unsaved")
    again = input("\nRegister another camper? (yes/no): ").lower()

    if again == "no":
        break

with open("camp_registrations.txt", "w") as file:
    for camper in campers:
        file.write("Registration Summary\n")
        file.write(f"name: {camper['name']}\n")
        file.write(f"age: {camper['age']}\n")
        file.write(f"camp: {camper['camp']}\n")
        file.write(f"days: {camper['days']}\n")
        file.write(f"meal: {camper['meal']}\n")
        file.write(f"shuttle: {'Yes' if camper['shuttle'] else 'No'}\n")
        file.write(f"total cost: ${camper['total_cost']}\n")
        file.write(f"\n")
        
print(f"\n{len(campers)} confirmed registrations saved to camp_registrations.txt")