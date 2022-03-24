from dataclasses import dataclass
from typing import Dict
from elements.point_device.point_device import PointDevice
from utility import VoltageClass


@dataclass
class OpenPoint(PointDevice):
    gridecode: str

    @staticmethod
    def new(
        id: int, guid: str, geo: Dict, facility_id: str, phase: str, enabled: str
    ) -> "OpenPoint":
        return OpenPoint(
            id,
            guid,
            phase,
            geo.get("coordiantes"),
            f"OP_{facility_id}",
            VoltageClass(1),
            enabled,
            None,
        )
