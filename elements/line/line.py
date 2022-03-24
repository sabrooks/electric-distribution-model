from dataclasses import dataclass
from typing import Dict, List

from elements.elements import Element, VoltageClass
from utility import Phase, Point


@dataclass
class Line(Element):
    size: str
    size_type: str
    conductor_type: str

    @staticmethod
    def new(
        id: int,
        guid: str,
        geo: Dict,
        phase: Phase,
        size: str,
        size_type: str,
        prefix: str,
        voltage_class: VoltageClass,
        feeder_id: str,
    ) -> "Line":
        return Line(
            id=id,
            guid=guid,
            geo=geo,
            name=f"{prefix}_{id}",
            phase=Phase(phase),
            voltage_class=voltage_class,
            enabled=True,
            feeder_id=feeder_id,
            size=size,
            size_type=size_type,
            conductor_type=f"{size} {size_type}",
        )


@dataclass
class Primary(Line):
    @staticmethod
    def new(
        id: int,
        guid: str,
        geo: Dict,
        phase: Phase,
        size: str,
        size_type: str,
        prefix: str,
        feeder_id: str,
    ) -> "Primary":
        return Primary(
            id=id,
            guid=guid,
            geo=geo,
            name=f"{prefix}_{id}",
            phase=Phase(phase),
            voltage_class=VoltageClass(1),
            enabled=True,
            feeder_id=feeder_id,
            size=size,
            size_type=size_type,
            conductor_type=f"{size} {size_type}",
        )


@dataclass
class Secondary(Line):
    @staticmethod
    def new(
        id: int,
        guid: str,
        geo: Dict,
        phase: Phase,
        size: str,
        size_type: str,
        prefix: str,
        feeder_id: str,
    ) -> "Secondary":
        return Secondary(
            id=id,
            guid=guid,
            geo=geo,
            name=f"{prefix}_{id}",
            phase=Phase(phase),
            voltage_class=VoltageClass(2),
            enabled=True,
            feeder_id=feeder_id,
            size=size,
            size_type=size_type,
            conductor_type=f"{size} {size_type}",
        )


@dataclass
class Busbar(Primary):
    @staticmethod
    def new(
        id: int,
        guid: str,
        geo: Dict,
        phase: Phase,
        feeder_id: str,
    ) -> "Busbar":
        return Busbar(
            id=id,
            guid=guid,
            geo=geo,
            name=f"BUS_{id}",
            phase=Phase(phase),
            voltage_class=VoltageClass(1),
            enabled=True,
            feeder_id=feeder_id,
            size="BUS",
            size_type="BUSBAR",
            conductor_type="BUSBAR",
        )

