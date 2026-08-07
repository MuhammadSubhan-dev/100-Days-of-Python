import art
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

profit = 0      #Variable for storing money in the machine

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True if the ingredients are sufficient for particular coffee."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25    #Each quarter is 0.25 of a dollar
    total += int(input("How many dimes? ")) * 0.1  # Each dime is 0.25 of a dollar
    total += int(input("How many nickels? ")) * 0.05  # Each nickel is 0.25 of a dollar
    total += int(input("How many pennies? ")) * 0.01  # Each penny is 0.25 of a dollar
    return total

def is_transaction_successful(money_recieved, drink_cost):
    """Returns True if the payment is successful."""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost,2)
        print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

def print_menu():
    print(f"Espresso: ${MENU['espresso']['cost']}")
    print(f"Latte: ${MENU['latte']['cost']}")
    print(f"Cappuccino: ${MENU['cappuccino']['cost']}")

is_operational = True
while is_operational:   #Keep being operational until turned off
    print(art.logo)
    print_menu()
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == "off":    #Secret string for switching off the machine
        is_operational = False
        print(art.off)
    elif coffee_type == "report":       #String for checking the available resources in machine
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        if coffee_type == "espresso":
            print(art.espresso)
        elif coffee_type == "latte":
            print(art.latte)
        elif coffee_type == "cappuccino":
            print(art.cappuccino)
        drink = MENU[coffee_type]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(coffee_type, drink["ingredients"])      #If ingredients are available and payment is processed then make coffe