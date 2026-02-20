from ccr_controls.validators import validate_volatility,ValidationError
from typing import Iterable


def runvolcheck(vols: Iterable[float]) ->None:
    try:
        validate_volatility(vols)
        print("Successful")
    except ValidationError as e:
        print(f"Validation failed:\n{e}")

runvolcheck([float("nan"), -1, 10, "0.3", None, float("inf")])
     
