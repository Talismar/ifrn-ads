from .exceptions.InventoryException import InventoryException


class Inventory:
    coffee = 0
    milk = 0
    sugar = 0
    chocolate = 0

    # def __init__(self):
    #     Inventory.setCoffee(15)
    #     Inventory.setMilk(15)
    #     Inventory.setSugar(15)
    #     Inventory.setChocolate(15)

    @staticmethod
    def getChocolate():
        return Inventory.chocolate

    @staticmethod
    def setChocolate(chocolate):
        if chocolate >= 0:
            Inventory.chocolate = chocolate

    @staticmethod
    def addChocolate(chocolate):
        try:
            amtChocolate = int(chocolate)
        except ValueError:
            raise InventoryException("Units of chocolate must be a positive integer")

        if amtChocolate >= 0:
            Inventory.chocolate += amtChocolate
        else:
            raise InventoryException("Units of chocolate must be a positive integer")

    @staticmethod
    def getCoffee():
        return Inventory.coffee

    @staticmethod
    def setCoffee(coffee):
        if coffee >= 0:
            Inventory.coffee = coffee

    @staticmethod
    def addCoffee(coffee):
        try:
            amtCoffee = int(coffee)
        except ValueError:
            raise InventoryException("Units of coffee must be a positive integer")

        if amtCoffee >= 0:
            Inventory.coffee += amtCoffee
        else:
            raise InventoryException("Units of coffee must be a positive integer")

    @staticmethod
    def getMilk():
        return Inventory.milk

    @staticmethod
    def setMilk(milk):
        if milk >= 0:
            Inventory.milk = milk

    @staticmethod
    def addMilk(milk):
        try:
            amtMilk = int(milk)
        except ValueError:
            raise InventoryException("Units of milk must be a positive integer")

        if amtMilk >= 0:
            Inventory.milk += amtMilk
        else:
            raise InventoryException("Units of milk must be a positive integer")

    @staticmethod
    def getSugar():
        return Inventory.sugar

    @staticmethod
    def setSugar(sugar):
        if sugar >= 0:
            Inventory.sugar = sugar

    @staticmethod
    def addSugar(sugar):
        try:
            amtSugar = int(sugar)
        except ValueError:
            raise InventoryException("Units of sugar must be a positive integer")

        if amtSugar >= 0:
            Inventory.sugar += amtSugar
        else:
            raise InventoryException("Units of sugar must be a positive integer")

    def enoughIngredients(self, r):
        isEnough = True
        if Inventory.getCoffee() < r.getAmtCoffee():
            isEnough = False
        if Inventory.getMilk() < r.getAmtMilk():
            isEnough = False
        if Inventory.getSugar() < r.getAmtSugar():
            isEnough = False
        if Inventory.getChocolate() < r.getAmtChocolate():
            isEnough = False
        return isEnough

    def useIngredients(self, r):
        if self.enoughIngredients(r):
            Inventory.coffee -= r.getAmtCoffee()
            Inventory.milk -= r.getAmtMilk()
            Inventory.sugar -= r.getAmtSugar()
            Inventory.chocolate -= r.getAmtChocolate()
            return True
        else:
            return False

    def __str__(self):
        return f"Coffee: {Inventory.getCoffee()}\nMilk: {Inventory.getMilk()}\nSugar: {Inventory.getSugar()}\nChocolate: {Inventory.getChocolate()}\n"
