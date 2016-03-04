from base import BaseObject, dynamicProperty

class BaseAnchor(BaseObject):

    def __repr__(self):
        pass

    x = dynamicProperty("x", "The x coordinate of the anchor.")

    def _get_x(self):
        self.raiseNotImplementedError()

    def _set_x(self, value):
        self.raiseNotImplementedError()

    y = dynamicProperty("y", "The y coordinate of the anchor.")

    def _get_y(self):
        self.raiseNotImplementedError()

    def _set_y(self, value):
        self.raiseNotImplementedError()

    position = dynamicProperty("position", "The position (x, y) of the anchor. XXX is this needed?")

    def _get_position(self):
        pass

    def _set_position(self, value):
        pass

    # --------------
    # Identification
    # --------------

    index = dynamicProperty("index", "The index of the anchor within the ordered list of the parent glyphs's anchor. XXX -1 (or None?) if the anchor does not belong to a glyph.")

    def _get_index(self):
        self.raiseNotImplementedError()

    name = dynamicProperty("name", "The name of the anchor.")

    def _get_name(self):
        self.raiseNotImplementedError()

    def _set_name(self):
        self.raiseNotImplementedError()

    mark = dynamicProperty("mark", "The anchor's mark. XXX need to determine the data type")

    def _get_mark(self):
        self.raiseNotImplementedError()

    def _set_mark(self):
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
        a anchor that does not belong to a segment.
        """
