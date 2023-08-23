#Virtual Coffee Machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

def coffee_resources(coffee, money):
    if coffee.lower() == 'report':
        for key, item in resources.items():
            print(f"{key}: {item}")
        print(f"Money: ${money}")
    else:
        if MENU[coffee]['ingredients']['water'] <= resources['water']:
            if MENU[coffee]['ingredients']['coffee'] <= resources['coffee']:
                if MENU[coffee]['ingredients']['milk'] <= resources['milk']:
                    return True
        else:
            return False

def resources_used(coffee):
    resources['water'] -= MENU[coffee]['ingredients']['water']
    resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
    resources['milk'] -= MENU[coffee]['ingredients']['milk']

def money_check(price, coffee):
    if price < MENU[coffee]['cost']:
        return False

    return True


def coffee_machine(money = 0.0):
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee == 'off':
        return 0
    if coffee == "report":
        coffee_resources(coffee, money)
        coffee_machine(money)
    elif coffee_resources(coffee, money):
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        price = round(pennies * 0.01 + dimes * 0.1 + nickles * 0.05 + quarters * 0.25, 2)
        if not money_check(price, coffee):
            print("Sorry that's not enough money. Money refunded.")
            coffee_machine(money)
        money += MENU[coffee]['cost']
        resources_used(coffee)
        print(f"Here is ${round(price - MENU[coffee]['cost'], 2)} in change.")
        print(f"Here is your {coffee}. Enjoy!")
        coffee_machine(money)
    else:
        print(f"Not enough resources to make {coffee}\nPlease choose any other coffee or come back later")
        coffee_machine(money)


coffee_machine()
