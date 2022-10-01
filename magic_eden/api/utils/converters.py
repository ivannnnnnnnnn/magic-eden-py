from typing import Any

DIVIDER = 1_000_000_000


def convert_sol_absolute(v: Any) -> float:
    if isinstance(v, int):
        return round(v / DIVIDER, 2)
    return round(float(0), 2)
