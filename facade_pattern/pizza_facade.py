from facade_pattern.dough import Dough
from facade_pattern.sauce import Sauce
from facade_pattern.topping import Topping
from facade_pattern.cheese import Cheese
from facade_pattern.oven import Oven


class PizzaFacade:

    def __init__(self, sauce, topping, cheese):
        self.dough = Dough()
        self.sauce = Sauce(sauce)
        self.topping = Topping(topping)
        self.cheese = Cheese(cheese)
        self.oven = Oven()

    def make_pizza(self):
        self.dough.add_sauce(self.sauce)
        self.dough.add_cheese(self.cheese)
        self.dough.add_topping(self.topping)
        self.oven.set_temperature(450)
        self.oven.set_timer(25)
        self.oven.cook(self.dough)
