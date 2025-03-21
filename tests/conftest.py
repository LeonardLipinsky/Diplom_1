import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.database import Database


@pytest.fixture
def bun():
    return Bun(name="Sesame Bun", price=2.5)


@pytest.fixture
def ingredient():
    return Ingredient(ingredient_type="meat", name="Beef Patty", price=5.0)


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def database():
    return Database()