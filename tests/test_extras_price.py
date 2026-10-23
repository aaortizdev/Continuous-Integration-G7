"""Pruebas unitarias de R2 (extras): get_extras_price."""

from gym import get_extras_price


def test_extras_price_no_extras():
    """Sin extras, el costo de los extras es 0."""
    assert get_extras_price("BASIC", []) == 0


def test_extras_price_one_regular_extra():
    """PERSONAL_TRAINING cuesta 25 con cualquier plan."""
    assert get_extras_price("STANDARD", ["PERSONAL_TRAINING"]) == 25


def test_extras_price_two_regular_extras():
    """GROUP_CLASSES + PERSONAL_TRAINING suman 15 + 25 = 40."""
    assert get_extras_price("STANDARD", ["GROUP_CLASSES", "PERSONAL_TRAINING"]) == 40


def test_extras_price_premium_extras_with_premium_plan():
    """Con el plan PREMIUM, SPA + SPECIALIZED_PROGRAM suman 30 + 40 = 70."""
    assert get_extras_price("PREMIUM", ["SPA", "SPECIALIZED_PROGRAM"]) == 70


def test_extras_price_mixed_extras_with_premium_plan():
    """Con el plan PREMIUM se pueden combinar extras normales y premium (95)."""
    extras = ["SPA", "SPECIALIZED_PROGRAM", "PERSONAL_TRAINING"]
    assert get_extras_price("PREMIUM", extras) == 95


def test_extras_price_premium_extra_without_premium_plan():
    """Un extra premium (SPA) con el plan BASIC hace inválida la selección."""
    assert get_extras_price("BASIC", ["SPA"]) == -1
    assert get_extras_price("STANDARD", ["SPECIALIZED_PROGRAM"]) == -1


def test_extras_price_unknown_extra():
    """Un extra que no está en la tabla devuelve -1."""
    assert get_extras_price("PREMIUM", ["SAUNA"]) == -1


def test_extras_price_repeated_extra():
    """Un extra repetido hace inválida la selección (supuesto del equipo)."""
    assert get_extras_price("BASIC", ["GROUP_CLASSES", "GROUP_CLASSES"]) == -1
