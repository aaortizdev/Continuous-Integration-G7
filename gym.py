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
    has_premium = any(_normalize(e) in PREMIUM_EXTRAS for e in extras)
    if has_premium:
        return amount * 1.15
    return amount


def round_final_total(total_amount: float, is_valid: bool) -> int:
    """R7: redondea half up a un entero; devuelve -1 si es inválido o se canceló."""
    if not is_valid or total_amount < 0:
        return INVALID
    return int(Decimal(str(total_amount)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))

def calculate_quote(plan: str, extras: list, members: int) -> int:
    """Calcula la cotización total uniendo las reglas del equipo."""
    plan_price = get_plan_price(plan)
    extras_price = get_extras_price(plan, extras)
    if plan_price == -1 or extras_price == -1 or members < 1:
        return -1
    subtotal = calculate_subtotal(plan_price, extras_price, members)
    after_r4 = apply_group_discount(subtotal, members)
    after_r5 = apply_special_offer(after_r4)
    after_r6 = apply_premium_surcharge(after_r5, extras)
    return round_final_total(after_r6, True)

if __name__ == '__main__':
    # 1. Pedir datos al usuario
    plan_input = input("Ingrese el plan (BASIC, STANDARD, PREMIUM): ").strip()
    extras_input = input("Ingrese los extras separados por coma (o deje vacío): ").strip()
    # Convertir el string de extras en una lista
    if extras_input:
        extras_list = [e.strip() for e in extras_input.split(',')]
    else:
        extras_list = []
    members_input = int(input("Ingrese el número de miembros: "))
    # 2. Lógica para desglosar y mostrar los valores intermedios
    p_price = get_plan_price(plan_input)
    e_price = get_extras_price(plan_input, extras_list)
    if p_price == -1 or e_price == -1 or members_input < 1:
        print("Selección inválida.")
        print("Resultado: -1")
    else:
        # Calcular los pasos intermedios para mostrarlos en consola
        sub = calculate_subtotal(p_price, e_price, members_input)
        r4_val = apply_group_discount(sub, members_input)
        r5_val = apply_special_offer(r4_val)
        r6_val = apply_premium_surcharge(r5_val, extras_list)
        print("\n--- RESUMEN DE COTIZACIÓN ---")
        print(f"Subtotal: {sub}")
        print(f"Descuento grupal aplicado: {sub - r4_val}")
        print(f"Descuento de oferta especial: {r4_val - r5_val}")
        print(f"Recargo premium: {r6_val - r5_val}")
        print(f"Total preliminar: {r6_val}")
        print("-----------------------------\n")
        confirm = input("¿Desea confirmar esta cotización? (y/n): ").strip().lower()
        if confirm == 'y':
            final_result = calculate_quote(plan_input, extras_list, members_input)
            print(f"Resultado: {final_result}")
        else:
            print("Resultado: -1")
