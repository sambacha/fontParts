import weakref
from base import BaseObject, dynamicProperty

class BaseGuideline(BaseObject):

    # -------
    # Parents
    # -------

    def getParent(self):
        """
        This is a backwards compatibility method.
        """
        glyph = self.glyph
        if glyph is not None:
            return glyph
        return self.font

    # Glyph

    _glyph = None

    glyph = dynamicProperty("glyph", "The guideline's parent glyph.")

    def _get_glyph(self):
        if self._glyph is None:
            return None
        return self._glyph()

    def _set_glyph(self, glyph):
        assert self._font is None
        assert self._glyph is None
        if glyph is not None:
            glyph = weakref.ref(glyph)
        self._glyph = glyph

    # Font

    _font = None

    font = dynamicProperty("font", "The guideline's parent font.")

    def _get_font(self):
        if self._font is not None:
            return self._font()
        elif self._glyph is not None:
            return self.glyph.font
        return None

    def _set_font(self, font):
        assert self._font is None
        assert self._glyph is None
        if font is not None:
            font = weakref.ref(font)
        self._font = font

    # Layer

    layer = dynamicProperty("layer", "The guideline's parent layer.")

    def _get_layer(self):
        if self._glyph is None:
            return None
        return self.glyph.layer

    # --------
    # Position
    # --------

    x = dynamicProperty("x", "The x coordinate of the guideline.")

    def _get_x(self):
        self.raiseNotImplementedError()

    def _set_x(self, value):
        self.raiseNotImplementedError()

    y = dynamicProperty("y", "The y coordinate of the guideline.")

    def _get_y(self):
        self.raiseNotImplementedError()

    def _set_y(self, value):
        self.raiseNotImplementedError()

    angle = dynamicProperty("angle", "The angle of the guideline. XXX need to define (should be the same as in the UFO spec")

    def _get_angle(self):
        self.raiseNotImplementedError()

    def _set_angle(self, value):
        self.raiseNotImplementedError()

    # --------------
    # Identification
    # --------------

    index = dynamicProperty("index", "The index of the guideline within the ordered list of the parent glyphs's guideline. XXX -1 (or None?) if the guideline does not belong to a glyph. I vote None-BK")

    def _get_index(self):
        self.raiseNotImplementedError()

    identifier = dynamicProperty("identifier", "The unique identifier for the guideline.")

    def _get_identifier(self):
        self.raiseNotImplementedError()

    name = dynamicProperty("name", "The name of the guideline.")

    def _get_name(self):
        self.raiseNotImplementedError()

    def _set_name(self):
        self.raiseNotImplementedError()

    color = dynamicProperty("color", "The guideline's color. XXX need to determine the data type")

    def _get_color(self):
        self.raiseNotImplementedError()

    def _set_color(self):
        self.raiseNotImplementedError()

    # ---------------
    # Transformations
    # ---------------

    def transform(self, matrix):
        """
        Transform the guideline with the transformation matrix.
        The matrix must be a tuple defining a 2x2 transformation
        plus offset, aka Affine transform.
        """

    def move(self, value):
        """
        Move the guideline by value. Value must
        be a tuple defining x and y values.
        """

    def scale(self, value, center=None):
        """
        Scale the guideline by value. Value must be a
        tuple defining x and y values or a number.

        center defines the (x, y) point at which the
        scale should originate. The default is (0, 0).
        """

    def rotate(self, angle, offset=None):
        """
        Rotate the guideline by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the rotation.
        """

    def skew(self, angle, offset=None):
        """
        Skew the guideline by angle.

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

    def copy(self):
        """
        Copy this guideline by duplicating the data into
        a guideline that does not belong to a parent object.
        """
