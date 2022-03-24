from dataclasses import dataclass
from typing import Dict
from elements.elements import VoltageClass, PointDevice


@dataclass
class Light(PointDevice):
    light_type: str

    def get_children(self, *kwargs):
        # Return empty list.  Lights don't have childern.
        return []

    def to_geojson(self) -> Dict:
        return {
            "type": "Feature",
            "geometry": self.geometry,
            "properties": {
                "feature_type": "Light",
                "id": self.id,
                "guid": self.guid,
                "name": self.name,
                "voltage_class": self.voltage_class.name,
                "phase": self.phase,
                "parent": self.parent,
            },
        }


LIGHT_SQL = """
    Select id
    ,globalid
    ,ST_AsGeoJSON(location)::json
    ,facilityid
    ,phasedesignation
    ,subtypecd
    ,enabled
    from data.streetlight;
    """
