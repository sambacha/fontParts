import unittest
import warnings
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
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            anchor._generateIdentifier()
            assert len(w) == 1
            assert issubclass(w[-1].category, DeprecationWarning)
            assert "Anchor._generateIdentifier()" in str(w[-1].message)
        self.assertEqual(
            anchor._generateIdentifier(),
            anchor._getIdentifier()
        )

    def test_anchor_deprecated_generateIdentifer(self):
        anchor, _ = self.objectGenerator("anchor")
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            anchor.generateIdentifier()
            assert issubclass(w[-1].category, DeprecationWarning)
            assert "Anchor.generateIdentifier()" in str(w[-1].message)
        self.assertEqual(
            anchor.generateIdentifier(),
            anchor.getIdentifier()
        )

    def test_anchor_deprecated_getParent(self):
        glyph = self.getAnchor_index()
        anchor = glyph.anchors[0]
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            anchor.getParent()
            assert len(w) == 1
            assert issubclass(w[-1].category, DeprecationWarning)
            assert "Anchor.getParent()" in str(w[-1].message)
        self.assertEqual(
            anchor.getParent(),
            anchor.glyph
        )

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
