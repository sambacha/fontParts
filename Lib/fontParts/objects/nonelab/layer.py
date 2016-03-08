import defcon
from fontParts.objects.base import BaseLayer, FontPartsError
from base import RBaseObject


class RLayer(RBaseObject, BaseLayer):

    wrapClass = defcon.Layer

    def __init__(self, wrap=None, font=None):
        self.font = font
        if wrap is None:
            wrap = self.wrapClass()
        self._wrapped = wrap

    def naked(self):
        return self._wrapped

    # --------------
    # Identification
    # --------------

    # name

    def _get_name(self):
        return self.naked().name

    def _set_name(self, value):
        self.naked().name = value

    # color

    def _get_color(self):
        value = self.naked().color
        value = self._convertFromDefconColor(value)
        return value

    def _set_color(self, value):
        self.naked().color = value