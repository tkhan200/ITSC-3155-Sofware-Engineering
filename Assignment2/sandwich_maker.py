
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for items,amount in ingredients.items():
            if self.machine_resources.get(items, 0) < amount:
                print("Not enough ingredients to make a sandwich")
                return False
        return True



    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount
            print(f"Here is the ingredient: {ingredient}")