from apps.ad_hoc.dist_model_copy.elements.system import (
    get_system,
    get_down_line_meters,
    Protection,
    System,
    Element,
)
from apps.ad_hoc.dist_model_copy.elements.transformer import Transformer

system = get_system()

xfmrs = filter(lambda x: isinstance(x, Transformer), system.values())
pwr_xfmrs = filter(lambda x: x.xfmr_type == "Power Transformer", xfmrs)
for pwr_xfmr in pwr_xfmrs:
    meters = get_down_line_meters(pwr_xfmr)
    print(f"{pwr_xfmr}: meters = {len(meters)}")


# Corrections - Should be temporary
system["{5DF6F19F-6D2E-4652-868D-A1DCA53DBB60}"].feeder_id = "NR4"
system["{38CE6DBB-33F1-42A8-BE59-16921D7D9636}"].feeder_id = "NR3"
KNOWN_ISSUES = {
    "{7F7248E5-B473-4883-8A09-A99015AED122}",
    "{BBA718AD-23D9-4150-8C59-D2C248BCF8B2}",
    "{2AC0C37F-A823-42E9-8B1C-B6F7635A6B44}",
    "{A3E9DBFF-536F-4DF1-9FC4-62AF3D6A0857}",
    "{8FC03653-D7B9-476D-ABC7-B86B617CC7DB}",
    "{C01A06ED-A496-4522-837F-5A47D536AD3A}",
    "{8336AF5D-EB3A-47C6-BB0F-0D6EB921B028}",
    "{B1F9FFED-60A4-4AC7-8E86-2D591DF1E218}",
    "{243641CC-27FD-4FDF-90A5-A43A06B9E014}",
    "{4D1DCE4B-0671-4162-AE99-9A59F062B476}",
}


def validation(system: System) -> None:
    def check_children(element: Element, feeder: str):
        if feeder is None:
            if isinstance(element, Protection):
                if element.subtype == "Feeder Head":
                    feeder = element.feeder_id
        if feeder is not None and feeder != element.feeder_id and element.enabled:
            # Stop on known errors
            if element.guid in KNOWN_ISSUES:
                return
            raise ValueError(f"{element} on {feeder}: assigned to {element.feeder_id}")
        for child in element.children:
            check_children(child, feeder)

    xfmrs = filter(lambda x: isinstance(x, Transformer), system.values())
    pwr_xfmrs = filter(lambda x: x.xfmr_type == "Power Transformer", xfmrs)
    for pwr_xfmr in pwr_xfmrs:
        check_children(pwr_xfmr, None)


# TODO - PriUG_59321:{7F7248E5-B473-4883-8A09-A99015AED122} on NR3: assigned to NR1
# TODO - Write tracer - trace and element to the feeder head


def trace(element: Element):
    print(element)
    if not isinstance(element, Transformer) or element.xfmr_type != "Power Transformer":
        trace(element.parent)


mismatch = system.get("{2AC0C37F-A823-42E9-8B1C-B6F7635A6B44}")
trace(mismatch)
