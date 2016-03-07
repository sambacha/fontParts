from base import BaseObject, dynamicProperty
import validators

class BaseAnchor(BaseObject):

    def __repr__(self):
        pass

    # --------
    # Position
    # --------

    # x

    x = dynamicProperty("base_x", "The x coordinate of the anchor.")

    def _get_base_x(self):
        value = self._get_x()
        value = validators.validateXValue(value)
        return value

    def _set_base_x(self, value):
        value = validators.validateXValue(value)
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

    y = dynamicProperty("y", "The y coordinate of the anchor.")

    def _get_base_y(self):
        value = self._get_y()
        value = validators.validateYValue(value)
        return value

    def _set_base_y(self, value):
        value = validators.validateYValue(value)
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

    index = dynamicProperty("index", "The index of the anchor within the ordered list of the parent glyphs's anchor. XXX -1 (or None?) if the anchor does not belong to a glyph. I vote None-BK")

    def _get_index(self):
        self.raiseNotImplementedError()

    # identifier

    identifier = dynamicProperty("identifier", "The unique identifier for the anchor.")

    def _get_identifier(self):
        self.raiseNotImplementedError()

    # name

    name = dynamicProperty("base_name", "The name of the anchor.")

    def _get_base_name(self):
        value = self._get_name()
        if value is not None:
            value = validators.validateString(value)
        return value

    def _set_base_name(self, value):
        if value is not None:
            value = validators.validateString(value)
        self._set_name(value)

    def _get_name(self):
        """
        Get the name anchor of the anchor.
        This must return a unicode string or None.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_name(self):
        """
        Get the name anchor of the anchor.
        This will be a unicode string or None.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # color

    color = dynamicProperty("color", "The anchor's color. XXX need to determine the data type")

    def _get_color(self):
        self.raiseNotImplementedError()

    def _set_color(self):
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

    def move(self, value):
        """
        Move the anchor by value. Value must
        be a tuple defining x and y values.
        """

    def scale(self, value, center=None):
        """
        Scale the anchor by value. Value must be a
        tuple defining x and y values.

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

    def skew(self, angle, offset=None):
        """
        Skew the anchor by angle.

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
        Copy this anchor by duplicating the data into
        a anchor that does not belong to a glyph.
        """
