import unittest
from fontParts.world import SortFonts

class TestSortFonts(unittest.TestCase):

    def getFont(self):
        font, _ = self.objectGenerator("font")
        return font

    def getFonts_sortBy(self, attr, values):
        fonts = []
        for value in values:
            font = self.getFont()
            setattr(font.info, attr, value)
            if attr != "familyName":
                font.info.familyName = "%s %s" % (attr, repr(value))
            fonts.append(font)
        return fonts

    def getFont_sortBy_monospaceGlyphs(self):
        font = self.getFont()
        glyph1 = font.newGlyph("a")
        glyph1.width = 100
        glyph2 = font.newGlyph("b")
        glyph2.width = 100
        return font

    def getFont_sortBy_proportionalGlyphs(self):
        font = self.getFont()
        glyph1 = font.newGlyph("a")
        glyph1.width = 100
        glyph2 = font.newGlyph("b")
        glyph2.width = 200
        return font

    # familyName

    def test_sortBy_familyName(self):
        font1, font2, font3, font4 = self.getFonts_sortBy(
            "familyName",
            ["aaa", "bbb", "ccc", None]
        )
        beforeSort = [font1, font2, font3, font4]
        afterSort = SortFonts(beforeSort, "familyName")
        expectedSort = [font4, font1, font2, font3]
        self.assertEqual(afterSort, expectedSort)

    # styleName

    def test_sortBy_styleName(self):
        font1, font2, font3, font4 = self.getFonts_sortBy(
            "styleName",
            ["aaa", "bbb", "ccc", None]
        )
        beforeSort = [font1, font2, font3, font4]
        afterSort = SortFonts(beforeSort, "styleName")
        expectedSort = [font4, font1, font2, font3]
        self.assertEqual(afterSort, expectedSort)

    # isRoman

    def test_sortBy_isRoman_styleMapStyleName(self):
        font1, font2, font3, font4 = self.getFonts_sortBy(
            "styleMapStyleName",
            ["regular", "italic", "bold", "bold italic"]
        )
        beforeSort = [font1, font3, font4, font2]
        afterSort = SortFonts(beforeSort, "isRoman")
        expectedSort = [font2, font4, font1, font3]
        self.assertEqual(afterSort, expectedSort)

    def test_sortBy_isRoman_italicAngle(self):
        font1, font2, font3, font4 = self.getFonts_sortBy(
            "italicAngle",
            [1, 2, 3, 0]
        )
        beforeSort = [font1, font2, font3, font4]
        afterSort = SortFonts(beforeSort, "isRoman")
        expectedSort = [font4, font1, font2, font3]
        self.assertEqual(afterSort, expectedSort)

    # isItalic

    def test_sortBy_isItalic_styleMapStyleName(self):
        font1, font2, font3, font4 = self.getFonts_sortBy(
            "styleMapStyleName",
            ["regular", "italic", "bold", "bold italic"]
        )
        beforeSort = [font1, font2, font3, font4]
        afterSort = SortFonts(beforeSort, "isItalic")
        expectedSort = [font2, font4, font1, font3]
        self.assertEqual(afterSort, expectedSort)

    def test_sortBy_isItalic_italicAngle(self):
        font1, font2, font3, font4 = self.getFonts_sortBy(
            "italicAngle",
            [0, 1, 2, 3]
        )
        beforeSort = [font1, font2, font3, font4]
        afterSort = SortFonts(beforeSort, "isItalic")
        expectedSort = [font2, font3, font4, font1]
        self.assertEqual(afterSort, expectedSort)

    # widthValue

    def test_sortBy_widthValue(self):
        font1, font2, font3, font4 = self.getFonts_sortBy(
            "openTypeOS2WidthClass",
            [1, 2, 3, None]
        )
        beforeSort = [font1, font2, font3, font4]
        afterSort = SortFonts(beforeSort, "widthValue")
        expectedSort = [font4, font1, font2, font3]
        self.assertEqual(afterSort, expectedSort)

    # weightValue

    def test_sortBy_weightValue(self):
        font1, font2, font3, font4 = self.getFonts_sortBy(
            "openTypeOS2WeightClass",
            [100, 200, 300, None]
        )
        beforeSort = [font1, font2, font3, font4]
        afterSort = SortFonts(beforeSort, "weightValue")
        expectedSort = [font4, font1, font2, font3]
        self.assertEqual(afterSort, expectedSort)

    # isMonospace

    def test_sortBy_isProportional_postscriptIsFixedPitch(self):
        font1, font2, font3, font4 = self.getFonts_sortBy(
            "postscriptIsFixedPitch",
            [True, True, False, False]
        )
        beforeSort = [font1, font2, font3, font4]
        afterSort = SortFonts(beforeSort, "isMonospace")
        expectedSort = [font3, font4, font1, font2]
        self.assertEqual(afterSort, expectedSort)

    def test_sortBy_isMonospace_glyphs(self):
        font1 = self.getFont_sortBy_monospaceGlyphs()
        font2 = self.getFont_sortBy_monospaceGlyphs()
        font3 = self.getFont_sortBy_proportionalGlyphs()
        font4 = self.getFont_sortBy_proportionalGlyphs()
        beforeSort = [font3, font4, font1, font2]
        afterSort = SortFonts(beforeSort, "isMonospace")
        expectedSort = [font1, font2, font3, font4]
        self.assertEqual(afterSort, expectedSort)

    # isProportional

    def test_sortBy_isProportional_postscriptIsFixedPitch(self):
        font1, font2, font3, font4 = self.getFonts_sortBy(
            "postscriptIsFixedPitch",
            [False, False, True, True]
        )
        beforeSort = [font1, font2, font3, font4]
        afterSort = SortFonts(beforeSort, "isProportional")
        expectedSort = [font3, font4, font1, font2]
        self.assertEqual(afterSort, expectedSort)

    def test_sortBy_isProportional_glyphs(self):
        font1 = self.getFont_sortBy_monospaceGlyphs()
        font2 = self.getFont_sortBy_monospaceGlyphs()
        font3 = self.getFont_sortBy_proportionalGlyphs()
        font4 = self.getFont_sortBy_proportionalGlyphs()
        beforeSort = [font1, font2, font3, font4]
        afterSort = SortFonts(beforeSort, "isProportional")
        expectedSort = [font3, font4, font1, font2]
        self.assertEqual(afterSort, expectedSort)
