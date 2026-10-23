"""Pruebas para el recargo premium (R6)."""

import pytest

from gym import apply_premium_surcharge


def test_premium_surcharge_applied():
    """Prueba que se aplique el recargo premium."""
    assert apply_premium_surcharge(100, ["SPA"]) == pytest.approx(115.0)

def test_premium_surcharge_not_applied():
    """Prueba que no se aplique el recargo si no hay extras premium."""
    assert apply_premium_surcharge(100, ["GROUP_CLASSES"]) == 100.0
