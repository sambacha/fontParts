import weakref
from base import BaseObject, dynamicProperty

class BaseContour(BaseObject):

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

    glyph = dynamicProperty("glyph", "The contour's parent glyph.")

    def _get_glyph(self):
        if self._glyph is None:
            return None
        return self._glyph()

    def _set_glyph(self, glyph):
        assert self._glyph is None
        if glyph is not None:
            glyph = weakref.ref(glyph)
        self._glyph = glyph

    # Font

    font = dynamicProperty("font", "The contour's parent font.")

    def _get_font(self):
        if self._glyph is None:
            return None
        return self.glyph.font

    # Layer

    layer = dynamicProperty("layer", "The contour's parent layer.")

    def _get_layer(self):
        if self._glyph is None:
            return None
        return self.glyph.layer

    # --------------
    # Identification
    # --------------

    index = dynamicProperty("index", "The index of the contour within the ordered list of the parent glyph's contours. XXX -1 (or None?) if the contour does not belong to a glyph.")

    def _get_index(self):
        self.raiseNotImplementedError()

    def _set_index(self, value):
        self.raiseNotImplementedError()

    identifier = dynamicProperty("identifier", "The unique identifier for the contour.")

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

    # ------------------
    # Data normalization
    # ------------------

    def autoStartSegment(self):
        """
        Automatically set the segment with on curve in the
        lower left of the contour as the first segment.
        """

    def round(self):
        """
        Round coordinates in all points.
        """

    # ---------------
    # Transformations
    # ---------------

    def transform(self, matrix):
        """
        Transform the contour with the transformation matrix.
        The matrix must be a tuple defining a 2x2 transformation
        plus offset, aka Affine transform.
        """

    def move(self, value):
        """
        Move the contour by value. Value must
        be a tuple defining x and y values.
        """

    def scale(self, value, center=None):
        """
        Scale the contour by value. Value must be a
        tuple defining x and y values or a number.

        center defines the (x, y) point at which the
        scale should originate. The default is (0, 0).
        """

    def rotate(self, angle, offset=None):
        """
        Rotate the contour by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the rotation.
        """

    def skew(self, angle, offset=None):
        """
        Skew the contour by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the skew.
        """

    # ---------
    # Direction
    # ---------

    clockwise = dynamicProperty("clockwise", "Boolean indicating if the contour's winding direction is clockwise.")

    def _get_clockwise(self):
        self.raiseNotImplementedError()

    def _set_clockwise(self):
        pass

    def reverseContour(self):
        """
        Reverse the direction of the contour.
        """

    # ------------
    # Data Queries
    # ------------

    def pointInside(self, point, evenOdd=0):
        """
        Determine if point is in the black or white of the contour.

        point must be an (x, y) tuple.
        XXX define evenOdd
        """

    box = dynamicProperty("box", "The bounding box of the contour: (xMin, yMin, xMax, yMax) or None.")

    def _get_box(self):
        """
        XXX

        The object returned should let None be the same as (0, 0, 0, 0)
        because lots of things want to know None but for backwards compatibility
        we can't switch to returning None.
        (Currently if there are no outlines, None is returned in some environments and (0, 0, 0, 0) in others)

        XXX
        """

    # ----
    # Misc
    # ----

    def copy(self):
        """
        Copy this contour by duplicating the data into
        a contour that does not belong to a glyph.
        """

    # --------
    # Segments
    # --------

    def __getitem__(self, index):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    segments = dynamicProperty("segments")

    def _get_segments(self):
        self.raiseNotImplementedError()

    def appendSegment(self, segmentType, points, smooth=False):
        """
        Append a segment to the contour.
        """

    def insertSegment(self, index, segmentType, points, smooth=False):
        """
        Insert a segment into the contour.
        """

    def removeSegment(self, index):
        """
        Remove a segment from the contour.
        """

    def setStartSegment(self, index):
        """
        Set the first segment on the contour.
        """

    # -------
    # bPoints
    # -------

    bPoints = dynamicProperty("bPoints")

    def _get_bPoints(self):
        self.raiseNotImplementedError()

    def appendBPoint(self, pointType, anchor, bcpIn=None, bcpOut=None):
        """
        Append a bPoint to the contour.

        XXX explain the args and defaults
        """

    def insertBPoint(self, index, pointType, anchor, bcpIn=None, bcpOut=None):
        """
        Insert a bPoint at index in the contour.

        XXX explain the args and defaults
        """

    # ------
    # Points
    # ------

    points = dynamicProperty("points")

    def _get_points(self):
        self.raiseNotImplementedError()
