import unittest
from fontParts.base import FontPartsError


class TestAnchor(unittest.TestCase):

    def getAnchor_generic(self):
        anchor, unrequested = self.objectGenerator("anchor")
        anchor.name = None
        anchor.x = 1
        anchor.y = 2
        anchor.color = None
        return anchor, unrequested

    # --------------
    # Identification
    # ---------------

    def getAnchor_identification(self):
        anchor, unrequested = self.getAnchor_generic()
        anchor.name = "Anchor Attribute Test"
        return anchor, unrequested

    def test_name(self):
        anchor, unrequested = self.getAnchor_identification()
        # get
        self.assertEqual(
            anchor.name,
            "Anchor Attribute Test"
        )
        # set: valid
        anchor.name = u"foo"
        self.assertEqual(
            anchor.name,
            u"foo"
        )
        anchor.name = None
        self.assertIsNone(
            anchor.name
        )
        # set: invalid
        with self.assertRaises(FontPartsError):
            anchor.name = 123
