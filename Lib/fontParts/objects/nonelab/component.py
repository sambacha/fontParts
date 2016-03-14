import defcon
from fontParts.objects.base import BaseComponent, FontPartsError
from base import RBaseObject

class RComponent(RBaseObject, BaseComponent):

    wrapClass = defcon.Component
