
import unittest
from decimal import Decimal
from invoice import calculate_line_total, calculate_invoice


class TestInvoice(unittest.TestCase):

    def test_line_total(self):
        result = calculate_line_total(2, "100")
        self.assertEqual(result, Decimal("200.00"))

    def test_invoice_subtotal(self):
        items = [
            {"quantity": 2, "unit_price": "100"},
            {"quantity": 3, "unit_price": "50"}
        ]

        result = calculate_invoice(items)
        self.assertEqual(result["subtotal"], Decimal("350.00"))

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            calculate_line_total(0, "100")

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_line_total(2, "-50")

    def test_empty_invoice(self):
        with self.assertRaises(ValueError):
            calculate_invoice([])

    def test_decimal_precision(self):
        self.assertEqual(
            calculate_line_total(2, "10.25"),
            Decimal("20.50")
        )

    def test_small_decimal_precision(self):
        self.assertEqual(
            calculate_line_total(3, "0.10"),
            Decimal("0.30")
        )

    def test_fractional_quantity(self):
        self.assertEqual(
            calculate_line_total("1.5", "10.00"),
            Decimal("15.00")
        )


if __name__ == "__main__":
    unittest.main()
