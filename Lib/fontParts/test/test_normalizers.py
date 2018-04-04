import unittest
from fontTools.misc.py23 import unicode, basestring
from fontParts.base import normalizers


class TestNormalizers(unittest.TestCase):

    # ----
    # Font
    # ----

    def getFont_layers(self):
        font, _ = self.objectGenerator("font")
        for name in ["A", "B", "C", "D", "E"]:
            font.newLayer(name)
        return font

    def getFont_glyphs(self):
        font, _ = self.objectGenerator("font")
        for name in ["A", "B", "C", "D", "E"]:
            font.newGlyph(name)
        return font

    # normalizeFileFormatVersion

    def test_normalizeFileFormatVersion_int(self):
        result = normalizers.normalizeFileFormatVersion(3)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 3.0)

    def test_normalizeFileFormatVersion_float(self):
        result = normalizers.normalizeFileFormatVersion(3.0)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 3.0)

    def test_normalizeFileFormatVersion_invalid(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeFileFormatVersion("3")

    # normalizeLayerOrder

    def test_normalizeLayerOrder_valid(self):
        font = self.getFont_layers()
        result = normalizers.normalizeLayerOrder(["A", "B", "C", "D", "E"], font)
        self.assertIsInstance(result, tuple)
        for i in result:
            self.assertIsInstance(i, unicode)
        self.assertEqual(result, (u"A", u"B", u"C", u"D", u"E"))

    def test_normalizeLayerOrder_validTuple(self):
        font = self.getFont_layers()
        result = normalizers.normalizeLayerOrder(tuple(["A", "B", "C", "D", "E"]), font)
        self.assertEqual(result, (u"A", u"B", u"C", u"D", u"E"))

    def test_normalizeLayerOrder_notList(self):
        font = self.getFont_layers()
        with self.assertRaises(TypeError):
            normalizers.normalizeLayerOrder("A B C D E", font)

    def test_normalizeGlyphOrder_invalidMember(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeGlyphOrder(["A", "B", "C", "D", 2])

    def test_normalizeLayerOrder_notInFont(self):
        font = self.getFont_layers()
        with self.assertRaises(ValueError):
            normalizers.normalizeLayerOrder(["A", "B", "C", "D", "E", "X"], font)

    def test_normalizeLayerOrder_duplicate(self):
        font = self.getFont_layers()
        with self.assertRaises(ValueError):
            normalizers.normalizeLayerOrder(["A", "B", "C", "C", "D", "E"], font)

    # normalizeDefaultLayerName

    def test_normalizeDefaultLayerName_valid(self):
        font = self.getFont_layers()
        result = normalizers.normalizeDefaultLayerName("B", font)
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"B")

    def test_normalizeDefaultLayerName_notValidLayerName(self):
        font = self.getFont_layers()
        with self.assertRaises(TypeError):
            normalizers.normalizeDefaultLayerName(1, font)

    def test_normalizeDefaultLayerName_notInFont(self):
        font = self.getFont_layers()
        with self.assertRaises(ValueError):
            normalizers.normalizeDefaultLayerName("X", font)

    # normalizeGlyphOrder

    def test_normalizeGlyphOrder_valid(self):
        result = normalizers.normalizeGlyphOrder(["A", "B", "C", "D", "E"])
        self.assertIsInstance(result, tuple)
        for i in result:
            self.assertIsInstance(i, unicode)
        self.assertEqual(result, (u"A", u"B", u"C", u"D", u"E"))

    def test_normalizeGlyphOrder_validTuple(self):
        result = normalizers.normalizeGlyphOrder(tuple(["A", "B", "C", "D", "E"]))
        self.assertEqual(result, (u"A", u"B", u"C", u"D", u"E"))

    def test_normalizeGlyphOrder_notList(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeGlyphOrder("A B C D E")

    def test_normalizeGlyphOrder_invalidMember(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeGlyphOrder(["A", "B", "C", "D", 2])

    def test_normalizeGlyphOrder_duplicate(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeGlyphOrder(["A", "B", "C", "C", "D", "E"])

