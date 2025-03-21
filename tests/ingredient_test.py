import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:
    @pytest.mark.parametrize(
        "ingredient_type, name, price, expected_type, expected_name, expected_price",
        [
            ("meat", "Beef Patty", 5.0, "meat", "Beef Patty", 5.0),
            ("sauce", "Ketchup", 0.5, "sauce", "Ketchup", 0.5)
        ]
        )
    def test_ingredient_properties(self, ingredient_type, name, price, expected_type, expected_name, expected_price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price