import unittest
import collections
from fontTools.misc.py23 import basestring
from fontParts.base import FontPartsError


class TestBPoint(unittest.TestCase):

    def getBPoint_corner(self):
        contour, _ = self.objectGenerator("contour")
        contour.appendPoint((0, 0), "move")
        contour.appendPoint((101, 202), "line")
        contour.appendPoint((303, 0), "line")
        bPoint = contour.bPoints[1]
        return bPoint

    def getBPoint_curve(self):
        contour, _ = self.objectGenerator("contour")
        contour.appendPoint((0, 0), "move")
        contour.appendSegment("curve", [(20, 130), (59, 202), (101, 202)])
        contour.appendSegment("curve", [(145, 202), (188, 105), (260, 105)])
        contour.appendSegment("line", [(329, 175)])
        bPoint = contour.bPoints[1]
        return bPoint
    
    def getBPoint_withName(self):
        bPoint = self.getBPoint_corner()
        bPoint.name = "BP"
        return bPoint

    # ----
    # repr
    # ----

    def test_reprContents(self):
        print "curve test"
        print self.getBPoint_curve()
        p = self.getBPoint_curve() # @@@ testing
        bPoint = self.getBPoint_corner()
        value = bPoint._reprContents()
        self.assertIsInstance(value, list)
        for i in value:
            self.assertIsInstance(i, basestring)

    def test_reprContents_noContour(self):
        point, _ = self.objectGenerator("point")
        value = point._reprContents()
        self.assertIsInstance(value, list)
        for i in value:
            self.assertIsInstance(i, basestring)
        
    # -------
    # Parents
    # -------

    def test_get_parent_font(self):
        font, _ = self.objectGenerator("font")
        layer = font.newLayer("L")
        glyph = layer.newGlyph("X")
        contour, _ = self.objectGenerator("contour")
        contour.appendPoint((0, 0), "move")
        contour.appendPoint((101, 202), "line")
        contour.appendPoint((303, 0), "line")
        glyph.appendContour(contour)
        contour = glyph.contours[0]
        bPoint = contour.bPoints[1]
        self.assertIsNotNone(bPoint.font)
        self.assertEqual(
            bPoint.font,
            font
        )

    def test_get_parent_noFont(self):
        layer, _ = self.objectGenerator("layer")
        glyph = layer.newGlyph("X")
        contour, _ = self.objectGenerator("contour")
        contour.appendPoint((0, 0), "move")
        contour.appendPoint((101, 202), "line")
        contour.appendPoint((303, 0), "line")
        glyph.appendContour(contour)
        contour = glyph.contours[0]
        bPoint = contour.bPoints[1]
        self.assertIsNone(bPoint.font)

    def test_get_parent_layer(self):
        layer, _ = self.objectGenerator("layer")
        glyph = layer.newGlyph("X")
        contour, _ = self.objectGenerator("contour")
        contour.appendPoint((0, 0), "move")
        contour.appendPoint((101, 202), "line")
        contour.appendPoint((303, 0), "line")
        glyph.appendContour(contour)
        contour = glyph.contours[0]
        bPoint = contour.bPoints[1]
        self.assertIsNotNone(bPoint.layer)
        self.assertEqual(
            bPoint.layer,
            layer
        )

    def test_get_parent_noLayer(self):
        glyph, _ = self.objectGenerator("glyph")
        contour, _ = self.objectGenerator("contour")
        contour.appendPoint((0, 0), "move")
        contour.appendPoint((101, 202), "line")
        contour.appendPoint((303, 0), "line")
        glyph.appendContour(contour)
        contour = glyph.contours[0]
        bPoint = contour.bPoints[1]
        self.assertIsNone(bPoint.font)
        self.assertIsNone(bPoint.layer)

    def test_get_parent_glyph(self):
        glyph, _ = self.objectGenerator("glyph")
        contour, _ = self.objectGenerator("contour")
        contour.appendPoint((0, 0), "move")
        contour.appendPoint((101, 202), "line")
        contour.appendPoint((303, 0), "line")
        glyph.appendContour(contour)
        contour = glyph.contours[0]
        bPoint = contour.bPoints[1]
        self.assertIsNotNone(bPoint.glyph)
        self.assertEqual(
            bPoint.glyph,
            glyph
        )

    def test_get_parent_noGlyph(self):
        contour, _ = self.objectGenerator("contour")
        contour.appendPoint((0, 0), "move")
        contour.appendPoint((101, 202), "line")
        contour.appendPoint((303, 0), "line")
        bPoint = contour.bPoints[1]
        self.assertIsNone(bPoint.glyph)

    def test_get_parent_contour(self):
        contour, _ = self.objectGenerator("contour")
        contour.appendPoint((0, 0), "move")
        contour.appendPoint((101, 202), "line")
        contour.appendPoint((303, 0), "line")
        bPoint = contour.bPoints[1]
        self.assertIsNotNone(bPoint.contour)
        self.assertEqual(
            bPoint.contour,
            contour
        )

    def test_get_parent_noContour(self):
        bPoint, _ = self.objectGenerator("bPoint")
        self.assertIsNone(bPoint.contour)

    def test_set_parent_contour(self):
        contour, _ = self.objectGenerator("contour")
        bPoint, _ = self.objectGenerator("bPoint")
        bPoint.contour = contour
        self.assertIsNotNone(bPoint.contour)
        self.assertEqual(
            bPoint.contour,
            contour
        )

    def test_set_already_set_parent_contour(self):
        contour, _ = self.objectGenerator("contour")
        contour.appendPoint((0, 0), "move")
        contour.appendPoint((101, 202), "line")
        contour.appendPoint((303, 0), "line")
        bPoint = contour.bPoints[1]
        contourOther, _ = self.objectGenerator("contour")
        with self.assertRaises(AssertionError):
            bPoint.contour = contourOther

    def test_set_parent_contour_none(self):
        bPoint, _ = self.objectGenerator("bPoint")
        bPoint.contour = None
        self.assertIsNone(bPoint.contour)

    def test_get_parent_glyph_noContour(self):
        bPoint, _ = self.objectGenerator("bPoint")
        self.assertIsNone(bPoint.glyph)

    def test_get_parent_layer_noContour(self):
        bPoint, _ = self.objectGenerator("bPoint")
        self.assertIsNone(bPoint.layer)

    def test_get_parent_font_noContour(self):
        bPoint, _ = self.objectGenerator("bPoint")
        self.assertIsNone(bPoint.font)
        
    # ----
    # Attributes
    # ----

    # type
    
    def test_type_corner(self):
        bPoint = self.getBPoint_corner()
        self.assertEqual(
            bPoint.type,
            "corner"
        )

    def test_type_curve(self):
        bPoint = self.getBPoint_corner()
        bPoint.type = "curve"
        self.assertEqual(
            bPoint.type,
            "curve"
        )

    def test_type_not_equal(self):
        bPoint = self.getBPoint_corner()
        bPoint.type = "curve"
        self.assertNotEqual(
            bPoint.type,
            "corner"
        )

    # anchor

    def test_get_anchor(self):
        bPoint = self.getBPoint_corner()
        self.assertEqual(
            bPoint.anchor,
            (101, 202)
        )
        
    def test_set_anchor_valid_tuple(self):
        bPoint = self.getBPoint_corner()
        bPoint.anchor = (51, 45)
        self.assertEqual(
            bPoint.anchor,
            (51, 45)
        )
        
    def test_set_anchor_valid_list(self):
        bPoint = self.getBPoint_corner()
        bPoint.anchor = [51, 45]
        self.assertEqual(
            bPoint.anchor,
            (51, 45)
        )
        
    def test_set_anchor_invalidLen(self):
        bPoint = self.getBPoint_corner()
        with self.assertRaises(ValueError):
            bPoint.anchor = [51, 45, 67]

    def test_set_x_invalidType(self):
        bPoint = self.getBPoint_corner()
        with self.assertRaises(TypeError):
            bPoint.anchor = 51
        
    # @@@ bcp in
    # with move point = FontPartsError
    # with (0, 0) and bcpOut is (0,0) turns into a line segment type
    # otherwise test that segment type ends up a curve, if it was a corner/line
    
    
    
    # @@@ bcp out
    


    # --------------
    # Identification
    # --------------

    # @@@ index

    def test_index(self):
        bPoint = self.getBPoint_corner()
        self.assertEqual(
            bPoint.index,
            1
        )
        
        
    # @@@ name

    # @@@ identifier

    def test_identifier_get_none(self):
        point = self.getBPoint_corner()
        self.assertIsNone(point.identifier)

    def test_identifier_generated_type(self):
        point = self.getBPoint_corner()
        point.generateIdentifier()
        self.assertIsInstance(point.identifier, basestring)

    def test_identifier_consistency(self):
        point = self.getBPoint_corner()
        point.generateIdentifier()
        # get: twice to test consistency
        self.assertEqual(point.identifier, point.identifier)

    def test_identifier_cannot_set(self):
        # identifier is a read-only property
        point = self.getBPoint_corner()
        with self.assertRaises(FontPartsError):
            point.identifier = "ABC"

    # ----
    # @@@ Hash
    # ----

    def test_hash(self):
        bPoint = self.getBPoint_corner()
        self.assertEqual(
            isinstance(bPoint, collections.Hashable),
            False
        )

    # --------
    # @@@ Equality
    # --------

    def test_object_equal_self(self):
        bPoint_one = self.getBPoint_corner()
        self.assertEqual(
            bPoint_one,
            bPoint_one
        )

    def test_object_not_equal_other(self):
        bPoint_one = self.getBPoint_corner()
        bPoint_two = self.getBPoint_corner()
        self.assertNotEqual(
            bPoint_one,
            bPoint_two
        )

    def test_object_equal_self_variable_assignment(self):
        bPoint_one = self.getBPoint_corner()
        a = bPoint_one
        a.anchor = (51, 45)
        self.assertEqual(
            bPoint_one,
            a
        )

    def test_object_not_equal_other_variable_assignment(self):
        bPoint_one = self.getBPoint_corner()
        bPoint_two = self.getBPoint_corner()
        a = bPoint_one
        self.assertNotEqual(
            bPoint_two,
            a
        )

    # ---------
    # @@@ Selection
    # ---------

    def test_selected_true(self):
        bPoint = self.getBPoint_corner()
        try:
            bPoint.selected = False
        except NotImplementedError:
            return
        bPoint.selected = True
        self.assertEqual(
            bPoint.selected,
            True
        )

    def test_selected_false(self):
        bPoint = self.getBPoint_corner()
        try:
            bPoint.selected = False
        except NotImplementedError:
            return
        bPoint.selected = False
        self.assertEqual(
            bPoint.selected,
            False
        )
    
    # ----
    # @@@ Copy
    # ----



    # --------------
    # @@@ Transformation
    # --------------
    
    # @@@ moveBy
    
    # @@@ scaleBy
    
    # @@@ rotateBy
    
    # @@@ skewBy
    
    
    # -------------
    # @@@ Normalization
    # -------------

    # @@@ round