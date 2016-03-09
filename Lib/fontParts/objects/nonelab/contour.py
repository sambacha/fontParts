import defcon
from fontParts.objects.base import BaseContour, FontPartsError
from base import RBaseObject

class RContour(RBaseObject, BaseContour):

    wrapClass = defcon.Contour

    def __init__(self, wrap=None):
        if wrap is None:
            wrap = self.wrapClass()
        self._wrapped = wrap