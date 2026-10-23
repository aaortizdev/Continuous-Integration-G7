from gym import calculate_quote

def test_calculate_quote_invalid_plan():
    """R8: Si el plan no existe (ej. GOLD), la cotización general debe retornar -1."""
    assert calculate_quote("GOLD", [], 1) == -1

def test_calculate_quote_invalid_members():
    """R8: Si los miembros son menores a 1 (ej. 0), la cotización general debe retornar -1."""
    assert calculate_quote("BASIC", [], 0) == -1

def test_calculate_quote_invalid_extra_for_plan():
    """R8: Si se pide un extra premium (SPA) en un plan inferior (BASIC), retorna -1."""
    assert calculate_quote("BASIC", ["SPA"], 1) == -1