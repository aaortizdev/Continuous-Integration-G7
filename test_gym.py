"""Pruebas de la cotización del gimnasio."""

from gym import GymQuote


def test_initial_total():
    """Una cotización nueva comienza con total cero."""
    quote = GymQuote()
    assert quote.total == 0
    