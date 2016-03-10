import defcon
from fontParts.objects.base import BaseGlyph, FontPartsError
from base import RBaseObject
from contour import RContour
from component import RComponent
from anchor import RAnchor
from guideline import RGuideline

class RGlyph(RBaseObject, BaseGlyph):

    wrapClass = defcon.Glyph
    contourClass = RContour
    componentClass = RComponent
    anchorClass = RAnchor
    guidelineClass = RGuideline

    def __init__(self, wrap=None):
        if wrap is None:
            wrap = self.wrapClass()
        self._wrapped = wrap

    # --------------
    # Identification
    # --------------

    # Name

    def _get_name(self):
        return self.naked().name

    def _set_name(self, value):
        self.naked().name = value

    # Unicodes

    def _get_unicodes(self):
        return self.naked().unicodes

    def _set_unicodes(self, value):
        self.naked().unicodes = value

    # -------
    # Metrics
    # -------

    # horizontal

    def _get_width(self):
        return self.naked().width

    def _set_width(self, value):
        self.naked().width = value

    # vertical

    def _get_height(self):
        return self.naked().height

    def _set_height(self, value):
        self.naked().height = value

    # -----------------------------------------
    # Contour, Component and Anchor Interaction
    # -----------------------------------------

    # Contours

    def _lenContours(self, **kwargs):
        return len(self.naked())

    def _getContour(self, index, **kwargs):
        glyph = self.naked()
        contour = glyph[index]
        return self.contourClass(contour)

    def _removeContour(self, index, **kwargs):
        glyph = self.naked()
        contour = glyph[index]
        glyph.removeContour(contour)

    # Components

    def _lenComponents(self, **kwargs):
        return len(self.naked().components)

    def _getComponent(self, index, **kwargs):
        glyph = self.naked()
        component = glyph.components[index]
        return self.componentClass(component)

    def _removeComponent(self, index, **kwargs):
        glyph = self.naked()
        component = glyph.components[index]
        glyph.removeComponent(component)

    # Anchors

    def _lenAnchors(self, **kwargs):
        return len(self.naked().anchors)

    def _getAnchor(self, index, **kwargs):
        glyph = self.naked()
        anchor = glyph.anchors[index]
        return self.anchorClass(anchor)

    def _appendAnchor(self, name, position=None, color=None, **kwargs):
        glyph = self.naked()
        anchor = self.anchorClass().naked()
        anchor.name = name
        anchor.x = position[0]
        anchor.y = position[1]
        anchor.color = color
        glyph.appendAnchor(anchor)
        return self.anchorClass(anchor)

    def _removeAnchor(self, index, **kwargs):
        glyph = self.naked()
        anchor = glyph.anchors[index]
        glyph.removeAnchor(anchor)

    # Guidelines

    def _lenGuidelines(self, **kwargs):
        return len(self.naked().guidelines)

    def _getGuideline(self, index, **kwargs):
        glyph = self.naked()
        guideline = glyph.guidelines[index]
        return self.guidelineClass(guideline)

    def _appendGuideline(self, position, angle, name=None, color=None, **kwargs):
        glyph = self.naked()
        guideline = self.guidelineClass().naked()
        guideline.x = position[0]
        guideline.y = position[1]
        guideline.name = name        
        guideline.color = color
        glyph.appendGuideline(guideline)
        return self.guidelineClass(guideline)

    def _removeGuideline(self, index, **kwargs):
        glyph = self.naked()
        guideline = glyph.guidelines[index]
        glyph.removeGuideline(guideline)