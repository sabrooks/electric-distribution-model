import unittest
from elements.line.line import Primary
from elements.point_device.openpoints import OpenPoint
from elements.point_device.protection.fuse import Fuse
from elements.point_device.protection.protection import Protection
from elements.point_device.service.service import Meter
from elements.point_device.transformer import Transformer
from utility import Phase

TEST_TX = Transformer.new(
    5252,
    "{10596386-2915-4983-B7C9-7022E973DAB2}",
    "B",
    {"type": "Point", "coordinates": [-122.613750856272, 47.3867416184875]},
    "2247726",
    "Single Phase Underground",
    25.0,
    "Shrubline",
    "Closed",
    "VN4",
)
TEST_FUSE = Fuse.new(
    195,
    "{F93CABDE-327F-4742-9AAF-19E73AD6335C}",
    {"type": "Point", "coordinates": [-132.649232211957, 46.2937869738138]},
    "5232575_1",
    "Overhead Expulsion",
    "40 A",
    "B",
    "Closed",
    "VN4",
)

METER_DETAILS = dict(
    meter_number="ABC1234",
    account="DEF7889",
    billing_route="NR3",
    serv_loc="0452760157008",
    billing_cycle="100  ",
    address="123 Any St",
    meter_model="I210 2S",
    account_type="RE",
    meter_type="2S 120/240V CL200 1PH CAT M1",
    current_class="CL200",
)

TEST_METER = Meter.new(
    14952,
    "{9003D2B4-551D-4F65-8285-8344B836EACE}",
    {"type": "Point", "coordinates": [-132.591119630628, 49.3092392396018]},
    "3822 56TH ST CT NW",
    "0157008",
    "C",
    METER_DETAILS.get("meter_number"),
    METER_DETAILS.get("meter_type"),
    "VN4",
)

PRIOH = Primary.new(
    27184,
    "{7435E8B9-5453-41BA-BEC1-6DFE482E8C55}",
    {
        "type": "LineString",
        "coordinates": [
            [-132.813933444659, 39.269741591484],
            [-132.813998925597, 39.2697310724818],
        ],
    },
    "A",
    "Unknown",
    "UNKUNK",
    "PriUG",
    "VN4",
)

TEST_OPENPOINT = OpenPoint.new(
    6,
    "{EF351215-09F4-43B9-A3F6-A9EFDFD48552}",
    {"type": "Point", "coordinates": [-132.554237587714, 39.2916152852508]},
    "6216350",
    "A",
    False,
    "123456",
)

TEST_PROTECTION = Protection.new(
    16643,
    "{66639AF3-B16D-4629-8F21-352E532C6188}",
    {"type": "Point", "coordinates": [-132.652359461986, 49.3320067454193]},
    "5021253",
    "Recloser",
    "ABC",
    "Open",
    "REC_",
    "VN4",
)


class TestTransformer(unittest.TestCase):
    def test_init(self):
        self.assertEqual(TEST_TX.phase, "B")
        self.assertEqual(TEST_TX.ratedkva, 25.0)
        self.assertTrue(TEST_TX.enabled)
        self.assertEqual(TEST_TX.feeder_id, "VN4")


class TestFuse(unittest.TestCase):
    def test_init(self):
        self.assertEqual(TEST_FUSE.fuse_type, "Overhead Expulsion")
        self.assertEqual(TEST_FUSE.feeder_id, "VN4")
        self.assertTrue(TEST_FUSE.enabled)


class TestMeter(unittest.TestCase):
    def test_init(self):
        self.assertEqual(TEST_METER.phase, Phase("B"))
        self.assertEqual(TEST_METER.meter_number, "ABC1234")
        self.assertEqual(TEST_METER.meter_type, "2S 120/240V CL200 1PH CAT M1")


class TestLine(unittest.TestCase):
    def test_init_prioh(self):
        self.assertEqual(PRIOH.guid, "{7435E8B9-5453-41BA-BEC1-6DFE482E8C55}")
        self.assertEqual(PRIOH.phase, Phase("A"))
        self.assertEqual(PRIOH.feeder_id, "VN4")


class TestOpenPoint(unittest.TestCase):
    def test_init(self):
        self.assertEqual(TEST_OPENPOINT.gridecode, "6216350")


class TestProtection(unittest.TestCase):
    def test_init(self):
        self.assertEqual(TEST_PROTECTION.feeder_id, "VN4")
        self.assertFalse(TEST_PROTECTION.enabled)
        self.assertEqual(TEST_PROTECTION.guid, "{66639AF3-B16D-4629-8F21-352E532C6188}")
