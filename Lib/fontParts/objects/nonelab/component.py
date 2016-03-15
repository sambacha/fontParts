import defcon
from fontParts.objects.base import BaseComponent, FontPartsError
from base import RBaseObject

class RComponent(RBaseObject, BaseComponent):

    wrapClass = defcon.Component

    # ----------
    # Attributes
    # ----------

    # baseGlyph

    def _get_baseGlyph(self):
        return self.naked().baseGlyph

    def _set_baseGlyph(self, value):
        self.naked().baseGlyph = value

    # transformation

    def _get_transformation(self):
        return self.naked().transformation

    def _set_transformation(self, value):
        self.naked().transformation = value

    # --------------
    # Identification
    # --------------

    # index

    def _set_index(self, value):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # identifier

    def _get_identifier(self):
        """
        Subclasses must override this method.
        """
        return self.naked().identifier

    # -------------
    # Normalization
    # -------------

    def _decompose(self):
        """
        Subclasses must override this method.
        """
        component = self.naked()
        glyph = component.glyph
        glyph.decomposeComponent(component)
