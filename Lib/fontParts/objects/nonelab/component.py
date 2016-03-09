import defcon
from fontParts.objects.base import BaseComponent, FontPartsError
from base import RBaseObject

class RComponent(RBaseObject, BaseComponent):

    wrapClass = defcon.Component

    def __init__(self, wrap=None):
        if wrap is None:
            wrap = self.wrapClass()
        self._wrapped = wrap