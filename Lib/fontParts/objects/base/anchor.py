import weakref
import math
from fontTools.misc import transform
import validators
from base import BaseObject, dynamicProperty
from color import Color

class BaseAnchor(BaseObject):

    # ----
    # Copy
    # ----

    copyAttributes = (
        "x",
        "y",
        "name",
        "color"
    )

    def copy(self):
        """
        Copy this anchor by duplicating the data into
        a anchor that does not belong to a glyph.
        """
        return super(BaseAnchor, self).copy()

    # -------
    # Parents
    # -------

    def getParent(self):
        """
        This is a backwards compatibility method.
        """
        return self.glyph

    # Glyph

    _glyph = None

    glyph = dynamicProperty("glyph", "The anchor's parent glyph.")

    def _get_glyph(self):
        if self._glyph is None:
            return None
        return self._glyph()

    def _set_glyph(self, glyph):
        assert self._glyph is None
        if glyph is not None:
            glyph = weakref.ref(glyph)
        self._glyph = glyph

    # Layer

    layer = dynamicProperty("layer", "The anchor's parent layer.")

    def _get_layer(self):
        if self._glyph is None:
            return None
        return self.glyph.layer

    # Font

    font = dynamicProperty("font", "The anchor's parent font.")

    def _get_font(self):
        if self._glyph is None:
            return None
        return self.glyph.font

    # --------
    # Position
    # --------

    # x

    x = dynamicProperty("base_x", "The x coordinate of the anchor.")

    def _get_base_x(self):
        value = self._get_x()
        value = validators.validateX(value)
        return value

    def _set_base_x(self, value):
        value = validators.validateX(value)
        self._set_x(value)

    def _get_x(self):
        """
        Get the x value of the anchor.
        This must return an int or a float.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_x(self, value):
        """
        Set the x value of the anchor.
        This will be an int or a float.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # y

    y = dynamicProperty("base_y", "The y coordinate of the anchor.")

    def _get_base_y(self):
        value = self._get_y()
        value = validators.validateY(value)
        return value

    def _set_base_y(self, value):
        value = validators.validateY(value)
        self._set_y(value)

    def _get_y(self):
        """
        Get the y value of the anchor.
        This must return an int or a float.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_y(self, value):
        """
        Set the y value of the anchor.
        This will be an int or a float.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # --------------
    # Identification
    # --------------

    # index

    index = dynamicProperty("base_index", "The index of the anchor within the ordered list of the parent glyphs's anchor.")

    def _get_base_index(self):
        value = self._get_index()
        value = validators.validateIndex(value)
        return value

    def _get_index(self):
        glyph = self.glyph
        if glyph is None:
            return None
        return glyph.anchors.index(self)

    # identifier

    identifier = dynamicProperty("base_identifier", "The unique identifier for the anchor.")

    def _get_base_identifier(self):
        value = self._get_identifier()
        value = validators.validateIdentifier(value)
        return value

    def _get_identifier(self):
        """
        Get the unique identifier of the anchor.
        This must return a string.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # name

    name = dynamicProperty("base_name", "The name of the anchor.")

    def _get_base_name(self):
        value = self._get_name()
        if value is not None:
            value = validators.validateAnchorName(value)
        return value

    def _set_base_name(self, value):
        if value is not None:
            value = validators.validateAnchorName(value)
        self._set_name(value)

    def _get_name(self):
        """
        Get the name of the anchor.
        This must return a unicode string or None.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_name(self, value):
        """
        Set the name of the anchor.
        This will be a unicode string or None.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # color

    color = dynamicProperty("base_color", "The anchor's color.")

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
        Get the color of the anchor.
        This must return a color tuple or None.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_color(self, value):
        """
        Set the color of the anchor.
        This will be a color tuple or None.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # ---------------
    # Transformations
    # ---------------

    def transform(self, matrix):
        """
        Transform the anchor with the transformation matrix.
        The matrix must be a tuple defining a 2x2 transformation
        plus offset, aka Affine transform.
        """
        matrix = validators.validateTransformationMatrix(matrix)
        self._transform(matrix)

    def _transform(self, matrix):
        """
        Transform the anchor with the matrix.
        The matrix will be a tuple of floats defining a 2x2
        transformation plus offset, aka Affine transform.

        Subclasses may override this method.
        """
        t = transform.Transform(*matrix)
        self.x, self.y = t.transformPoint((self.x, self.y))

    def move(self, value):
        """
        Move the anchor by value. Value must
        be a tuple defining x and y values.
        """
        value = validators.validateTransformationOffset(value)
        self._move(value)

    def _move(self, value):
        """
        Move the anchor by value.
        The value will be a tuple of (x, y) where
        x and y are ints or floats.

        Subclasses may override this method.
        """
        x, y = value
        t = transform.Offset(x, y)
        self.transform(tuple(t))

    def scale(self, value, center=None):
        """
        Scale the anchor by value. Value must be a
        tuple defining x and y values or a number.

        center defines the (x, y) point at which the
        scale should originate. The default is (0, 0).
        """

    def rotate(self, angle, offset=None):
        """
        Rotate the anchor by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the rotation.
        """
        angle = validators.validateTransformationAngle(angle)
        self._rotate(angle)

    def _rotate(self, angle):
        """
        Rotate the anchor by angle.
        The angle will be a float between 0 and 360 degrees.

        Subclasses may override this method.
        """
        a = angle / (180 / math.pi)
        t = transform.Identity.rotate(a)
        self.transform(tuple(t))

    def skew(self, angle, offset=None):
        """
        Skew the anchor by angle.

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
        self.x = int(round(self.x))
        self.y = int(round(self.y))
