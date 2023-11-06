import pytest

from src import Inventory, InventoryException, Recipe


class TestInventory:
    def setup_method(self, method):
        self.inventory_instance = Inventory()
        Inventory.setCoffee(0)
        Inventory.setMilk(0)
        Inventory.setChocolate(0)
        Inventory.setSugar(0)

    def test_add_coffee(self):
        self.inventory_instance.addCoffee(10)
        assert self.inventory_instance.getCoffee() == 10

    def test_add_milk(self):
        self.inventory_instance.addMilk(5)
        assert self.inventory_instance.getMilk() == 5

    def test_add_sugar(self):
        self.inventory_instance.addSugar(7)
        assert self.inventory_instance.getSugar() == 7

    def test_add_chocolate(self):
        self.inventory_instance.addChocolate(3)
        assert self.inventory_instance.getChocolate() == 3

    def test_use_ingredients_success(self):
        self.inventory_instance.addCoffee(10)
        self.inventory_instance.addMilk(5)
        self.inventory_instance.addSugar(7)
        self.inventory_instance.addChocolate(3)

        recipe = Recipe()
        recipe.setAmtCoffee(5)
        recipe.setAmtMilk(2)
        recipe.setAmtSugar(1)
        recipe.setAmtChocolate(2)

        success = self.inventory_instance.useIngredients(
            recipe
        )  # Assume a Recipe class with these ingredient amounts

        assert success is True
        assert self.inventory_instance.getCoffee() == 5
        assert self.inventory_instance.getMilk() == 3
        assert self.inventory_instance.getSugar() == 6
        assert self.inventory_instance.getChocolate() == 1

    def test_use_ingredients_failure(self):
        self.inventory_instance.addCoffee(2)
        self.inventory_instance.addMilk(2)
        self.inventory_instance.addSugar(2)
        self.inventory_instance.addChocolate(2)

        recipe = Recipe()
        recipe.setAmtCoffee(5)
        recipe.setAmtMilk(2)
        recipe.setAmtSugar(1)
        recipe.setAmtChocolate(2)

        success = self.inventory_instance.useIngredients(recipe)

        assert success is False
        assert self.inventory_instance.getCoffee() == 2
        assert self.inventory_instance.getMilk() == 2
        assert self.inventory_instance.getSugar() == 2
        assert self.inventory_instance.getChocolate() == 2

    def test_add_negative_amount_coffee(self):
        with pytest.raises(InventoryException):
            self.inventory_instance.addCoffee(-5)
