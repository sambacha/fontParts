import weakref
from base import BaseObject, dynamicProperty

class BaseBPoint(BaseObject):

    # -------
    # Parents
    # -------

    def getParent(self):
        """
        This is a backwards compatibility method.
        """
        return self.contour

    # Contour

    _contour = None

    contour = dynamicProperty("contour", "The bPoint's parent contour.")

    def _get_contour(self):
        if self._contour is None:
            return None
        return self._contour()

    def _set_contour(self, contour):
        assert self._contour is None
        if contour is not None:
            contour = weakref.ref(contour)
        self._contour = glyph

    # Glyph

    glyph = dynamicProperty("glyph", "The bPoint's parent glyph.")

    def _get_glyph(self):
        if self._glyph is None:
            return None
        return self._glyph()

    # Layer

    layer = dynamicProperty("layer", "The bPoint's parent layer.")

    def _get_layer(self):
        if self._glyph is None:
            return None
        return self.glyph.layer

    # Font

    font = dynamicProperty("font", "The bPoint's parent font.")

    def _get_font(self):
        if self._glyph is None:
            return None
        return self.glyph.font

    # ----------
    # Attributes
    # ----------

    anchor = dynamicProperty("anchor", "The anchor point.")

    def _get_anchor(self):
        pass

    def _set_anchor(self, value):
        pass

    bcpIn = dynamicProperty("bcpIn", "The incoming off curve.")

    def _get_bcpIn(self):
        pass

    def _set_bcpIn(self, value):
        pass

    bcpOut = dynamicProperty("bcpOut", "The outgoing off curve.")

    def _get_bcpOut(self):
        pass

    def _set_bcpOut(self, value):
        pass

    type = dynamicProperty("type", "The bPoint type.")

    def _get_type(self):
        pass

    def _set_type(self, value):
        pass

    # --------------
    # Identification
    # --------------

    index = dynamicProperty("index", "The index of the bPoint within the ordered list of the parent contour's bPoints. None if the bPoint does not belong to a contour.")

    def _get_index(self):
        pass

    # ---------------
    # Transformations
    # ---------------

    def transform(self, matrix):
        """
        Transform the bPoint with the transformation matrix.
        The matrix must be a tuple defining a 2x2 transformation
        plus offset, aka Affine transform.
        """

    def move(self, value):
        """
        Move the bPoint by value. Value must
        be a tuple defining x and y values.
        """

    def scale(self, value, center=None):
        """
        Scale the bPoint by value. Value must be a
        tuple defining x and y values or a number.

        center defines the (x, y) point at which the
        scale should originate. The default is (0, 0).
        """

    def rotate(self, angle, offset=None):
        """
        Rotate the bPoint by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the rotation.
        """

    def skew(self, angle, offset=None):
        """
        Skew the bPoint by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the skew.
        """
    # ----
    # Misc
    # ----

    def round(self):
        """
        Round coordinates.
        """