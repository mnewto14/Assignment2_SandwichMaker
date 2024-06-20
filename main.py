
import data
import sandwich_maker
import cashier
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()
def main():
    is_on = True

    while is_on:
        choice = input("Choose Sandwich (ham_cheese_sandwich/report/off): ").lower()

if choice == "report":
    print(f"Bread: {resources['bread']}")
    print(f"Cheese: {resources['cheese']}")
    print(f"Ham: {resources['ham']}")
else:
    print("Sorry, this sandwich is not available.")

if __name__=="__main__":
    main()
