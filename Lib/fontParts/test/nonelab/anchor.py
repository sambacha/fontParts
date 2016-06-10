import unittest
import defcon
from fontParts.test.base.anchor import TestAnchor
from fontParts.test.nonelab.base import BaseTest


class TestNoneLabAnchor(BaseTest, TestAnchor, unittest.TestCase):

    def test_naked(self):
        caseObjects = self.getCaseObjects("Test Anchor 1")
        anchor = caseObjects["anchor"]
        self.assertIsInstance(
            anchor.naked(),
            defcon.Anchor
        )


if __name__ == "__main__":
    unittest.main()
