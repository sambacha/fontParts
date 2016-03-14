import weakref
from base import BaseObject, dynamicProperty
import validators

class BasePoint(BaseObject):

    def copy(self):
        """
        Copy this point by duplicating the data into
        a point that does not belong to a segment.
        """

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

    contour = dynamicProperty("contour", "The point's parent contour.")

    def _get_contour(self):
        if self._contour is None:
            return None
        return self._contour()

    def _set_contour(self, contour):
        assert self._contour is None
        if contour is not None:
            contour = weakref.ref(contour)
        self._contour = contour

    # Glyph

    glyph = dynamicProperty("glyph", "The point's parent glyph.")

    def _get_glyph(self):
        if self._contour is None:
            return None
        return self.contour.glyph

    # Layer

    layer = dynamicProperty("layer", "The point's parent layer.")

    def _get_layer(self):
        if self._contour is None:
            return None
        return self.glyph.layer

    # Font

    font = dynamicProperty("font", "The point's parent font.")

    def _get_font(self):
        if self._contour is None:
            return None
        return self.glyph.font

    # ----------
    # Attributes
    # ----------

    # type

    type = dynamicProperty("base_type", "The point type. The possible types are move, line, curve, qCurve, offCurve.")

    def _get_base_type(self):
        value = self._get_type()
        value = validators.validatePointType(value)
        return value

    def _set_base_type(self, value):
        value = validators.validatePointType(value)
        self._set_type(value)

    def _get_type(self):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_type(self, value):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # smooth

    smooth = dynamicProperty("base_smooth", "Boolean indicating if the point is smooth or not.")

    def _get_base_smooth(self):
        value = self._get_smooth()
        value = validators.validateBoolean(value)
        return value

    def _set_base_smooth(self, value):
        value = validators.validateBoolean(value)
        self._set_smooth(value)

    def _get_smooth(self):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_smooth(self, value):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # x

    x = dynamicProperty("base_x", "The x coordinate of the point.")

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

    y = dynamicProperty("y", "The y coordinate of the point.")

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

    # --------------
    # Identification
    # --------------

    # index

    index = dynamicProperty("base_index", "The index of the point within the ordered list of the parent contour's points.")

    def _get_base_index(self):
        value = self._get_index()
        value = validators.validateIndex(value)
        return value

    def _get_index(self):
        """
        Subclasses may override this method.
        """
        contour = self.contour
        if contour is None:
            return None
        return contour.points.index(self)

    # name

    name = dynamicProperty("name", "The name of the point.")

    def _get_base_name(self):
        value = self._get_name()
        if value is not None:
            value = validators.validatePointName(value)
        return value

    def _set_base_name(self, value):
        if value is not None:
            value = validators.validatePointName(value)
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

    identifier = dynamicProperty("base_identifier", "The unique identifier for the point.")

    def _get_base_identifier(self):
        value = self._get_identifier()
        value = validators.validateIdentifier(value)
        return value

    def _get_identifier(self):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # ---------------
    # Transformations
    # ---------------

    def transform(self, matrix):
        """
        Transform the point with the transformation matrix.
        The matrix must be a tuple defining a 2x2 transformation
        plus offset, aka Affine transform.
        """

    def move(self, value):
        """
        Move the point by value. Value must
        be a tuple defining x and y values.
        """

    def scale(self, value, center=None):
        """
        Scale the point by value. Value must be a
        tuple defining x and y values or a number.

        center defines the (x, y) point at which the
        scale should originate. The default is (0, 0).
        """

    def rotate(self, angle, offset=None):
        """
        Rotate the point by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the rotation.
        """

    def skew(self, angle, offset=None):
        """
        Skew the point by angle.

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
