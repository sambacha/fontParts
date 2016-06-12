import unittest
from fontParts.base import FontPartsError


class TestContour(unittest.TestCase):

    # ------
    # Bounds
    # ------

    def getContour_bounds(self):
        glyph = self.objectGenerator("glyph")
        pen = glyph.getPen()
        pen.moveTo((0, 0))
        pen.lineTo((0, 100))
        pen.lineTo((100, 100))
        pen.lineTo((100, 0))
        pen.closePath()
        contour = glyph.contours[0]
        return contour, dict(glyph=glyph)

    def getContour_boundsExtrema(self):
        glyph = self.objectGenerator("glyph")
        pen = glyph.getPen()
        pen.moveTo((0, 0))
        pen.lineTo((0, 100))
        pen.lineTo((50, 100))
        pen.curveTo((117, 100), (117, 0), (50, 0))
        pen.closePath()
        contour = glyph.contours[0]
        return contour, dict(glyph=glyph)

    def test_bounds(self):
        # get
        contour, unrequested = self.getContour_bounds()
        self.assertEqual(
            contour.bounds,
            (0, 0, 100, 100)
        )
        # get: float
        contour.moveBy((0.5, -0.5))
        self.assertEqual(
            contour.bounds,
            (0.5, -0.5, 100.5, 99.5)
        )
        # get: point not at extrema
        contour, unrequested = self.getContour_boundsExtrema()
        bounds = tuple(int(round(i)) for i in contour.bounds)
        self.assertEqual(
            bounds,
            (0, 0, 100, 100)
        )
        # set
        with self.assertRaises(AttributeError):
            contour.bounds = (1, 2, 3, 4)
