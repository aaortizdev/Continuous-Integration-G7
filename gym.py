"""Cálculo de cotizaciones del gimnasio."""


class GymQuote:  # pylint: disable=too-few-public-methods
    """Representa la estructura inicial de una cotización."""

    def __init__(self):
        self.total = 0




def apply_group_discount(subtotal: float, members: int) -> float:
    """R4. Descuento grupal: 2 o más miembros obtienen 10% de descuento."""
    if members >= 2:
        return subtotal * 0.90
    return subtotal


def apply_special_offer(amount: float) -> float:
    """R5. Oferta especial: si es > 400 resta 50; si es > 200 resta 20."""
    if amount > 400:
        return amount - 50.0
    if amount > 200:
        return amount - 20.0
    return amount


def apply_premium_surcharge(amount: float, extras: list) -> float:
    """R6. Recargo premium: si hay al menos un extra premium, suma 15%."""
    # ⚠️ Ajusta "premium_support" y "premium_training" a los nombres reales de su tabla
    premium_extras = {"premium_support", "premium_training"}
    has_premium = any(e in premium_extras for e in extras)
    if has_premium:
        return amount * 1.15
    return amount

    