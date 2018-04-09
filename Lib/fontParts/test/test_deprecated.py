import unittest2 as unittest
from fontParts.base.deprecated import RemovedWarning


class TestNormalizers(unittest.TestCase):

    # ----
    # Font
    # ----

    def test_font_removed_getParent(self):
        font, _ = self.objectGenerator("font")
        with self.assertRaises(RemovedWarning):
            font.getParent()

    def test_font_removed_generateGlyph(self):
        font, _ = self.objectGenerator("font")
        with self.assertRaises(RemovedWarning):
            font.generateGlyph()

    def test_font_removed_compileGlyph(self):
        font, _ = self.objectGenerator("font")
        with self.assertRaises(RemovedWarning):
            font.compileGlyph()

    def test_font_removed_getGlyphNameToFileNameFunc(self):
        font, _ = self.objectGenerator("font")
        with self.assertRaises(RemovedWarning):
            font.getGlyphNameToFileNameFunc()

    # ------
    # Anchor
    # ------

    def getAnchor_index(self):
        glyph, _ = self.objectGenerator("glyph")
        glyph.appendAnchor("anchor 0", (0, 0))
        glyph.appendAnchor("anchor 1", (0, 0))
        glyph.appendAnchor("anchor 2", (0, 0))
        return glyph

    def test_anchor_deprecated__generateIdentifer(self):
        anchor, _ = self.objectGenerator("anchor")
        with self.assertWarnsRegex(DeprecationWarning, "Anchor._generateIdentifier()"):
            anchor._generateIdentifier()
        self.assertEqual(
            anchor._generateIdentifier(),
            anchor._getIdentifier()
        )

    def test_anchor_deprecated_generateIdentifer(self):
        anchor, _ = self.objectGenerator("anchor")
        with self.assertWarnsRegex(DeprecationWarning, "Anchor.generateIdentifier()"):
            anchor.generateIdentifier()
        self.assertEqual(
            anchor.generateIdentifier(),
            anchor.getIdentifier()
        )

    def test_anchor_deprecated_getParent(self):
        glyph = self.getAnchor_index()
        anchor = glyph.anchors[0]
        with self.assertWarnsRegex(DeprecationWarning, "Anchor.getParent()"):
            anchor.getParent()
        self.assertEqual(
            anchor.getParent(),
            anchor.glyph
        )

    def test_anchor_removed_setParent(self):
        glyph = self.getAnchor_index()
        anchor = glyph.anchors[0]
        with self.assertRaises(RemovedWarning):
            anchor.setParent(glyph)

    def test_anchor_removed_draw(self):
        glyph = self.getAnchor_index()
        pen = glyph.getPen()
        anchor = glyph.anchors[0]
        with self.assertRaises(RemovedWarning):
            anchor.draw(pen)

    def test_anchor_removed_drawPoints(self):
        glyph = self.getAnchor_index()
        pen = glyph.getPen()
        anchor = glyph.anchors[0]
        with self.assertRaises(RemovedWarning):
            anchor.drawPoints(pen)
