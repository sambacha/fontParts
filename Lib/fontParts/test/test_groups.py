import unittest
from fontParts.base import FontPartsError


class TestGroups(unittest.TestCase):

    def getGroups_generic(self):
        groups, unrequested = self.objectGenerator("groups")
        groups.update({
            "group 1" : ["A", "B", "C"],
            "group 2" : ["x", "y", "z"],
            "group 3" : []
        })
        return groups, unrequested

    # ---
    # len
    # ---

    def test_len(self):
        groups, unrequested = self.getGroups_generic()
        self.assertEqual(
            len(groups),
            3
        )
        groups.clear()
        self.assertEqual(
            len(groups),
            0
        )
