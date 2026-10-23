"""Pruebas unitarias de R3 (subtotal): calculate_subtotal."""

from gym import calculate_subtotal


def test_subtotal_one_member():
    """Con un miembro, el subtotal es plan + extras (30 + 0 = 30)."""
    assert calculate_subtotal(30, 0, 1) == 30


def test_subtotal_several_members():
    """El subtotal se multiplica por el número de miembros: (30 + 15) * 3 = 135."""
    assert calculate_subtotal(30, 15, 3) == 135


def test_subtotal_four_members_with_extras():
    """(45 + 40) * 4 = 340."""
    assert calculate_subtotal(45, 40, 4) == 340


def test_subtotal_zero_members():
    """Con 0 miembros la cotización es inválida y devuelve -1."""
    assert calculate_subtotal(30, 0, 0) == -1


def test_subtotal_negative_members():
    """Un número negativo de miembros devuelve -1."""
    assert calculate_subtotal(30, 0, -2) == -1


def test_subtotal_invalid_plan_or_extras_price():
    """Si R1 o R2 devolvieron -1, el subtotal también es -1."""
    assert calculate_subtotal(-1, 0, 1) == -1
    assert calculate_subtotal(30, -1, 1) == -1
