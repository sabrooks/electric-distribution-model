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


def connect(
    substation_transformers: List[Transformer],
    transformers: List[Transformer],
    secondary: List[Secondary],
    openpoints: List[OpenPoint],
    protection: List[Protection],
    fuses: List[Fuse],
    primary: List[Line],
    services: List[Service],
    lights=List[Light],
    stations=List[Station],
) -> nx.DiGraph:
    # Builds a directed graph by breadth first search starting at TP10-30 and TP-31

    # Assumes - No colocated openpoints, protection, fuses
    # Added enabled - if false do not make connections

    G = nx.DiGraph()

    # {Guid: Element.....}
    elements: Dict[str, Element] = {
        element.guid: element
        for element in substation_transformers
        + transformers
        + secondary
        + openpoints
        + protection
        + fuses
        + primary
        + services
        + lights
        + stations
    }

    def find_children(parent: Element):
        #
        children = parent.get_children(
            substation_transformers,
            transformers,
            secondary,
            openpoints,
            protection,
            fuses,
            primary,
            services,
            lights,
            stations,
        )
        for child_guid in children:
            G.add_edge(parent.guid, child_guid)
            child = elements.get(child_guid)
            find_children(child)

    for start in [
        "{C46A6964-A80C-4770-AF62-F357F937E32C}",
        "{ACB2DB69-0435-4438-B651-113D23D25015}",
    ]:
        start_element = elements.pop(start)
        find_children(start_element)

    return G
