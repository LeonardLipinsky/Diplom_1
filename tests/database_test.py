import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_database_initialization(self, database):
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6
        assert isinstance(database.buns[0], Bun)
        assert database.buns[0].name == "black bun"
        assert database.buns[0].price == 100
        assert isinstance(database.ingredients[0], Ingredient)
        assert database.ingredients[0].name == "hot sauce"
        assert database.ingredients[0].price == 100
        assert database.ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE

    def test_available_buns(self, database):
        buns = database.available_buns()
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        assert buns[0].name == "black bun"


    def test_available_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert all(
            isinstance(ingredient, Ingredient) for ingredient in ingredients)
        sauces = ingredients[:3]
        fillings = ingredients[3:]
        assert all(ingredient.get_type() == INGREDIENT_TYPE_SAUCE for ingredient in sauces)
        assert all(ingredient.get_type() == INGREDIENT_TYPE_FILLING for ingredient in fillings)