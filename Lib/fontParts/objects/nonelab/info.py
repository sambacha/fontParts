import defcon
from fontParts.objects.base import BaseInfo, FontPartsError
from base import RBaseObject

class RInfo(RBaseObject, BaseInfo):

    def _getAttr(self, attr):
        return getattr(self.naked(), attr)

    def _setAttr(self, attr, value):
        setattr(self.naked(), attr, value)
