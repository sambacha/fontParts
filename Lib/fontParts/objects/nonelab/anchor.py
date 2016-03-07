import defcon
from fontParts.objects.base import BaseAnchor

class RAnchor(BaseAnchor):

    wrapClass = defcon.Anchor

    def __init__(self, wrap=None, glyph=None):
        self.glyph = glyph
        if wrap is None:
            wrap = self.wrapClass()
        self._wrapped = wrap
        self._wrapped.x = 0
        self._wrapped.y = 0

    # --------
    # Position
    # --------

    # x

    def _get_x(self):
        return self._wrapped.x

    def _set_x(self, value):
        self._wrapped.x = value

    # y

    def _get_y(self):
        return self._wrapped.y

    def _set_y(self, value):
        self._wrapped.y = value

    # --------------
    # Identification
    # --------------

    # identifier

    def _get_identifier(self):
        return self._wrapped.identifier

    # name

    def _get_name(self):
        return self._wrapped.name

    def _set_name(self, value):
        self._wrapped.name = value

    # color

    def _get_color(self):
        value = self._wrapped.color
        if value is not None:
            value = tuple(value)
        return value

    def _set_color(self, value):
        self._wrapped.color = value
