import defcon
from fontParts.objects.base import BaseLayer, FontPartsError
from base import RBaseObject
from glyph import RGlyph

class RLayer(RBaseObject, BaseLayer):

    wrapClass = defcon.Layer
    glyphClass = RGlyph

    def __init__(self, wrap=None, font=None):
        self.font = font
        if wrap is None:
            wrap = self.wrapClass()
        self._wrapped = wrap

    # --------------
    # Identification
    # --------------

    # name

    def _get_name(self):
        return self.naked().name

    def _set_name(self, value, **kwargs):
        self.naked().name = value

    # color

    def _get_color(self):
        value = self.naked().color
        value = self._convertFromDefconColor(value)
        return value

    def _set_color(self, value, **kwargs):
        self.naked().color = value

    # -----------------
    # Glyph Interaction
    # -----------------

    def _getItem(self, name, **kwargs):
        layer = self.naked()
        glyph = layer[name]
        return self.glyphClass(glyph)

    def _keys(self, **kwargs):
        return self.naked().keys()
