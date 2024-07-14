MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

WORK = True
earning = 0


def check_resources(type):
    drink = MENU[type]['ingredients']
    for key in drink:
        if MENU[type]['ingredients'][key] > resources[key]:
            return False
        else:
            return True


def coffee_make():
    type = input("What kind of coffee do you want? espresso/latte/cappuccino: ")
    global earning

    if type == 'report':
        for key in resources:

            if key == 'water' or key == 'milk':
                print(f"{key}: {resources[key]}ml")
            elif key == 'coffee':
                print(f"{key}: {resources[key]}g")
        print(f'Money: {earning}$')
    elif type == 'off':
        global WORK
        WORK = False
    else:
        drink = MENU[type]['ingredients']
        if not check_resources(type):
            print(f'Sorry, not enough ingredients to make {type}')

        else:

            print("Please insert coins.")

            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            total_input = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
            value = MENU[type]['cost']
            change = round(total_input - value, 2)

            earning += round(total_input - change,2)


            if change < 0:
                print("Sorry, that's not enough money. Money returned.")
                earning +=0
            else:
                for key in drink:
                        resources[key] -= drink[key]
                        if key == 'coffee':
                            print(f"Here is your {change}$ change.")
                            print(f"Here is your {type}. Enjoy!")


while WORK:
    coffee_make()


