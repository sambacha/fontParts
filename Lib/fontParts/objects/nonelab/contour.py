import defcon
from fontParts.objects.base import BaseContour, FontPartsError
from base import RBaseObject

class RContour(RBaseObject, BaseContour):

    wrapClass = defcon.Contour

    def __init__(self, wrap=None):
        if wrap is None:
            wrap = self.wrapClass()
        self._wrapped = wrap

    # --------------
    # Identification
    # --------------

    # index

    def _set_index(self, value):
        contour = self.naked()
        glyph = contour.glyph
        glyph.removeContour(contour)
        glyph.insertContour(value, contour)

    # identifier

    def _get_identifier(self):
        return self.naked().identifier

    # ---------
    # Direction
    # ---------

    def _get_clockwise(self):
        return self.naked().clockwise

    def _reverseContour(self, **kwargs):
        self.naked().reverse()
