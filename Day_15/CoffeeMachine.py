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

cash = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order):
    for item in order["ingredients"]:
        if order["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = 0
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def transaction(money_inserted, order):
    if money_inserted >= order["cost"]:
        change = round(money_inserted - order["cost"],2)
        print(f"Here is your change of ${change:.2f}")
        global cash
        cash += order["cost"]
        return True
    else:
        print("Insufficient funds")
        return False

def make_order(order_name):
    order = MENU[order_name]
    if not check_resources(order):
        return

    money_inserted = process_coins()
    if transaction(money_inserted, order):
        print(f"Here is your {order_name}. Enjoy!")
        for item in order["ingredients"]:
            resources[item] -= order["ingredients"][item]
    else:
        print("Sorry, that's not enough money. Money refunded.")

def main():
    is_on = True
    while is_on is True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${cash}")
        elif choice in MENU:
            make_order(choice)
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
