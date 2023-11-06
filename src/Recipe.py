from .exceptions.RecipeException import RecipeException


class Recipe:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.amtCoffee = 0
        self.amtMilk = 0
        self.amtSugar = 0
        self.amtChocolate = 0

    def getAmtChocolate(self):
        return self.amtChocolate

    def setAmtChocolate(self, chocolate):
        try:
            amtChocolate = int(chocolate)
        except ValueError:
            raise RecipeException("Units of chocolate must be a positive integer")

        if amtChocolate >= 0:
            self.amtChocolate = amtChocolate
        else:
            raise RecipeException("Units of chocolate must be a positive integer")

    def getAmtCoffee(self):
        return self.amtCoffee

    def setAmtCoffee(self, coffee):
        try:
            amtCoffee = int(coffee)
        except ValueError:
            raise RecipeException("Units of coffee must be a positive integer")

        if amtCoffee >= 0:
            self.amtCoffee = amtCoffee
        else:
            raise RecipeException("Units of coffee must be a positive integer")

    def getAmtMilk(self):
        return self.amtMilk

    def setAmtMilk(self, milk):
        try:
            amtMilk = int(milk)
        except ValueError:
            raise RecipeException("Units of milk must be a positive integer")

        if amtMilk >= 0:
            self.amtMilk = amtMilk
        else:
            raise RecipeException("Units of milk must be a positive integer")

    def getAmtSugar(self):
        return self.amtSugar

    def setAmtSugar(self, sugar):
        try:
            amtSugar = int(sugar)
        except ValueError:
            raise RecipeException("Units of sugar must be a positive integer")

        if amtSugar >= 0:
            self.amtSugar = amtSugar
        else:
            raise RecipeException("Units of sugar must be a positive integer")

    def getName(self):
        return self.name

    def setName(self, name):
        if name is not None:
            self.name = name

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        try:
            amtPrice = int(price)
        except ValueError:
            raise RecipeException("Price must be a positive integer")

        if amtPrice >= 0:
            self.price = amtPrice
        else:
            raise RecipeException("Price must be a positive integer")

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if self is other:
            return True
        if other is None:
            return False
        if not isinstance(other, Recipe):
            return False
        return self.name == other.name
