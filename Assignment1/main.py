### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}



### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if self.machine_resources[item] < ingredients[item]:
                print("Sorry, ingredients are insufficient.")
                return False
            return True


    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Insert Coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickles = int(input("How many nickles?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        total = quarters + dimes + nickles + pennies
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(cost - coins , 2)
            print(f"Transaction result is accepted. Your total is: {change}")
            return True
        else:
            print("Transaction result is insufficient.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount
            print(f"Here is the ingredient: {ingredient}")

### Make an instance of SandwichMachine class and write the rest of the codes ###
def main():
    sandwich_machine = SandwichMachine(recipes)
    while True:
            choice = input("What sandwich would you like to make? (small/medium/large) or 'off' to exit: ")
            if choice == "off":
                print("Thank you for shopping with us!")
                break
            elif choice in recipes:
                sandwich = recipes[choice]
                if sandwich_machine.check_resources(sandwich["ingredients"]):
                    print(f"The cost is ${sandwich['cost']}")
                    money_inserted =  sandwich_machine.process_coins()
                    if sandwich_machine.transaction_result(money_inserted, sandwich['cost']):
                        sandwich_machine.make_sandwich(choice, sandwich["ingredients"])
                    else:
                        print("Invalid selection")
main()



