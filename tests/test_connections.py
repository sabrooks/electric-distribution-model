from typing import Dict
import unittest
from elements.elements import Element
from elements.line.line import Secondary
from elements.point_device.openpoints import OpenPoint
from elements.point_device.protection.fuse import Fuse
from elements.point_device.protection.protection import Protection
from elements.point_device.service.service import Meter
from elements.point_device.transformer import Transformer
from utility import Phase

sec_1 = Secondary.new(
    1,
    "{7435E8B9-5453-41BA-BEC1-6DFE482E8C55}",
    {"type": "LineString", "coordinates": [[-130.0, 40.0], [-130.1, 40.1],],},
    "A",
    "350",
    "AC",
    "SecUG",
    "BN6",
)

sec_2 = Secondary.new(
    2,
    "{7435E8B9-5453-41BA-BEC1-6DFE482E8C52}",
    {"type": "LineString", "coordinates": [[-130.0, 40.0], [-130.2, 40.2],],},
    "A",
    "350",
    "AC",
    "SecUG",
    "BN6",
)


m_1 = Meter.new(
    11,
    "{9003D2B4-551D-4F65-8285-8344B836EACE}",
    {"type": "Point", "coordinates": [-130.1, 40.1]},
    "1111 56TH ST CT NW",
    "0157008",
    "A",
    1,
    "I210 2S",
    "BN4",
)

m_2 = Meter.new(
    22,
    "{9003D2B4-551D-4F65-8285-8344B836EACE}",
    {"type": "Point", "coordinates": [-130.2, 40.2]},
    "2222 56TH ST CT NW",
    "98767",
    "A",
    1,
    "I210 2S",
    "BN4",
)

tx = Transformer.new(
    5252,
    "{10596386-2915-4983-B7C9-7022E973DAB2}",
    "A",
    {"type": "Point", "coordinates": [-130.0, 40.0]},
    "2247726",
    "Single Phase Underground",
    25.0,
    "Shrubline",
    "Closed",
    "BN4",
)

system: Dict[str, Element] = {el.guid: el for el in [sec_1, sec_2, m_1, m_2, tx]}
