import defcon
from fontParts.objects.base import BaseFeatures, FontPartsError
from base import RBaseObject

class RFeatures(RBaseObject, BaseFeatures):

    def _get_text(self):
        return self.naked().text

    def _set_text(self, value):
        self.naked().text = value