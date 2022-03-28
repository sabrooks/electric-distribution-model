from typing import List, Dict
import networkx as nx
from elements.line.line import Line, Secondary
from elements.point_device.service.service import Service
from elements.point_device.protection.fuse import Fuse
from elements.point_device.transformer import Transformer
from elements.point_device.openpoints import OpenPoint
from elements.point_device.service.light import Light
from elements.point_device.protection.protection import Protection
from elements.station import Station
from elements.elements import Element

