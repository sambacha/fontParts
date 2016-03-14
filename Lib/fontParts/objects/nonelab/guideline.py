import defcon
from fontParts.objects.base import BaseGuideline, FontPartsError
from base import RBaseObject

class RGuideline(RBaseObject, BaseGuideline):

    wrapClass = defcon.Guideline

    def __init__(self, wrap=None):
        if wrap is None:
            wrap = self.wrapClass()
        self._wrapped = wrap

   # --------
    # Position
    # --------

    # x

    def _get_x(self):
        return self.naked().x

    def _set_x(self, value):
        self.naked().x = value

    # y

    def _get_y(self):
        return self.naked().y

    def _set_y(self, value):
        self.naked().y = value

    # angle

    def _get_angle(self):
        return self.naked().angle

    def _set_angle(self, value):
        self.naked().angle = value

    # --------------
    # Identification
    # --------------

    # identifier

    def _get_identifier(self):
        return self.naked().identifier

    # name

    def _get_name(self):
        return self.naked().name

    def _set_name(self, value):
        self.naked().name = value

    # color

    def _get_color(self):
        value = self.naked().color
        if value is not None:
            value = tuple(value)
        return value

    def _set_color(self, value):
        self.naked().color = value