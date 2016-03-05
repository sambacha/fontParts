from base import BaseObject, dynamicProperty

class BaseComponent(BaseObject):

    def __repr__(self):
        pass

    baseGlyph = dynamicProperty("baseGlyph", "The glyph the component references.")

    def _get_baseGlyph(self):
        self.raiseNotImplementedError()

    def _set_baseGlyph(self, value):
        self.raiseNotImplementedError()

    transformation = dynamicProperty("transformation", "The component's transformation matrix.")

    def _get_transformation(self):
        self.raiseNotImplementedError()

    def _set_transformation(self, value):
        self.raiseNotImplementedError()

    offset = dynamicProperty("offset", "The component's offset.")

    def _get_offset(self):
        pass

    def _set_offset(self, value):
        pass

    scale = dynamicProperty("scale", "The component's scale.")

    def _get_scale(self):
        pass

    def _set_scale(self, value):
        pass

    # --------------
    # Identification
    # --------------

    index = dynamicProperty("index", "The index of the component within the ordered list of the parent glyph's components. XXX -1 (or None?) if the component does not belong to a glyph A vote for None-BK.")

    def _get_index(self):
        self.raiseNotImplementedError()

    def _set_index(self, value):
        self.raiseNotImplementedError()

    identifier = dynamicProperty("identifier", "The unique identifier for the component.")

    def _get_identifier(self):
        self.raiseNotImplementedError()

    # ----
    # Pens
    # ----

    def draw(self, pen):
        """
        Draw the contour with the given Pen.
        """

    def drawPoints(self, pen):
        """
        Draw the contour with the given PointPen.
        """

    # ---------------
    # Transformations
    # ---------------

    def transform(self, matrix):
        """
        Transform the component with the transformation matrix.
        The matrix must be a tuple defining a 2x2 transformation
        plus offset, aka Affine transform.
        """

    def move(self, value):
        """
        Move the component by value. Value must
        be a tuple defining x and y values.
        """

    def scale(self, value, center=None):
        """
        Scale the component by value. Value must be a
        tuple defining x and y values.

        center defines the (x, y) point at which the
        scale should originate. The default is (0, 0).
        """

    def rotate(self, angle, offset=None):
        """
        Rotate the component by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the rotation.
        """

    def skew(self, angle, offset=None):
        """
        Skew the component by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the skew.
        """

    def decompose(self):
        """
        Decompose the component into one or more
        contours in the parent glyph. This must raise
        an error if the component does not belong to a glyph.
        """

    # ----
    # Misc
    # ----

    def round(self):
        """
        Round coordinates.

        # XXX define what this rounds. Surely it only rounds offsets?
        """

    def copy(self):
        """
        Copy this component by duplicating the data into
        a component that does not belong to a glyph.
        """
