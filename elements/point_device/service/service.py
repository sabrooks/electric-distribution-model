from dataclasses import dataclass
from typing import Dict
from itertools import tee
from elements.elements import VoltageClass

from elements.point_device.point_device import PointDevice
from utility import Phase


@dataclass
class Meter(PointDevice):
    address: str
    account: str
    meter_number: str
    meter_type: str

    @staticmethod
    def new(
        id: int,
        guid: str,
        geo: Dict,
        address: str,
        account: str,
        phase: str,
        meter_number: str,
        meter_type: str,
        feeder_id: str,
    ) -> "Meter":
        return Meter(
            id=id,
            guid=guid,
            phase=Phase(phase),
            geo=geo.get("coordinates"),
            name=f"M{meter_number}",
            voltage_class=VoltageClass(2),
            enabled=True,
            feeder_id=feeder_id,
            address=address,
            account=account,
            meter_number=meter_number,
            meter_type=meter_type,
        )

