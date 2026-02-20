#Things that could go wrong:
#Negative vol, extremely large vol, missing value, non-numeric value
from typing import Iterable
import math

class ValidationError(ValueError):
    """Raised when volatility validation fails."""
    pass

def is_numeric(val) -> bool:
    return isinstance(val, (int, float)) and not isinstance(val, bool)



def validate_volatility(vols: Iterable[float])-> None:
    errors=[]
    vols=list(vols)
    if not vols:
        errors.append("Volatility data cannot be empty")
    for idx,vol in enumerate(vols):
        if vol is None:
            errors.append(f"Missing value ({vol}) detected at index {idx}")
            continue

        if not is_numeric(vol):
            errors.append(f"Volatility value ({vol}) is non numeric at index {idx}")
            continue

        if math.isnan(vol):
            errors.append(f"NaN detected at index {idx}")
            continue

        if math.isinf(vol):
            errors.append(f"Infinite volatility detected at index {idx}")
            continue

        if vol<0:
            errors.append(f"Negative vol ({vol}) found at index {idx}")

        if vol>5.0:
            errors.append(f"Volatility value unrealistically high ({vol}) at index {idx}")
    if errors:
            raise ValidationError(errors)
        