"""Pruebas para el descuento grupal (R4)."""

from gym import apply_group_discount


def test_group_discount_applied():
    """Prueba que el descuento grupal se aplique con 2 miembros."""
    assert apply_group_discount(100, 2) == 90.0


def test_group_discount_not_applied():
    """Prueba que el descuento grupal no se aplique con 1 miembro."""
    assert apply_group_discount(100, 1) == 100.0
