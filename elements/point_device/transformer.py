from dataclasses import dataclass
from typing import Dict, Optional

from enum import Enum
from elements.elements import VoltageClass
from elements.point_device.point_device import PointDevice
from utility import Phase


class TransformerStyle(Enum):
    SHURBLINE = "Shrubline"


@dataclass
class Transformer(PointDevice):
    ratedkva: float
    style: TransformerStyle
    gridcode: str
    xfmr_type: str

    @staticmethod
    def new(
        id: int,
        guid: str,
        phase: str,
        geo: Dict,
        facility_id: str,
        subtype_cd: str,
        ratedkva: float,
        style: str,
        enabled: str,
        feeder_id: str,
    ) -> "Transformer":
        return Transformer(
            id=id,
            guid=guid,
            phase=Phase(phase),
            geo=geo.get("coordinates"),
            name=f"XMFR_{facility_id}",
            voltage_class=VoltageClass.Primary,
            enabled=True if enabled == "Closed" else False,
            feeder_id=feeder_id,
            ratedkva=ratedkva,
            style=TransformerStyle(style),
            gridcode=facility_id,
            xfmr_type=subtype_cd,
        )
