from typing import Dict
from elements.line.line import line_sql, BUSBAR_SQL
from elements.point_device.service.service import SERVICE_SQL
from elements.point_device.protection.fuse import FUSE_SQL
from elements.point_device.transformer import XFMR_SQL
from elements.point_device.service.light import LIGHT_SQL
from elements.point_device.openpoints import OPENPOINT_SQL
from elements.point_device.protection.protection import PROTECTION_SQL
from elements.station import STATION_SQL
from elements.elements import Element, VoltageClass


System = Dict[str, Element]


def load() -> System:
    """
    Loads elements from Postgres DB.  Returns system elements as a dictionary searchable by guid.
    """
    system = {}

    return System(
        protection=protection,
        lights=lights,
        fuses=fuses,
        substation_transformers=sub_xfmrs,
        transformers=dist_xfmrs,
        openpoints=openpoints,
        services=services,
        primary=priugs + priohs + busbars,
        secondary=secugs + secohs,
        stations=stations,
    )

