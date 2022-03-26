from dataclasses import dataclass
from typing import Dict
from elements.point_device.point_device import PointDevice
from utility import Phase, VoltageClass


@dataclass
class OpenPoint(PointDevice):
    gridcode: str

    @staticmethod
    def new(
        id: int,
        guid: str,
        geo: Dict,
        facility_id: str,
        phase: str,
        enabled: str,
        gridcode: str,
    ) -> "OpenPoint":
        return OpenPoint(
            id=id,
            guid=guid,
            phase=Phase(phase),
            geo=geo.get("coordiantes"),
            name=f"OP_{facility_id}",
            voltage_class=VoltageClass(1),
            enabled=enabled,
            feeder_id=None,
            gridcode=gridcode,
        )
