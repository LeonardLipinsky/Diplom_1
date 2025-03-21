from unittest.mock import MagicMock
from praktikum.ingredient import Ingredient

class TestBurger:
    def test_set_buns(self, burger, bun):
        burger.set_buns(bun)
        assert burger.bun is bun

    def test_add_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self, burger, ingredient):
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger, ingredient):
        another_ingredient = Ingredient("sauce", "Ketchup", 1.5)
        burger.add_ingredient(ingredient)
        burger.add_ingredient(another_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == another_ingredient
        assert burger.ingredients[1] == ingredient

    def test_get_price(self, burger, bun, ingredient):
        mocked_bun = MagicMock()
        mocked_bun.get_price.return_value = 2.5
        mocked_ingredient = MagicMock()
        mocked_ingredient.get_price.return_value = 5.0
        burger.set_buns(mocked_bun)
        burger.add_ingredient(mocked_ingredient)
        price = burger.get_price()
        assert price == 10.0

    def test_get_receipt(self, burger, bun, ingredient):
        mocked_bun = MagicMock()
        mocked_bun.get_name.return_value = "Sesame Bun"
        mocked_bun.get_price.return_value = 2.5
        mocked_ingredient = MagicMock()
        mocked_ingredient.get_type.return_value = "Meat"
        mocked_ingredient.get_name.return_value = "Beef Patty"
        mocked_ingredient.get_price.return_value = 5.0
        burger.set_buns(mocked_bun)
        burger.add_ingredient(mocked_ingredient)
        receipt = burger.get_receipt()
        expected_receipt = (
            "(==== Sesame Bun ====)\n"
            "= meat Beef Patty =\n"
            "(==== Sesame Bun ====)\n"
            "\n"  
            "Price: 10.0"
            )
        assert receipt == expected_receipt