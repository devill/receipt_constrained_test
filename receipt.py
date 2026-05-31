from datetime import date, timedelta

TAX_RATE = 0.20


def format_receipt(items_with_prices, items_with_quantities, today=None):
    prices = dict(items_with_prices)
    quantities = dict(items_with_quantities)
    today = today or date.today()
    payable_by = today + timedelta(days=7)

    lines = [
        "RECEIPT",
        "",
        f"Date: {today.isoformat()}",
        f"Payable by: {payable_by.isoformat()}",
        "",
    ]

    subtotal = 0.0
    for item, qty in quantities.items():
        price = prices[item]
        line_total = price * qty
        subtotal += line_total
        lines.append(f"{item} x {qty} @ {price:.2f} = {line_total:.2f}")

    tax = subtotal * TAX_RATE
    total = subtotal + tax

    lines += [
        "",
        f"Subtotal: {subtotal:.2f}",
        f"Tax:      {tax:.2f}",
        f"Total:    {total:.2f}",
    ]
    return "\n".join(lines)
