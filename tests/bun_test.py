import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize(
        "name,price,expected_name,expected_price",
        [
            ("Sesame Bun", 2.5, "Sesame Bun", 2.5),
            ("Gluten-Free Bun", 3.0, "Gluten-Free Bun", 3.0),
            ("Brioche Bun", 2.8, "Brioche Bun", 2.8)
        ]
    )
    def test_bun_properties(self, name, price, expected_name, expected_price):
        bun = Bun(name=name, price=price)
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price