from .Inventory import Inventory
from .RecipeBook import RecipeBook


class CoffeeMaker:
    def __init__(self):
        self.recipeBook = RecipeBook()
        self.inventory = Inventory()

    def addRecipe(self, r):
        return self.recipeBook.addRecipe(r)

    def deleteRecipe(self, recipeToDelete):
        return self.recipeBook.deleteRecipe(recipeToDelete)

    def editRecipe(self, recipeToEdit, r):
        return self.recipeBook.editRecipe(recipeToEdit, r)

    def addInventory(self, amtCoffee, amtMilk, amtSugar, amtChocolate):
        self.inventory.addCoffee(amtCoffee)
        self.inventory.addMilk(amtMilk)
        self.inventory.addSugar(amtSugar)
        self.inventory.addChocolate(amtChocolate)

    def checkInventory(self):
        return str(self.inventory)

    def makeCoffee(self, recipeToPurchase, amtPaid):
        change = 0

        recipes = self.getRecipes()
        if (
            recipeToPurchase < 0
            or recipeToPurchase >= len(recipes)
            or recipes[recipeToPurchase] is None
        ):
            change = amtPaid
        elif recipes[recipeToPurchase].getPrice() <= amtPaid:
            if self.inventory.useIngredients(recipes[recipeToPurchase]):
                change = amtPaid - recipes[recipeToPurchase].getPrice()
            else:
                change = amtPaid
        else:
            change = amtPaid

        return change

    def getRecipes(self):
        return self.recipeBook.getRecipes()
