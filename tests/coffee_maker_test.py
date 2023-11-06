from src import CoffeeMaker, Recipe


class TestCoffeeMaker:
    def setup_method(self, method):
        self.coffee_maker_instance = CoffeeMaker()

    def test_add_recipe(self):
        recipe = Recipe()
        recipe.setName("Espresso")
        recipe.setPrice(2.5)
        recipe.setAmtCoffee(2)
        recipe.setAmtMilk(1)
        recipe.setAmtSugar(0)
        recipe.setAmtChocolate(0)

        added = self.coffee_maker_instance.addRecipe(recipe)

        assert added is True
        assert len(self.coffee_maker_instance.recipeBook.getRecipes()) == 1

    def test_delete_recipe(self):
        recipe = Recipe()
        recipe.setName("Latte")
        recipe.setPrice(3.0)
        recipe.setAmtCoffee(1)
        recipe.setAmtMilk(2)
        recipe.setAmtSugar(1)
        recipe.setAmtChocolate(0)

        self.coffee_maker_instance.addRecipe(recipe)
        recipes_before = len(self.coffee_maker_instance.recipeBook.getRecipes())
        deleted_recipe = self.coffee_maker_instance.deleteRecipe(0)
        recipes_after = len(self.coffee_maker_instance.recipeBook.getRecipes())

        assert deleted_recipe is not None
        assert recipes_before == recipes_after + 1

    def test_edit_recipe(self):
        recipe = Recipe()
        recipe.setName("Cappuccino")
        recipe.setPrice(3.5)
        recipe.setAmtCoffee(1)
        recipe.setAmtMilk(2)
        recipe.setAmtSugar(0)
        recipe.setAmtChocolate(1)

        self.coffee_maker_instance.addRecipe(recipe)

        new_recipe = Recipe()
        new_recipe.setPrice(4.0)
        new_recipe.setAmtCoffee(2)
        new_recipe.setAmtMilk(2)
        new_recipe.setAmtSugar(1)
        new_recipe.setAmtChocolate(1)

        edited_recipe_name = self.coffee_maker_instance.editRecipe(0, new_recipe)

        assert edited_recipe_name is not None
        assert edited_recipe_name == "Cappuccino"

    def test_make_coffee(self):
        recipe = Recipe()
        recipe.setName("Mocha")
        recipe.setPrice(4.0)
        recipe.setAmtCoffee(2)
        recipe.setAmtMilk(1)
        recipe.setAmtSugar(1)
        recipe.setAmtChocolate(2)

        self.coffee_maker_instance.addRecipe(recipe)

        self.coffee_maker_instance.addInventory(10, 5, 5, 10)
        change = self.coffee_maker_instance.makeCoffee(0, 5.0)

        assert change == 1.0
        assert (
            self.coffee_maker_instance.checkInventory()
            == "Coffee: 8\nMilk: 4\nSugar: 4\nChocolate: 8\n"
        )
