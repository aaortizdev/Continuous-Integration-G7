"""Pruebas de la cotización del gimnasio."""

import pytest

from gym import GymQuote
from gym import apply_group_discount, apply_special_offer, apply_premium_surcharge


def test_initial_total():
    """Una cotización nueva comienza con total cero."""
    quote = GymQuote()
    assert quote.total == 0

# --- Tests de Developer B (Genesis) ---

# R4 - Group Discount
def test_group_discount_applied():
    """Prueba que el descuento grupal se aplique con 2 miembros."""
    assert apply_group_discount(100, 2) == 90.0


def test_group_discount_not_applied():
    """Prueba que el descuento grupal no se aplique con 1 miembro."""
    assert apply_group_discount(100, 1) == 100.0


# R5 - Special Offer
def test_special_offer_gt_400():
    """Prueba la oferta especial cuando el monto es mayor a 400."""
    assert apply_special_offer(500) == 450.0


def test_special_offer_gt_200():
    """Prueba la oferta especial cuando el monto es mayor a 200."""
    assert apply_special_offer(300) == 280.0


def test_special_offer_less_or_equal_200():
    """Prueba que no se aplique oferta cuando el monto es 200 o menos."""
    assert apply_special_offer(150) == 150.0


# R6 - Premium Surcharge
def test_premium_surcharge_applied():
    """Prueba que se aplique el recargo premium."""
    assert apply_premium_surcharge(100, ["premium_support"]) == pytest.approx(115.0)


def test_premium_surcharge_not_applied():
    """Prueba que no se aplique el recargo si no hay extras premium."""
    assert apply_premium_surcharge(100, ["basic_support"]) == 100.0
