
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


MONEY_PLACES = Decimal("0.01")


def money(value):
    """Convert a value into a validated two-decimal monetary amount."""
    try:
        amount = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError("Invalid monetary value.")

    if not amount.is_finite() or amount < 0:
        raise ValueError("Amount must be finite and non-negative.")

    return amount.quantize(MONEY_PLACES, rounding=ROUND_HALF_UP)


def calculate_line_total(quantity, unit_price):
    """Calculate one invoice line total."""
    try:
        qty = Decimal(str(quantity))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError("Invalid quantity.")

    if not qty.is_finite() or qty <= 0:
        raise ValueError("Quantity must be greater than zero.")

    price = money(unit_price)
    return (qty * price).quantize(
        MONEY_PLACES, rounding=ROUND_HALF_UP
    )


def calculate_invoice(items):
    """Calculate invoice subtotal and total from line items."""
    if not items:
        raise ValueError("Invoice must contain at least one item.")

    subtotal = Decimal("0.00")

    for item in items:
        if "quantity" not in item or "unit_price" not in item:
            raise ValueError("Each item needs quantity and unit_price.")

        subtotal += calculate_line_total(
            item["quantity"],
            item["unit_price"]
        )

    subtotal = money(subtotal)

    return {
        "subtotal": subtotal,
        "total": subtotal
    }
