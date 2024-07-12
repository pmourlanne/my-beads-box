def get_price_display(amount, currency):
    # TODO: handle more currencies
    if currency == "USD":
        return f"${amount/100:.2f}"

    if currency == "EUR":
        return f"{amount/100:.2f}€"

    raise ValueError(f"Unknown currency: {currency}")
