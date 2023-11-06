from CoffeeMaker import CoffeeMaker
from exceptions.InventoryException import InventoryException
from exceptions.RecipeException import RecipeException
from Recipe import Recipe

coffeeMaker: CoffeeMaker


def inputOutput(message: str):
    print(message)

    try:
        return input()
    except Exception as e:
        print("Error reading in value")
        mainMenu()


def addRecipe():
    # Read in recipe name
    name = inputOutput("\nPlease enter the recipe name: ")

    # Read in recipe price
    priceString = inputOutput("\nPlease enter the recipe price: $")

    # Read in amt coffee
    coffeeString = inputOutput("\nPlease enter the units of coffee in the recipe: ")

    # Read in amt milk
    milkString = inputOutput("\nPlease enter the units of milk in the recipe: ")

    # Read in amt sugar
    sugarString = inputOutput("\nPlease enter the units of sugar in the recipe: ")

    # Read in amt chocolate
    chocolateString = inputOutput(
        "\nPlease enter the units of chocolate in the recipe: "
    )

    r = Recipe()
    try:
        r.setName(name)
        r.setPrice(priceString)
        r.setAmtCoffee(coffeeString)
        r.setAmtMilk(milkString)
        r.setAmtSugar(sugarString)
        r.setAmtChocolate(chocolateString)

        recipeAdded = coffeeMaker.addRecipe(r)

        if recipeAdded:
            print(name + " successfully added.\n")
        else:
            print(name + " could not be added.\n")

    except RecipeException as e:
        print(e)
    finally:
        mainMenu()


def recipeListSelection(message: str):
    userSelection = inputOutput(message)
    recipe = 0
    try:
        recipe = int(userSelection) - 1
        if recipe >= 0 and recipe <= 2:
            pass
        else:
            recipe = -1

    except Exception as e:
        print("Please select a number from 1-3.")
        recipe = -1

    return recipe


def deleteRecipe():
    recipes = coffeeMaker.getRecipes()
    for i in range(len(recipes)):
        if recipes[i] is not None:
            print(f"{i + 1} . {recipes[i].getName()}")

    recipeToDelete = recipeListSelection(
        "Please select the number of the recipe to delete."
    )

    if recipeToDelete < 0:
        mainMenu()

    recipeDeleted = coffeeMaker.deleteRecipe(recipeToDelete)

    if recipeDeleted is not None:
        print(recipeDeleted + " successfully deleted.\n")
    else:
        print("Selected recipe doesn't exist and could not be deleted.\n")

    mainMenu()


def editRecipe():
    recipes = coffeeMaker.getRecipes()
    for i in range(len(recipes)):
        if recipes[i] is not None:
            print(f"{i + 1} . {recipes[i].getName()}")

    recipeToEdit = recipeListSelection(
        "Please select the number of the recipe to edit."
    )

    if recipeToEdit < 0:
        mainMenu()

    # Read in recipe price
    priceString = inputOutput("\nPlease enter the recipe price: $")

    # Read in amt coffee
    coffeeString = inputOutput("\nPlease enter the units of coffee in the recipe: ")

    # Read in amt milk
    milkString = inputOutput("\nPlease enter the units of milk in the recipe: ")

    # Read in amt sugar
    sugarString = inputOutput("\nPlease enter the units of sugar in the recipe: ")

    # Read in amt chocolate
    chocolateString = inputOutput(
        "\nPlease enter the units of chocolate in the recipe: "
    )

    newRecipe = Recipe()
    try:
        newRecipe.setPrice(priceString)
        newRecipe.setAmtCoffee(coffeeString)
        newRecipe.setAmtMilk(milkString)
        newRecipe.setAmtSugar(sugarString)
        newRecipe.setAmtChocolate(chocolateString)

        recipeEdited = coffeeMaker.editRecipe(recipeToEdit, newRecipe)

        if recipeEdited is not None:
            print(recipeEdited + " successfully edited.\n")

        else:
            print(recipeEdited + "could not be edited.\n")

    except RecipeException as e:
        print(e)
    finally:
        mainMenu()


def addInventory():
    # Read in amt coffee
    coffeeString = inputOutput("\nPlease enter the units of coffee to add: ")

    # Read in amt milk
    milkString = inputOutput("\nPlease enter the units of milk to add: ")

    # Read in amt sugar
    sugarString = inputOutput("\nPlease enter the units of sugar to add: ")

    # Read in amt chocolate
    chocolateString = inputOutput("\nPlease enter the units of chocolate to add: ")

    try:
        coffeeMaker.addInventory(coffeeString, milkString, sugarString, chocolateString)
        print("Inventory successfully added")
    except InventoryException as e:
        print("Inventory was not added")
    finally:
        mainMenu()


def checkInventory():
    print(coffeeMaker.checkInventory())
    mainMenu()


def makeCoffee():
    recipes = coffeeMaker.getRecipes()

    for i in range(len(recipes)):
        if recipes[i] is not None:
            print(f"{i + 1} . {recipes[i].getName()}")

    recipeToPurchase = recipeListSelection(
        "Please select the number of the recipe to purchase."
    )

    amountPaid = inputOutput("Please enter the amount you wish to pay")
    amtPaid = 0
    try:
        amtPaid = int(amountPaid)
    except Exception as e:
        print("Please enter a positive integer")
        mainMenu()

    change = coffeeMaker.makeCoffee(recipeToPurchase, amtPaid)

    if change == amtPaid:
        print("Insufficient funds to purchase.")
    else:
        print(
            "Thank you for purchasing "
            + coffeeMaker.getRecipes()[recipeToPurchase].getName()
        )

    print("Your change is: " + change + "\n")
    mainMenu()


def mainMenu():
    print("1. Add a recipe")
    print("2. Delete a recipe")
    print("3. Edit a recipe")
    print("4. Add inventory")
    print("5. Check inventory")
    print("6. Make coffee")
    print("0. Exit\n")

    try:
        userInput = int(
            inputOutput(
                "Please press the number that corresponds to what you would like the coffee maker to do."
            )
        )

        if userInput >= 0 and userInput <= 6:
            if userInput == 1:
                addRecipe()
            if userInput == 2:
                deleteRecipe()
            if userInput == 3:
                editRecipe()
            if userInput == 4:
                addInventory()
            if userInput == 5:
                checkInventory()
            if userInput == 6:
                makeCoffee()
            if userInput == 0:
                exit(0)
        else:
            print("Please enter a number from 0 - 6")
            mainMenu()

    except Exception as e:
        print("Please enter a number from 0 - 6")
        mainMenu()


if __name__ == "__main__":
    coffeeMaker = CoffeeMaker()
    print("Welcome to the CoffeeMaker!\n")
    mainMenu()
1
