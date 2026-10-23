"""Pruebas para la oferta especial (R5)."""

from gym import apply_special_offer


def test_special_offer_gt_400():
    """Prueba la oferta especial cuando el monto es mayor a 400."""
    assert apply_special_offer(500) == 450.0


def test_special_offer_gt_200():
    """Prueba la oferta especial cuando el monto es mayor a 200."""
    assert apply_special_offer(300) == 280.0


def test_special_offer_less_or_equal_200():
    """Prueba que no se aplique oferta cuando el monto es 200 o menos."""
    assert apply_special_offer(150) == 150.0
