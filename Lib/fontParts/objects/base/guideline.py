import weakref
from base import BaseObject, dynamicProperty

class BaseGuideline(BaseObject):

    def copy(self):
        """
        Copy this guideline by duplicating the data into
        a guideline that does not belong to a parent object.
        """

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

    # x

    x = dynamicProperty("base_x", "The x coordinate of the guideline.")

    def _get_base_x(self):
        value = self._get_x()
        value = validators.validateX(value)
        return value

    def _set_base_x(self, value):
        value = validators.validateX(value)
        self._set_x(value)

    def _get_x(self):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_x(self, value):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # y

    y = dynamicProperty("base_y", "The y coordinate of the guideline.")

    def _get_base_y(self):
        value = self._get_y()
        value = validators.validateY(value)
        return value

    def _set_base_y(self, value):
        value = validators.validateY(value)
        self._set_y(value)

    def _get_y(self):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_y(self, value):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # angle

    angle = dynamicProperty("base_angle", "The angle of the guideline.")

    def _get_base_angle(self):
        value = self._get_y()
        value = validators.validateGuidelineAngle(value)
        return value

    def _set_base_angle(self, value):
        value = validators.validateGuidelineAngle(value)
        self._set_y(value)

    def _get_angle(self):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_angle(self, value):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # --------------
    # Identification
    # --------------

    # index

    index = dynamicProperty("base_index", "The index of the guideline within the ordered list of the parent's guidelines.")

    def _get_base_index(self):
        value = self._get_index()
        value = validators.validateIndex(value)
        return value

    def _get_index(self):
        """
        Subclasses may override this method.
        """
        glyph = self.glyph
        if glyph is not None:
            parent = glyph
        else:
            parent = self.font
        if parent is None:
            return None
        return parent.guidelines.index(self)

    # name

    name = dynamicProperty("name", "The name of the guideline.")

    def _get_base_name(self):
        value = self._get_name()
        if value is not None:
            value = validators.validateGuidelineName(value)
        return value

    def _set_base_name(self, value):
        if value is not None:
            value = validators.validateGuidelineName(value)
        self._set_value(value)

    def _get_name(self):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_name(self, value):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # identifier

    identifier = dynamicProperty("base_identifier", "The unique identifier for the guideline.")

    def _get_base_identifier(self):
        value = self._get_identifier()
        value = validators.validateIdentifier(value)
        return value

    def _get_identifier(self):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # color

    color = dynamicProperty("base_color", "The guideline's color.")

    def _get_base_color(self):
        value = self._get_color()
        if value is not None:
            value = validators.validateColor(value)
            value = Color(value)
        return value

    def _set_base_color(self, value):
        if value is not None:
            value = validators.validateColor(value)
        self._set_color(value)

    def _get_color(self):
        """
        Get the color of the guideline.
        This must return a color tuple or None.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_color(self, value):
        """
        Set the color of the guideline.
        This will be a color tuple or None.

        Subclasses must override this method.
        """
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

    # -------------
    # Normalization
    # -------------

    def round(self):
        """
        Round coordinates.
        """
        self._round()

    def _round(self, **kwargs):
        """
        Subclasses may override this method.
        """
        self.x = int(round(self.x))
        self.y = int(round(self.y))
