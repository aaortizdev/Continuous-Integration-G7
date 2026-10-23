"""Pruebas unitarias de R1 (planes): get_plan_price."""

from gym import get_plan_price


def test_plan_price_basic():
    """El plan BASIC cuesta 30 por miembro."""
    assert get_plan_price("BASIC") == 30


def test_plan_price_standard():
    """El plan STANDARD cuesta 45 por miembro."""
    assert get_plan_price("STANDARD") == 45


def test_plan_price_premium():
    """El plan PREMIUM cuesta 70 por miembro."""
    assert get_plan_price("PREMIUM") == 70


def test_plan_price_ignores_case_and_spaces():
    """El nombre del plan se acepta en minúsculas y con espacios alrededor."""
    assert get_plan_price("  basic ") == 30


def test_plan_price_invalid_plan():
    """Un plan que no está en la tabla (GOLD) devuelve -1."""
    assert get_plan_price("GOLD") == -1


def test_plan_price_empty_or_missing_plan():
    """Un plan vacío o ausente devuelve -1."""
    assert get_plan_price("") == -1
    assert get_plan_price(None) == -1
