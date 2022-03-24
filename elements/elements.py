from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Tuple


class VoltageClass(Enum):
    Transmission = 0
    Primary = 1
    Secondary = 2


Location = Tuple[float, float, VoltageClass]


@dataclass
class Element:
    id: int
    guid: str
    phase: str
    geo: List[List[float]]
    name: str
    voltage_class: VoltageClass
    enabled: bool
    feeder_id: Optional[str]


"""
        self.id: int = id
        self.guid: str = guid
        self.phase: str = phase
        self.geometry: Dict = geo
        self.name: str = name
        self.voltage_class: VoltageClass = voltage_class
        self.parent: Optional["Element"] = None
        self.children: List["Element"] = []
        self.enabled: bool = enabled
        self.feeder_id: str = feeder_id
"""


Connection = Tuple[str]
Network = List[Connection]  # [Parent GUID, Child GUID]
Elements = Dict[str, Element]
