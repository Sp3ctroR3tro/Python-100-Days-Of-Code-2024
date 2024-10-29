from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creating objects from the give classes
Brewmaster3000 = CoffeeMaker()
Register = MoneyMachine()
menu = Menu()

turned_on = True
while turned_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        turned_on = False
    elif choice == "report":
        Brewmaster3000.report()
        Register.report()
    else:
        drink = menu.find_drink(choice)
        resource_on_hand = Brewmaster3000.is_resource_sufficient(drink)
        if resource_on_hand:
            payment_accepted = Register.make_payment(drink.cost)
            if payment_accepted:
                Brewmaster3000.make_coffee(drink)