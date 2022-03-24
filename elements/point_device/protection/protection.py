from dataclasses import dataclass
from typing import Dict, NamedTuple

from utility import VoltageClass
from ..point_device import PointDevice
from datetime import datetime
from enum import Enum
import re

STATION_NAME = r"^[\w\_]+_(?P<gridcode>\d{7})$"

assert re.match(STATION_NAME, "REC_SUB_GIG_HARBOR_1234567") is not None


class Status(Enum):
    OPEN = 0
    CLOSED = 1


@dataclass
class Protection(PointDevice):
    gridcode: str
    subtype: str

    @staticmethod
    def new(
        id, guid, geo, facility_id, subtype, phase, enabled, prefix, feeder_id
    ) -> "Protection":
        return Protection(
            id,
            guid,
            phase,
            geo,
            f"{prefix}{facility_id}",
            VoltageClass(1),
            enabled,
            feeder_id,
        )


class ProtectionStatus(NamedTuple):
    station_name: str
    point_name: str
    point_desc: str
    station_desc: str
    update_time: datetime
    status: Status
    gridcode: str

    @staticmethod
    def new(
        station_name: str,
        point_name: str,
        point_desc: str,
        station_desc: str,
        update_time: datetime,
        value: int,
    ) -> "ProtectionStatus":
        status = Status(value)
        if m := re.search(STATION_NAME, station_name):
            gridcode = m.group("gridcode")
        else:
            gridcode = None
        return ProtectionStatus(
            station_name,
            point_name,
            point_desc,
            station_desc,
            update_time,
            status,
            gridcode,
        )


PROTECTION_SQL = """
    Select id
    ,globalid
    ,ST_AsGeoJSON(location)::json
    ,facilityid
    ,subtypecd
    ,phasedesignation
    ,enabled
    ,prefix
    ,feederid
    from data.dynamicprotectivedevice;
"""

SWITCH_SQL = """
    Select id
    ,globalid
    ,ST_AsGeoJSON(location)::json
    ,facilityid
    ,subtypecd
    ,phasedesignation
    ,enabled
    ,feederid
    from data.rw_switch;
"""

PROTECTION_STATUS = """
SELECT
      [STATIONPOINTS].NAME as Station
      ,statupoints.NAME as Point
      ,statupoints.[DESC] as PointDescription
      ,[STATIONPOINTS].[DESC] as StationDescription
      ,[UPDATETIME]
      ,[VALUE]
    FROM (Select *
      FROM [ScadaDB].[dbo].[STATUSPOINTS]
      Where [NAME] = '52A'
  ) as statupoints
  Inner Join [ScadaDB].[dbo].[STATIONPOINTS]
  ON statupoints.STATIONPID = STATIONPOINTS.PKEY
  """


def get_protection() -> Dict[str, Protection]:
    with iqgeo_engine.begin() as conn:
        raw = conn.execute(PROTECTION_SQL)
        protection = {
            guid: Protection(
                id, guid, geo, facility_id, subtype, phase, enabled, prefix, feeder_id
            )
            for id, guid, geo, facility_id, subtype, phase, enabled, prefix, feeder_id in raw
        }

    with iqgeo_engine.begin() as conn:
        raw = conn.execute(SWITCH_SQL)
        switches = {
            guid: Protection(
                id, guid, geo, facility_id, subtype, phase, enabled, "SW_", feeder_id
            )
            for id, guid, geo, facility_id, subtype, phase, enabled, feeder_id in raw
        }
    return {**protection, **switches}


def get_protection_status() -> Dict[str, ProtectionStatus]:
    with mssql_engine.begin() as conn:
        raw = conn.execute(PROTECTION_STATUS)
        statuses = (
            ProtectionStatus.new(
                station, point, point_desc, station_desc, update, value
            )
            for station, point, point_desc, station_desc, update, value in raw
        )
        return {s.gridcode: s for s in statuses}


TEST_PROTECTION = Protection(
    16643,
    "{66639AF3-B16D-4629-8F21-352E532C6188}",
    {"type": "Point", "coordinates": [-122.652359461986, 47.3320067454193]},
    "5021253",
    "Recloser",
    "ABC",
    "Open",
    "REC_",
    "VN4",
)

assert TEST_PROTECTION.locations == [
    (-122.652359461986, 47.3320067454193, VoltageClass(1))
]
assert TEST_PROTECTION.feeder_id == "VN4"
