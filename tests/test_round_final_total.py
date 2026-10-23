"""Pruebas unitarias de R7 (resultado): round_final_total."""

from gym import round_final_total


def test_round_whole_number_stays_the_same():
    """Un total entero no cambia (30 -> 30)."""
    assert round_final_total(30, True) == 30


def test_round_half_goes_up():
    """El .5 se redondea hacia arriba (121.5 -> 122), no al par más cercano."""
    assert round_final_total(121.5, True) == 122
    assert round_final_total(2.5, True) == 3
    assert round_final_total(0.5, True) == 1


def test_round_below_half_goes_down():
    """Por debajo de .5 se redondea hacia abajo (215.05 -> 215)."""
    assert round_final_total(215.05, True) == 215


def test_round_above_half_goes_up():
    """Por encima de .5 se redondea hacia arriba (411.7 -> 412, 625.6 -> 626)."""
    assert round_final_total(411.7, True) == 412
    assert round_final_total(625.6, True) == 626


def test_round_invalid_selection():
    """Si la selección es inválida, el resultado es -1."""
    assert round_final_total(100, False) == -1
    assert round_final_total(-1, True) == -1


def test_round_user_cancelled():
    """Si el usuario responde 'n' en la confirmación, el resultado es -1."""
    user_confirmed = False
    assert round_final_total(250.0, user_confirmed) == -1
