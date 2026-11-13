
import unittest
from decimal import Decimal

from invoice import (
    calculate_line_total,
    calculate_invoice,
)


class TestInvoice(unittest.TestCase):

    def test_line_total(self):
        result = calculate_line_total(2, "100.00")
        self.assertEqual(result, Decimal("200.00"))

    def test_invoice_subtotal(self):
        items = [
            {"quantity": 2, "unit_price": "100.00"},
            {"quantity": 3, "unit_price": "50.00"},
        ]

        result = calculate_invoice(items)

        self.assertEqual(result["subtotal"], Decimal("350.00"))
        self.assertEqual(result["total"], Decimal("350.00"))

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            calculate_line_total(0, "100.00")

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_line_total(1, "-50.00")

    def test_empty_invoice(self):
        with self.assertRaises(ValueError):
            calculate_invoice([])


if __name__ == "__main__":
    unittest.main()
