import weakref
from base import BaseObject, dynamicProperty
import validators
from color import Color

class BaseImage(BaseObject):

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

    glyph = dynamicProperty("glyph", "The image's parent glyph.")

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

    layer = dynamicProperty("layer", "The image's parent layer.")

    def _get_layer(self):
        if self._glyph is None:
            return None
        return self.glyph.layer

    # Font

    font = dynamicProperty("font", "The image's parent font.")

    def _get_font(self):
        if self._glyph is None:
            return None
        return self.glyph.font

    # ----------
    # Attributes
    # ----------

    # Transformation

    transformation = dynamicProperty("base_transformation", "The image's transformation matrix.")

    def _get_base_transformation(self):
        value = self._get_transformation()
        value = validators.validateTransformationMatrix(value)
        return value

    def _set_base_transformation(self, value):
        value = validators.validateTransformationMatrix(value)
        self._set_transformation(value)

    def _get_transformation(self):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_transformation(self, value):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    offset = dynamicProperty("base_offset", "The image's offset.")

    def _get_base_offset(self):
        value = self._get_offset()
        value = validators.validateTransformationOffset(value)
        return value

    def _set_base_offset(self, value):
        value = validators.validateTransformationOffset(value)
        self._set_offset(value)

    def _get_offset(self):
        """
        Subclasses may override this method.
        """
        sx, sxy, syx, sy, ox, oy = self.transformation
        return (ox, oy)

    def _set_offset(self, value):
        """
        Subclasses may override this method.
        """
        sx, sxy, syx, sy, ox, oy = self.transformation
        ox, oy = value
        self.transformation = (sx, sxy, syx, sy, ox, oy)

    scale = dynamicProperty("base_scale", "The image's scale.")

    def _get_base_scale(self):
        value = self._get_scale()
        value = validators.validateTransformationScale(value)
        return value

    def _set_base_scale(self, value):
        value = validators.validateTransformationScale(value)
        self._set_scale(value)

    def _get_scale(self):
        """
        Subclasses may override this method.
        """
        sx, sxy, syx, sy, ox, oy = self.transformation
        return (sx, sy)

    def _set_scale(self, value):
        """
        Subclasses may override this method.
        """
        sx, sxy, syx, sy, ox, oy = self.transformation
        sx, sy = value
        self.transformation = (sx, sxy, syx, sy, ox, oy)

    # Color

    color = dynamicProperty("base_color", "The image's color.")

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
        Return the color value as a color tuple or None.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_color(self, value):
        """
        value will be a color tuple or None.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # Data

    data = dynamicProperty("data", "The image's raw byte data. The possible formats are defined by the environments.")

    def _get_base_data(self):
        return self._get_data()

    def _set_base_data(self, value):
        self._set_data(value)

    def _get_data(self):
        """
        This must return raw byte data.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_data(self):
        """
        value will be raw byte data.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # ---------------
    # Transformations
    # ---------------

    def transform(self, matrix):
        """
        Transform the image with the transformation matrix.
        The matrix must be a tuple defining a 2x2 transformation
        plus offset, aka Affine transform.
        """

    def move(self, value):
        """
        Move the image by value. Value must
        be a tuple defining x and y values.
        """

    def scale(self, value, center=None):
        """
        Scale the image by value. Value must be a
        tuple defining x and y values or a number.

        center defines the (x, y) point at which the
        scale should originate. The default is (0, 0).
        """

    def rotate(self, angle, offset=None):
        """
        Rotate the image by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the rotation.
        """

    def skew(self, angle, offset=None):
        """
        Skew the image by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the skew.
        """

    # ----
    # Misc
    # ----

    def copy(self):
        """
        Copy this image by duplicating the data into
        a image that does not belong to a glyph.
        """
