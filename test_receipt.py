import re

from receipt import format_receipt


def test_sums_and_dates_are_correct():
    items_with_prices = [("apple", 1.00), ("bread", 2.50)]
    items_with_quantities = [("apple", 3), ("bread", 2)]

    receipt = format_receipt(items_with_prices, items_with_quantities)

    assert re.search(r"Date: \d{4}-\d{2}-\d{2}", receipt)
    assert re.search(r"Payable by: \d{4}-\d{2}-\d{2}", receipt)
    assert "8.00" in receipt
