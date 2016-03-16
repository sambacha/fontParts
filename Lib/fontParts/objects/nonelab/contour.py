import defcon
from fontParts.objects.base import BaseContour, FontPartsError
from base import RBaseObject
from point import RPoint
from segment import RSegment

class RContour(RBaseObject, BaseContour):

    wrapClass = defcon.Contour
    pointClass = RPoint
    segmentClass = RSegment

    # --------------
    # Identification
    # --------------

    # index

    def _set_index(self, value):
        contour = self.naked()
        glyph = contour.glyph
        if value > glyph.contours.index(contour):
            value -= 1
        glyph.removeContour(contour)
        glyph.insertContour(value, contour)

    # identifier

    def _get_identifier(self):
        contour = self.naked()
        if contour.identifier is None:
            contour.generateIdentifier()
        return contour.identifier

    # ---------
    # Direction
    # ---------

    def _get_clockwise(self):
        return self.naked().clockwise

    def _reverseContour(self, **kwargs):
        self.naked().reverse()

    # ------
    # Points
    # ------

    def _lenPoints(self, **kwargs):
        return len(self.naked())

    def _getPoint(self, index, **kwargs):
        contour = self.naked()
        point = contour[index]
        return self.pointClass(point)

    def _insertPoint(self, index, position, type=None, smooth=None, name=None, identifier=None):
        point = self.pointClass()
        point.x = position[0]
        point.y = position[1]
        point.type = type
        point.smooth = smooth
        point.name = name
        point = point.naked()
        point.identifier = identifier
        self.naked().insertPoint(index, point)

    def _removePoint(self, index, **kwargs):
        contour = self.naked()
        point = contour[index]
        contour.removePoint(point)
