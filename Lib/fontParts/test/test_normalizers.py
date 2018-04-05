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
        self.assertEqual(result, tuple())

    def test_normalizeGroupValue_notList(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeGroupValue("A B C")

    def test_normalizeGroupValue_invalidMember(self):
        with self.assertRaises(TypeError):
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
        with self.assertRaises(TypeError):
            normalizers.normalizeLibValue({1 : 1, "B" : 2})

    def test_normalizeLibValue_invalidDictValue(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeLibValue({"A" : None, "B" : 2})

    # -----
    # Layer
    # -----

    # normalizeLayer

    def test_normalizeLayer_valid(self):
        from fontParts.base.layer import BaseLayer
        layer, _ = self.objectGenerator("layer")
        result = normalizers.normalizeLayer(layer)
        self.assertIsInstance(result, BaseLayer)
        self.assertEqual(result, layer)

    def test_normalizeLayer_notLayer(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeLayer(123)

    # normalizeLayerName

    def test_normalizeLayerName_valid(self):
        result = normalizers.normalizeLayerName("A")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"A")

    def test_normalizeLayerName_notString(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeLayerName(123)

    def test_normalizeLayerName_notLongEnough(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeLayerName("")

    # -----
    # Glyph
    # -----

    # normalizeGlyph

    def test_normalizeGlyph_valid(self):
        from fontParts.base.glyph import BaseGlyph
        glyph, _ = self.objectGenerator("glyph")
        result = normalizers.normalizeGlyph(glyph)
        self.assertIsInstance(result, BaseGlyph)
        self.assertEqual(result, glyph)

    def test_normalizeGlyph_notGlyph(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeGlyph(123)

    # normalizeGlyphName

    def test_normalizeGlyphName_valid(self):
        result = normalizers.normalizeGlyphName("A")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"A")

    def test_normalizeGlyphName_notString(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeGlyphName(123)

    def test_normalizeGlyphName_notLongEnough(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeGlyphName("")

    # normalizeGlyphUnicodes

    def test_normalizeGlyphUnicodes_valid(self):
        result = normalizers.normalizeGlyphUnicodes([1, 2, 3])
        self.assertIsInstance(result, tuple)
        self.assertEqual(result, (1, 2, 3))

    def test_normalizeGlyphUnicodes_validTuple(self):
        result = normalizers.normalizeGlyphUnicodes(tuple([1, 2, 3]))
        self.assertEqual(result, (1, 2, 3))

    def test_normalizeGlyphUnicodes_invalidDuplicateMembers(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeGlyphUnicodes([1, 2, 3, 2])

    def test_normalizeGlyphUnicodes_invalidMember(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeGlyphUnicodes([1, 2, "xyz"])

    # normalizeGlyphUnicode

    def test_normalizeGlyphUnicode_validInt(self):
        result = normalizers.normalizeGlyphUnicode(1)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)

    def test_normalizeGlyphUnicode_validHex(self):
        result = normalizers.normalizeGlyphUnicode("0001")
        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)

    def test_normalizeGlyphUnicode_validRangeMinimum(self):
        result = normalizers.normalizeGlyphUnicode(0)
        self.assertEqual(result, 0)

    def test_normalizeGlyphUnicode_validRangeMaximum(self):
        result = normalizers.normalizeGlyphUnicode(1114111)
        self.assertEqual(result, 1114111)

    def test_normalizeGlyphUnicode_invalidFloat(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeGlyphUnicode(1.0)

    def test_normalizeGlyphUnicode_invalidString(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeGlyphUnicode("xyz")

    def test_normalizeGlyphUnicode_invalidRangeMinimum(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeGlyphUnicode(-1)

    def test_normalizeGlyphUnicode_invalidRangeMaximum(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeGlyphUnicode(1114112)

    # normalizeGlyphBottomMargin

    def test_normalizeGlyphBottomMargin_zero(self):
        result = normalizers.normalizeGlyphBottomMargin(0)
        self.assertEqual(result, 0)

    def test_normalizeGlyphBottomMargin_positiveInt(self):
        result = normalizers.normalizeGlyphBottomMargin(1)
        self.assertEqual(result, 1)

    def test_normalizeGlyphBottomMargin_negativeInt(self):
        result = normalizers.normalizeGlyphBottomMargin(-1)
        self.assertEqual(result, -1)

    def test_normalizeGlyphBottomMargin_positiveFloat(self):
        result = normalizers.normalizeGlyphBottomMargin(1.01)
        self.assertEqual(result, 1.01)

    def test_normalizeGlyphBottomMargin_negativeFloat(self):
        result = normalizers.normalizeGlyphBottomMargin(-1.01)
        self.assertEqual(result, -1.01)

    def test_normalizeGlyphBottomMargin_notNumber(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeGlyphBottomMargin("1")

    # normalizeGlyphLeftMargin

    def test_normalizeGlyphLeftMargin_zero(self):
        result = normalizers.normalizeGlyphLeftMargin(0)
        self.assertEqual(result, 0)

    def test_normalizeGlyphLeftMargin_positiveInt(self):
        result = normalizers.normalizeGlyphLeftMargin(1)
        self.assertEqual(result, 1)

    def test_normalizeGlyphLeftMargin_negativeInt(self):
        result = normalizers.normalizeGlyphLeftMargin(-1)
        self.assertEqual(result, -1)

    def test_normalizeGlyphLeftMargin_positiveFloat(self):
        result = normalizers.normalizeGlyphLeftMargin(1.01)
        self.assertEqual(result, 1.01)

    def test_normalizeGlyphLeftMargin_negativeFloat(self):
        result = normalizers.normalizeGlyphLeftMargin(-1.01)
        self.assertEqual(result, -1.01)

    def test_normalizeGlyphLeftMargin_notNumber(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeGlyphLeftMargin("1")

    # normalizeGlyphRightMargin

    def test_normalizeGlyphRightMargin_zero(self):
        result = normalizers.normalizeGlyphRightMargin(0)
        self.assertEqual(result, 0)

    def test_normalizeGlyphRightMargin_positiveInt(self):
        result = normalizers.normalizeGlyphRightMargin(1)
        self.assertEqual(result, 1)

    def test_normalizeGlyphRightMargin_negativeInt(self):
        result = normalizers.normalizeGlyphRightMargin(-1)
        self.assertEqual(result, -1)

    def test_normalizeGlyphRightMargin_positiveFloat(self):
        result = normalizers.normalizeGlyphRightMargin(1.01)
        self.assertEqual(result, 1.01)

    def test_normalizeGlyphRightMargin_negativeFloat(self):
        result = normalizers.normalizeGlyphRightMargin(-1.01)
        self.assertEqual(result, -1.01)

    def test_normalizeGlyphRightMargin_notNumber(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeGlyphRightMargin("1")

    # normalizeGlyphHeight

    def test_normalizeGlyphHeight_zero(self):
        result = normalizers.normalizeGlyphHeight(0)
        self.assertEqual(result, 0)

    def test_normalizeGlyphHeight_positiveInt(self):
        result = normalizers.normalizeGlyphHeight(1)
        self.assertEqual(result, 1)

    def test_normalizeGlyphHeight_negativeInt(self):
        result = normalizers.normalizeGlyphHeight(-1)
        self.assertEqual(result, -1)

    def test_normalizeGlyphHeight_positiveFloat(self):
        result = normalizers.normalizeGlyphHeight(1.01)
        self.assertEqual(result, 1.01)

    def test_normalizeGlyphHeight_negativeFloat(self):
        result = normalizers.normalizeGlyphHeight(-1.01)
        self.assertEqual(result, -1.01)

    def test_normalizeGlyphHeight_notNumber(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeGlyphHeight("1")

    # normalizeGlyphBottomMargin

    def test_normalizeGlyphBottomMargin_zero(self):
        result = normalizers.normalizeGlyphBottomMargin(0)
        self.assertEqual(result, 0)

    def test_normalizeGlyphBottomMargin_positiveInt(self):
        result = normalizers.normalizeGlyphBottomMargin(1)
        self.assertEqual(result, 1)

    def test_normalizeGlyphBottomMargin_negativeInt(self):
        result = normalizers.normalizeGlyphBottomMargin(-1)
        self.assertEqual(result, -1)

    def test_normalizeGlyphBottomMargin_positiveFloat(self):
        result = normalizers.normalizeGlyphBottomMargin(1.01)
        self.assertEqual(result, 1.01)

    def test_normalizeGlyphBottomMargin_negativeFloat(self):
        result = normalizers.normalizeGlyphBottomMargin(-1.01)
        self.assertEqual(result, -1.01)

    def test_normalizeGlyphBottomMargin_notNumber(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeGlyphBottomMargin("1")

    # normalizeGlyphTopMargin

    def test_normalizeGlyphTopMargin_zero(self):
        result = normalizers.normalizeGlyphTopMargin(0)
        self.assertEqual(result, 0)

    def test_normalizeGlyphTopMargin_positiveInt(self):
        result = normalizers.normalizeGlyphTopMargin(1)
        self.assertEqual(result, 1)

    def test_normalizeGlyphTopMargin_negativeInt(self):
        result = normalizers.normalizeGlyphTopMargin(-1)
        self.assertEqual(result, -1)

    def test_normalizeGlyphTopMargin_positiveFloat(self):
        result = normalizers.normalizeGlyphTopMargin(1.01)
        self.assertEqual(result, 1.01)

    def test_normalizeGlyphTopMargin_negativeFloat(self):
        result = normalizers.normalizeGlyphTopMargin(-1.01)
        self.assertEqual(result, -1.01)

    def test_normalizeGlyphTopMargin_notNumber(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeGlyphTopMargin("1")

    # -------
    # Contour
    # -------

    # normalizeContour

    def test_normalizeContour_valid(self):
        from fontParts.base.contour import BaseContour
        contour, _ = self.objectGenerator("contour")
        result = normalizers.normalizeContour(contour)
        self.assertIsInstance(result, BaseContour)
        self.assertEqual(result, contour)

    def test_normalizeContour_notContour(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeContour(123)

    # normalizeContourIndex

    def test_normalizeContourIndex_zero(self):
        result = normalizers.normalizeContourIndex(0)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)

    def test_normalizeContourIndex_positiveInt(self):
        result = normalizers.normalizeContourIndex(1)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 1)

    def test_normalizeContourIndex_negativeInt(self):
        result = normalizers.normalizeContourIndex(-1)
        self.assertIsInstance(result, int)
        self.assertEqual(result, -1)

    def test_normalizeContourIndex_notInt(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeContourIndex(1.0)

    # -----
    # Point
    # -----

    # normalizePoint

    def test_normalizePoint_valid(self):
        from fontParts.base.point import BasePoint
        point, _ = self.objectGenerator("point")
        result = normalizers.normalizePoint(point)
        self.assertIsInstance(result, BasePoint)
        self.assertEqual(result, point)

    def test_normalizePoint_notPoint(self):
        with self.assertRaises(TypeError):
            normalizers.normalizePoint(123)

    # normalizePointType

    def test_normalizePointType_move(self):
        result = normalizers.normalizePointType("move")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"move")

    def test_normalizePointType_Move(self):
        with self.assertRaises(ValueError):
            normalizers.normalizePointType("Move")

    def test_normalizePointType_MOVE(self):
        with self.assertRaises(ValueError):
            normalizers.normalizePointType("MOVE")

    def test_normalizePointType_line(self):
        result = normalizers.normalizePointType("line")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"line")

    def test_normalizePointType_Line(self):
        with self.assertRaises(ValueError):
            normalizers.normalizePointType("Line")

    def test_normalizePointType_LINE(self):
        with self.assertRaises(ValueError):
            normalizers.normalizePointType("LINE")

    def test_normalizePointType_offcurve(self):
        result = normalizers.normalizePointType("offcurve")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"offcurve")

    def test_normalizePointType_OffCurve(self):
        with self.assertRaises(ValueError):
            normalizers.normalizePointType("OffCurve")

    def test_normalizePointType_OFFCURVE(self):
        with self.assertRaises(ValueError):
            normalizers.normalizePointType("OFFCURVE")

    def test_normalizePointType_curve(self):
        result = normalizers.normalizePointType("curve")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"curve")

    def test_normalizePointType_OffCurve(self):
        with self.assertRaises(ValueError):
            normalizers.normalizePointType("Curve")

    def test_normalizePointType_OFFCURVE(self):
        with self.assertRaises(ValueError):
            normalizers.normalizePointType("CURVE")

    def test_normalizePointType_qcurve(self):
        result = normalizers.normalizePointType("qcurve")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"qcurve")

    def test_normalizePointType_QOffCurve(self):
        with self.assertRaises(ValueError):
            normalizers.normalizePointType("QCurve")

    def test_normalizePointType_QOFFCURVE(self):
        with self.assertRaises(ValueError):
            normalizers.normalizePointType("QCURVE")

    def test_normalizePointType_unknown(self):
        with self.assertRaises(ValueError):
            normalizers.normalizePointType("unknonwn")

    def test_normalizePointType_notString(self):
        with self.assertRaises(TypeError):
            normalizers.normalizePointType(123)

    # normalizePointName

    def test_normalizePointName_valid(self):
        result = normalizers.normalizePointName("A")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"A")

    def test_normalizePointName_notString(self):
        with self.assertRaises(TypeError):
            normalizers.normalizePointName(123)

    def test_normalizePointName_notLongEnough(self):
        with self.assertRaises(ValueError):
            normalizers.normalizePointName("")

    # -------
    # Segment
    # -------

    # normalizeSegment

    def test_normalizeSegment_valid(self):
        from fontParts.base.segment import BaseSegment
        segment, _ = self.objectGenerator("segment")
        result = normalizers.normalizeSegment(segment)
        self.assertIsInstance(result, BaseSegment)
        self.assertEqual(result, segment)

    def test_normalizePoint_notContour(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeSegment(123)

    # normalizeSegmentType

    def test_normalizeSegmentType_move(self):
        result = normalizers.normalizeSegmentType("move")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"move")

    def test_normalizeSegmentType_Move(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeSegmentType("Move")

    def test_normalizeSegmentType_MOVE(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeSegmentType("MOVE")

    def test_normalizeSegmentType_line(self):
        result = normalizers.normalizeSegmentType("line")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"line")

    def test_normalizeSegmentType_Line(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeSegmentType("Line")

    def test_normalizeSegmentType_LINE(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeSegmentType("LINE")

    def test_normalizeSegmentType_curve(self):
        result = normalizers.normalizeSegmentType("curve")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"curve")

    def test_normalizeSegmentType_OffCurve(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeSegmentType("Curve")

    def test_normalizeSegmentType_OFFCURVE(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeSegmentType("CURVE")

    def test_normalizeSegmentType_qcurve(self):
        result = normalizers.normalizeSegmentType("qcurve")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"qcurve")

    def test_normalizeSegmentType_QOffCurve(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeSegmentType("QCurve")

    def test_normalizeSegmentType_QOFFCURVE(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeSegmentType("QCURVE")

    def test_normalizeSegmentType_unknown(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeSegmentType("offcurve")

    def test_normalizeSegmentType_notString(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeSegmentType(123)

    # ------
    # BPoint
    # ------

    # normalizeBPoint

    def test_normalizeBPoint_valid(self):
        from fontParts.base.bPoint import BaseBPoint
        bPoint, _ = self.objectGenerator("bPoint")
        result = normalizers.normalizeBPoint(bPoint)
        self.assertIsInstance(result, BaseBPoint)
        self.assertEqual(result, bPoint)

    def test_normalizeBPoint_notBPoint(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeSegment(123)

    # normalizeBPointType

    def test_normalizeBPointType_corner(self):
        result = normalizers.normalizeBPointType("corner")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"corner")

    def test_normalizeBPointType_Corner(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeBPointType("Corner")

    def test_normalizeBPointType_CORNER(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeBPointType("CORNER")

    def test_normalizeBPointType_curve(self):
        result = normalizers.normalizeBPointType("curve")
        self.assertIsInstance(result, unicode)
        self.assertEqual(result, u"curve")

    def test_normalizeBPointType_OffCurve(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeBPointType("Curve")

    def test_normalizeBPointType_OFFCURVE(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeBPointType("CURVE")

    def test_normalizeBPointType_unknown(self):
        with self.assertRaises(ValueError):
            normalizers.normalizeBPointType("offcurve")

    def test_normalizeBPointType_notString(self):
        with self.assertRaises(TypeError):
            normalizers.normalizeBPointType(123)
