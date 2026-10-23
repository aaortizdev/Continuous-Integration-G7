"""Cálculo de cotizaciones del gimnasio."""


class GymQuote:  # pylint: disable=too-few-public-methods
    """Representa la estructura inicial de una cotización."""

    def __init__(self):
        self.total = 0


def get_plan_price(plan: str) -> float:
    return 30.0  # Valor simulado temporal

def get_extras_price(plan: str, extras: list) -> float:
    return 0.0

def calculate_subtotal(plan_price: float, extras_price: float, members: int) -> float:
    return (plan_price + extras_price) * members

def apply_group_discount(amount: float, members: int) -> float:
    return amount

def apply_special_offer(amount: float) -> float:
    return amount

def apply_premium_surcharge(amount: float, extras: list) -> float:
    return amount

def round_final_total(total_amount: float, is_valid: bool) -> int:
    return int(total_amount)

def calculate_quote(plan: str, extras: list, members: int) -> int:
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