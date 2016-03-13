import weakref
from base import BaseObject, dynamicProperty, FontPartsError
import validators

class BaseContour(BaseObject):

    def copy(self):
        """
        Copy this contour by duplicating the data into
        a contour that does not belong to a glyph.
        """

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

    # index

    index = dynamicProperty("base_index", "The index of the contour within the ordered list of the parent glyph's contours.")

    def _get_base_index(self):
        glyph = self.glyph
        if glyph is None:
            return None
        value = self._get_index()
        value = validators.validateIndex(value)
        return value

    def _set_base_index(self, value):
        glyph = self.glyph
        if glyph is None:
            raise FontPartsError("The contour does not belong to a glyph.")
        value = validators.validateIndex(value)
        contourCount = len(glyph.contours)
        if value < 0:
            value = -(value % contourCount)
        if value >= contourCount:
            value = contourCount
        self._set_index(value)

    def _get_index(self):
        """
        Subclasses may override this method.
        """
        glyph = self.glyph
        return glyph.contours.index(self)

    def _set_index(self, value):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # identifier

    identifier = dynamicProperty("base_identifier", "The unique identifier for the contour.")

    def _get_base_identifier(self):
        value = self._get_identifier()
        if value is not None:
            value = validators.validateIdentifier(value)
        return value

    def _get_identifier(self):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # ----
    # Pens
    # ----

    def draw(self, pen):
        """
        Draw the contour with the given Pen.
        """
        self._draw(pen)

    def _draw(self, pen, **kwargs):
        """
        Subclasses may override this method.
        """
        from ufoLib.pointPen import PointToSegmentPen
        adapter = PointToSegmentPen(pen)
        self.drawPoints(adapter)

    def drawPoints(self, pen):
        """
        Draw the contour with the given PointPen.
        """
        self._drawPoints(pen)

    def _drawPoints(self, pen, **kwargs):
        """
        Subclasses may override this method.
        """
        # The try: ... except TypeError: ...
        # handles backwards compatibility with
        # point pens that have not been upgraded
        # to point pen protocol 2. 
        try:
            pen.beginPath(self.identifier)
        except TypeError:
            pen.beginPath()
        for point in self.points:
            typ = point.type
            if typ == "offcurve":
                typ = None
            try:
                pen.addPoint(pt=(point.x, point.y), segmentType=typ, smooth=point.smooth, identifier=point.identifier)
            except TypeError:
                pen.addPoint(pt=(point.x, point.y), segmentType=typ, smooth=point.smooth)
        pen.endPath()

    # ------------------
    # Data normalization
    # ------------------

    def autoStartSegment(self):
        """
        Automatically set the segment with on curve in the
        lower left of the contour as the first segment.
        """
        self._autoStartSegment()

    def _autoStartSegment(self, **kwargs):
        """
        Subclasses may override this method.

        XXX port this from robofab
        """
        self.raiseNotImplementedError()

    def round(self):
        """
        Round coordinates in all points.
        """
        self._round()

    def _round(self, **kwargs):
        """
        Subclasses may override this method.
        """
        for point in self.points:
            point.round()

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

    clockwise = dynamicProperty("base_clockwise", "Boolean indicating if the contour's winding direction is clockwise.")

    def _get_base_clockwise(self):
        value = self._get_clockwise()
        value = validators.validateBoolean(value)
        return value

    def _set_base_clockwise(self, value):
        value = validators.validateBoolean(value)
        self._set_clockwise(value)

    def _get_clockwise(self):
        """
        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_clockwise(self, value):
        """
        Subclasses may override this method.
        """
        if self.clockwise != value:
            self.reverseContour()

    def reverse(self):
        """
        Reverse the direction of the contour.
        """
        self._reverseContour()

    def _reverse(self, **kwargs):
        """
        Subclasses may override this method.
        """
        self.raiseNotImplementedError()

    # ------------
    # Data Queries
    # ------------

    def pointInside(self, point):
        """
        Determine if point is in the black or white of the contour.

        point must be an (x, y) tuple.
        """
        point = validators.validateCoordinateTuple(point)
        return self._pointInside(point)

    def _pointInside(self, point):
        """
        XXX

        This can be ported from RoboFab.

        XXX
        """
        self.raiseNotImplementedError()

    box = dynamicProperty("box", "The bounding box of the contour: (xMin, yMin, xMax, yMax) or None.")

    def _get_base_box(self):
        value = self._get_box()
        if value is not None:
            value = validators.validateBoundingBox(value)
        return value

    def _get_box(self):
        """
        Subclasses may override this method.
        """
        from fontTools.pens.boundsPen import BoundsPen
        pen = BoundsPen(self.layer)
        self.draw(pen)
        return pen.bounds

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
