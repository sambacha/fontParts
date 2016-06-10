from fontParts.base import FontPartsError
from fontParts.test.support import BaseTestCase, registerTestData


class TestAnchor(BaseTestCase):

    testData = {}

    registerTestData(
        testData,
        "Generic Anchor",
        """
        + object: Anchor = anchor
        anchor.name = None
        anchor.x = 1
        anchor.y = 2
        anchor.color = None
        """
    )

    # --------------
    # Identification
    # ---------------

    registerTestData(
        testData,
        "Test Anchor 1",
        """
        + base: Generic Anchor
        anchor.name = "testAnchor1"
        """
    )

    def test_name(self):
        testObjects = self.getTestObjects("Test Anchor 1")
        anchor = testObjects["anchor"]
        # get
        self.assertEqual(
            anchor.name,
            "testAnchor1"
        )
        # set: valid
        anchor.name = u"foo"
        self.assertEqual(
            anchor.name,
            u"foo"
        )
        # set: invalid
        with self.assertRaises(FontPartsError):
            anchor.name = 123
