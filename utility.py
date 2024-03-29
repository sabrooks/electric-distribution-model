from enum import Enum
from typing import List, Tuple

from elements.elements import Element


class Phase(Enum):
    A = "A"
    B = "B"
    C = "C"
    AB = "AB"
    AC = "AC"
    BC = "BC"
    ABC = "ABC"


class VoltageClass(Enum):
    Transmission = 0
    Primary = 1
    Secondary = 2


Point = Tuple[float, float]
Line = List[Point]
System = {str, Element}
