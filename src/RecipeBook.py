class RecipeBook:
    def __init__(self):
        self.recipeArray = [None] * 3

    def getRecipes(self):
        return [i for i in self.recipeArray if i is not None]

    def addRecipe(self, r):
        exists = False

        for i in range(len(self.recipeArray)):
            if r == self.recipeArray[i]:
                exists = True

        added = False

        if not exists:
            for i in range(len(self.recipeArray)):
                if self.recipeArray[i] is None:
                    self.recipeArray[i] = r
                    added = True
                    break

        return added

    def deleteRecipe(self, recipeToDelete):
        if recipeToDelete < 0 or recipeToDelete >= len(self.recipeArray):
            return None

        if self.recipeArray[recipeToDelete] is not None:
            recipeName = self.recipeArray[recipeToDelete].getName()
            self.recipeArray[recipeToDelete] = None
            return recipeName
        else:
            return None

    def editRecipe(self, recipeToEdit, newRecipe):
        if recipeToEdit < 0 or recipeToEdit >= len(
            [i for i in self.recipeArray if i is not None]
        ):
            return None

        if self.recipeArray[recipeToEdit] is not None:
            recipeName = self.recipeArray[recipeToEdit].getName()
            self.recipeArray[recipeToEdit] = newRecipe
            newRecipe.setName(recipeName)
            return recipeName
        else:
            return None
