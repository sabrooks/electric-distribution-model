from dataclasses import dataclass
from typing import Dict

from utility import Phase, VoltageClass
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
        id: int,
        guid: str,
        geo: Dict,
        facility_id: str,
        subtype: str,
        phase: Phase,
        enabled: bool,
        prefix: str,
        feeder_id: str,
    ) -> "Protection":
        return Protection(
            id,
            guid,
            Phase(phase),
            geo.get("coordinates"),
            f"{prefix}{facility_id}",
            VoltageClass(1),
            enabled,
            feeder_id,
            facility_id,
            subtype,
        )


@dataclass
class ProtectionStatus:
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

