from typing import Dict, Optional
from dataclasses import dataclass
from elements.point_device.point_device import PointDevice
from utility import Phase, VoltageClass


@dataclass
class Fuse(PointDevice):
    gridcode: str
    max_current: Optional[int]
    fuse_type: str

    @staticmethod
    def new(
        id: int,
        guid: str,
        geo: Dict,
        facility_id: str,
        subtype_cd: str,
        current: str,
        phase: str,
        enabled: str,
        feeder_id: str,
    ) -> "Fuse":
        return Fuse(
            id=id,
            guid=guid,
            phase=Phase(phase),
            geo=geo.get("coordinates"),
            name=f"FUS_{facility_id}",
            voltage_class=VoltageClass(1),
            enabled=True if enabled == "Closed" else False,
            feeder_id=feeder_id,
            gridcode=facility_id,
            max_current=int(current.split(" ")[0]) if current != "Unknown" else None,
            fuse_type=subtype_cd,
        )


FUSE_SQL = """
    Select id
    ,globalid
    ,ST_AsGeoJSON(location)::json
    ,facilityid
    ,subtypecd
    ,maxcontinuouscurrent
    ,phasedesignation
    ,enabled
    ,feederid
    from data.fuse;
    """

