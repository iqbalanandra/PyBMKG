from dataclasses import dataclass

from .coordinate import Coordinate
from .enum import Type
from .name import Name

__all__ = ["Area"]


@dataclass(unsafe_hash=True, slots=True)
class Area:
    id: str
    coordinate: Coordinate
    type: Type
    region: str
    level: str
    description: str
    domain: str
    tags: str
    names: Name
