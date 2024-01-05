from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

done = False
while not done:
    order = input(f"Please choose a coffee. {menu.get_items()}: ")

    while order == "report":
        coffee_maker.report()
        order = input(f"Please choose a coffee. {menu.get_items()}")

    if order == "off":
        done = True
        break

    menu_item = menu.find_drink(order)

    if not menu_item is None:
        if coffee_maker.is_resource_sufficient(menu_item):
            if money_machine.make_payment(menu_item.cost):
                coffee_maker.make_coffee(menu_item)
            else:
                print("Sorry, you don't have enough money.")
        else:
            print("Sorry, the machine has insufficient resources.")
    else:
        print("Sorry, this is not a drink we offer.")
