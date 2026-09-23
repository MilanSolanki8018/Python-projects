from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# mi = MenuItem()
m = Menu()
cm = CoffeeMaker()
mm = MoneyMachine()

is_one = True
while is_one:
    option = m.get_items()
    choice = str(input(f"What would you like? ({option})"))

    if choice == "off":
        print("Machine Close.")
        is_one = False
    elif choice == "report":
        cm.report()
        mm.report()
    else:
        drink = m.find_drink(choice)
        if cm.is_resource_sufficient(drink):
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)

