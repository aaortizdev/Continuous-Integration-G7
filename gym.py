"""Cálculo de cotizaciones del gimnasio."""

from decimal import Decimal, ROUND_HALF_UP

PLAN_PRICES = {"BASIC": 30, "STANDARD": 45, "PREMIUM": 70}
EXTRA_PRICES = {
    "GROUP_CLASSES": 15,
    "PERSONAL_TRAINING": 25,
    "SPA": 30,
    "SPECIALIZED_PROGRAM": 40,
}
PREMIUM_EXTRAS = {"SPA", "SPECIALIZED_PROGRAM"}
INVALID = -1


class GymQuote:  # pylint: disable=too-few-public-methods
    """Representa la estructura inicial de una cotización."""

    def __init__(self):
        self.total = 0


# --- Developer A: R1, R2, R3, R7 ---


def _normalize(name) -> str:
    """Devuelve el nombre en mayúsculas y sin espacios, o '' si no es texto."""
    return name.strip().upper() if isinstance(name, str) else ""


def get_plan_price(plan: str) -> float:
    """R1: devuelve el precio del plan (30, 45 o 70), o -1 si el plan es inválido."""
    return float(PLAN_PRICES.get(_normalize(plan), INVALID))


def get_extras_price(plan: str, extras: list) -> float:
    """R2: devuelve el costo total de los extras, o -1 si la selección es inválida.
    Es inválida si un extra es desconocido, si se repite, o si se elige un extra
    premium sin tener el plan PREMIUM.
    """
    plan_name = _normalize(plan)
    chosen = set()
    total = 0.0
    for extra in extras or []:
        name = _normalize(extra)
        if name not in EXTRA_PRICES or name in chosen:
            return INVALID
        if name in PREMIUM_EXTRAS and plan_name != "PREMIUM":
            return INVALID
        chosen.add(name)
        total += EXTRA_PRICES[name]
    return total


def calculate_subtotal(plan_price: float, extras_price: float, members: int) -> float:
    """R3: devuelve (plan_price + extras_price) * members, o -1 si la entrada es inválida."""
    if members < 1 or plan_price < 0 or extras_price < 0:
        return INVALID
    return (plan_price + extras_price) * members


def round_final_total(total_amount: float, is_valid: bool) -> int:
    """R7: redondea half up a un entero; devuelve -1 si es inválido o se canceló."""
    if not is_valid or total_amount < 0:
        return INVALID
    return int(Decimal(str(total_amount)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
