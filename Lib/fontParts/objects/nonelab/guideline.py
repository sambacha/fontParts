import defcon
from fontParts.objects.base import BaseGuideline, FontPartsError
from base import RBaseObject

class RGuideline(RBaseObject, BaseGuideline):

    wrapClass = defcon.Guideline

    def __init__(self, wrap=None):
        if wrap is None:
            wrap = self.wrapClass()
        self._wrapped = wrap