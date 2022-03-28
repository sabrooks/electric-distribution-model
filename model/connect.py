from typing import Deque, Dict
from elements.elements import Element
from elements.point_device.transformer import Transformer
from utility import Point
from collections import deque


def connect(system: Dict[str, Element]) -> None:

    frontier: Deque[Element] = deque(
        (element for element in system.values() if isinstance(element, Transformer)),
        None,
    )
    while frontier:
        parent = frontier.pop()
        children = [element for element in system.values() if element.geo == parent.geo]
        frontier.extend(children)
        for child in children:
            del system[child.guid]

