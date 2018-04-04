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

    # -------
    # Kerning
    # -------

    # normalizeKerningKey

    def test_normalizeKerningKey_validGlyphs(self):
        result = normalizers.normalizeKerningKey(("A", "B"))
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, (u"A", u"B"))

    def test_normalizeKerningKey_validGroups(self):
        result = normalizers.normalizeKerningKey(("public.kern1.A", "public.kern2.B"))
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, (u"public.kern1.A", u"public.kern2.B"))

    def test_normalizeKerningKey_validList(self):
        result = normalizers.normalizeKerningKey(["A", "B"])
        self.assertEqual(result, (u"A", u"B"))

    def test_normalizeKerningKey_notTuple(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeKerningKey("A B")

    def test_normalizeKerningKey_notEnoughMembers(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeKerningKey(("A",))

    def test_normalizeKerningKey_tooManyMembers(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeKerningKey(("A", "B", "C"))

    def test_normalizeKerningKey_memberNotString(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeKerningKey(("A", 2))
        with self.assertRaises(TypeError):
            normalizers.normalizeKerningKey((1, "B"))

    def test_normalizeKerningKey_memberNotLongEnough(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeKerningKey(("A", ""))
        with self.assertRaises(ValueError):
            normalizers.normalizeKerningKey(("", "B"))

    def test_normalizeKerningKey_invalidSide1Group(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeKerningKey(("public.kern2.A", "B"))

    def test_normalizeKerningKey_invalidSide2Group(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeKerningKey(("A", "public.kern1.B"))

    # normalizeKerningValue

    def test_normalizeKerningValue_zero(self):
        result = normalizers.normalizeKerningValue(0)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)

    def test_normalizeKerningValue_positiveInt(self):
        result = normalizers.normalizeKerningValue(1)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)

    def test_normalizeKerningValue_negativeInt(self):
        result = normalizers.normalizeKerningValue(-1)
        self.assertIsInstance(result, int)
        self.assertEqual(result, -1)

    def test_normalizeKerningValue_positiveFloat(self):
        result = normalizers.normalizeKerningValue(1.0)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 1.0)

    def test_normalizeKerningValue_negativeFloat(self):
        result = normalizers.normalizeKerningValue(-1.0)
        self.assertIsInstance(result, float)
        self.assertEqual(result, -1.0)

    def test_normalizeKerningValue_notNumber(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeKerningValue("1")

    # ------
    # Groups
    # ------

    # normalizeGroupKey

    def test_normalizeGroupKey_valid(self):
        result = normalizers.normalizeGroupKey("A")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"A")

    def test_normalizeGroupKey_notString(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeGroupKey(1)

    def test_normalizeGroupKey_notLongEnough(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeGroupKey("")

    # normalizeGroupValue

    def test_normalizeGroupValue_valid(self):
        result = normalizers.normalizeGroupValue(["A", "B", "C"])
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, (u"A", u"B", u"C"))

    def test_normalizeGroupValue_validTuple(self):
        result = normalizers.normalizeGroupValue(("A", "B", "C"))
        self.assertEqual(result, (u"A", u"B", u"C"))

    def test_normalizeGroupValue_validEmpty(self):
        result = normalizers.normalizeGroupValue([])
        self.assertEqual(result, (,))

    def test_normalizeGroupValue_notList(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeGroupValue("A B C")

    def test_normalizeGroupValue_invalidMember(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeGroupValue(["A", "B", 3])

    # --------
    # Features
    # --------

    # normalizeFeatureText

    def test_normalizeFeatureText_valid(self):
        result = normalizers.normalizeFeatureText("test")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"test")

    def test_normalizeFeatureText_notString(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeFeatureText(123)

    # ---
    # Lib
    # ---

    # normalizeLibKey

    def test_normalizeLibKey_valid(self):
        result = normalizers.normalizeLibKey("test")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"test")

    def test_normalizeLibKey_notString(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeLibKey(123)

    def test_normalizeLibKey_emptyString(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeLibKey("")

    # normalizeLibValue

    def test_normalizeLibValue_invalidNone(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeLibValue(None)

    def test_normalizeLibValue_validString(self):
        result = normalizers.normalizeLibValue("test")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"test")

    def test_normalizeLibValue_validInt(self):
        result = normalizers.normalizeLibValue(1)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)

    def test_normalizeLibValue_validFloat(self):
        result = normalizers.normalizeLibValue(1.0)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 1.0)

    def test_normalizeLibValue_validTuple(self):
        result = normalizers.normalizeLibValue(("A", "B"))
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, (u"A", u"B"))

    def test_normalizeLibValue_invalidTupleMember(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeLibValue((1, None))

    def test_normalizeLibValue_validList(self):
        result = normalizers.normalizeLibValue(["A", "B"])
        self.assertIsInstance(result, list)
        self.assertEqual(result, [u"A", u"B"])

    def test_normalizeLibValue_invalidListMember(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeLibValue([1, None])

    def test_normalizeLibValue_validDict(self):
        result = normalizers.normalizeLibValue({"A" : 1, "B" : 2})
        self.assertIsInstance(result, dict)
        self.assertEqual(result, {u"A" : 1, u"B" : 2})

    def test_normalizeLibValue_invalidDictKey(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeLibValue({1 : 1, "B" : 2})

    def test_normalizeLibValue_invalidDictValue(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeLibValue({"A" : None, "B" : 2})

