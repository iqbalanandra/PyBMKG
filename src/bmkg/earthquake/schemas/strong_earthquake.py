from dataclasses import dataclass

from .earthquake import Earthquake

__all__ = ["StrongEarthquake"]


@dataclass(slots=True)
class StrongEarthquake:
    """
    `StrongEarthquake` schema used to store info about `earthquake` and `potensi`.
    """

    earthquake: Earthquake
    potensi: str