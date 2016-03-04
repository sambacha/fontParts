class BasePoint(BaseObject):

    # ----------
    # Attributes
    # ----------

    def __repr__(self):
        pass

    type = dynamicProperty("type", "The point type. The possible types are move, line, curve, qcurve, offcurve (XXX is None also used for offcurves?).")

    def _get_type(self):
        self.raiseNotImplementedError()

    def _set_type(self, value):
        self.raiseNotImplementedError()

    smooth = dynamicProperty("smooth", "Boolean indicating if the point is smooth or not.")

    def _get_smooth(self):
        self.raiseNotImplementedError()

    def _set_smooth(self, value):
        self.raiseNotImplementedError()

    x = dynamicProperty("x", "The x coordinate of the point.")

    def _get_x(self):
        self.raiseNotImplementedError()

    def _set_x(self, value):
        self.raiseNotImplementedError()

    y = dynamicProperty("y", "The y coordinate of the point.")

    def _get_y(self):
        self.raiseNotImplementedError()

    def _set_y(self, value):
        self.raiseNotImplementedError()

    # --------------
    # Identification
    # --------------

    index = dynamicProperty("index", "The index of the point within the ordered list of the parent contour's points. None if the point does not belong to a contour. XXX does the index reference the index within the segment or the contour?")

    def _get_index(self):
        self.raiseNotImplementedError()

    name = dynamicProperty("name", "The name of the point.")

    def _get_name(self):
        self.raiseNotImplementedError()

    def _set_name(self):
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
        tuple defining x and y values.

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

    # ----
    # Misc
    # ----

    def round(self):
        """
        Round coordinates.
        """

    def copy(self):
        """
        Copy this point by duplicating the data into
        a point that does not belong to a segment.
        """