import data
from sandwich_maker import SandwichMaker
from cashier import Cashier



# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    sandwich_machine = SandwichMaker(recipes)
    while True:
        choice = input("What sandwich would you like to make? (small/medium/large/report) or 'off' to exit: ")
        if choice == "off":
            print("Thank you for shopping with us!")
            break

        elif choice in recipes:
            sandwich = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                print(f"The cost is ${sandwich['cost']}")
                money_inserted =  cashier_instance.process_coins()
                if cashier_instance.transaction_result(money_inserted, sandwich['cost']):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])
                else:
                    print("Invalid selection")





if __name__=="__main__":
    main()