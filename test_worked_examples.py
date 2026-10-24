"""Comprueba los once ejemplos del enunciado del gimnasio."""

import pytest

from gym import calculate_quote


@pytest.mark.parametrize(
    "plan, extras, members, expected",
    [
        pytest.param(
            "BASIC", [], 1, 30,
            id="example-01-basic",
        ),
        pytest.param(
            "STANDARD", ["PERSONAL_TRAINING"], 1, 70,
            id="example-02-standard-training",
        ),
        pytest.param(
            "BASIC", ["GROUP_CLASSES"], 2, 81,
            id="example-03-group-discount",
        ),
        pytest.param(
            "BASIC", ["GROUP_CLASSES"], 3, 122,
            id="example-04-half-up-rounding",
        ),
        pytest.param(
            "STANDARD", ["GROUP_CLASSES", "PERSONAL_TRAINING"], 4, 286,
            id="example-05-special-offer",
        ),
        pytest.param(
            "PREMIUM", ["GROUP_CLASSES", "SPA"], 2, 215,
            id="example-06-premium-surcharge",
        ),
        pytest.param(
            "PREMIUM", ["SPA", "SPECIALIZED_PROGRAM"], 3, 412,
            id="example-07-premium-offer",
        ),
        pytest.param(
            "PREMIUM",
            ["SPA", "SPECIALIZED_PROGRAM", "PERSONAL_TRAINING"],
            4,
            626,
            id="example-08-large-premium-group",
        ),
        pytest.param(
            "BASIC", ["SPA"], 1, -1,
            id="example-09-invalid-premium-extra",
        ),
        pytest.param(
            "GOLD", [], 1, -1,
            id="example-10-invalid-plan",
        ),
        pytest.param(
            "BASIC", [], 0, -1,
            id="example-11-invalid-members",
        ),
    ],
)
def test_worked_examples(plan, extras, members, expected):
    """Cada ejemplo debe producir el total indicado en el enunciado."""
    assert calculate_quote(plan, extras, members) == expected
