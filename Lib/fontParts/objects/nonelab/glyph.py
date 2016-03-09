import defcon
from fontParts.objects.base import BaseGlyph, FontPartsError
from base import RBaseObject

class RGlyph(RBaseObject, BaseGlyph):

    wrapClass = defcon.Glyph

    def __init__(self, wrap=None, layer=None):
        self.layer = layer
        if wrap is None:
            wrap = self.wrapClass()
        self._wrapped = wrap
