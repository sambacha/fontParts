import weakref
from errors import FontPartsError
from base import BaseObject, TransformationMixin, dynamicProperty
import validators

class BaseContour(BaseObject, TransformationMixin):

    segmentClass = None
    bPointClass = None

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
            if typ == "offCurve":
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

    # --------------
    # Transformation
    # --------------

    def _transformBy(self, matrix, origin=None, originOffset=None, **kwargs):
        """
        Subclasses may override this method.
        """
        for point in self.points:
            point.transformBy(matrix, origin=origin)

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

    bounds = dynamicProperty("bounds", "The bounds of the contour: (xMin, yMin, xMax, yMax) or None.")

    def _get_base_bounds(self):
        value = self._get_bounds()
        if value is not None:
            value = validators.validateBoundingBox(value)
        return value

    def _get_bounds(self):
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

    """
    The base class implements the full segment interaction API.
    Subclasses do not need to override anything within the contour
    other than registering segmentClass. Subclasses may choose to
    implement this API independently if desired.
    """

    def _setContourInSegment(self, segment):
        if segment.contour is None:
            segment.contour = self

    segments = dynamicProperty("segments")

    def _get_segments(self):
        """
        Subclasses may override this method.
        """
        segments = [[]]
        lastWasOffCurve = False
        for point in self.points:
            segments[-1].append(point)
            if point.type is not "offCurve":
                segments.append([])
            lastWasOffCurve = point.type is "offCurve"
        if len(segments[-1]) == 0:
            del segments[-1]
        if lastWasOffCurve:
            segment = segments.pop(-1)
            assert len(segments[0]) == 1
            segment.append(segments[0][0])
            del segments[0]
            segments.append(segment)
        elif segments[0][-1].type != "move":
            segment = segments.pop(0)
            segments.append(segment)
        # wrap into segments
        wrapped = []
        for points in segments:
            s = self.segmentClass()
            s._setPoints(points)
            self._setContourInSegment(s)
            wrapped.append(s)
        return wrapped

    def __getitem__(self, index):
        return self.segments[index]

    def __iter__(self):
        return self._iterSegments()

    def _iterSegments(self):
        segments = self.segments
        count = len(segments)
        index = 0
        while count:
            yield segments[index]
            count -= 1
            index += 1

    def __len__(self):
        return self._len__segments()

    def _len__segments(self, **kwargs):
        """
        Subclasses may override this method.
        """
        return len(self.segments)

    def appendSegment(self, type, points, smooth=False):
        """
        Append a segment to the contour.
        """
        type = validators.validateSegmentType(type)
        pts = []
        for pt in points:
            pt = validators.validateCoordinateTuple(pt)
            pts.append(pt)
        points = pts
        smooth = validators.validateBoolean(smooth)
        self._appendSegment(type=type, points=points, smooth=smooth)

    def _appendSegment(self, type=None, points=None, smooth=False, **kwargs):
        """
        Subclasses may override this method.
        """
        self._insertSegment(len(self), type=type, points=points, smooth=smooth)

    def insertSegment(self, index, type, points, smooth=False):
        """
        Insert a segment into the contour.
        """
        index = validators.validateIndex(index)
        type = validators.validateSegmentType(type)
        pts = []
        for pt in points:
            pt = validators.validateCoordinateTuple(pt)
            pts.append(pt)
        points = pts
        smooth = validators.validateBoolean(smooth)
        self._insertSegment(index=index, type=type, points=points, smooth=smooth)

    def _insertSegment(self, index=None, type=None, points=None, smooth=False, **kwargs):
        """
        Subclasses may override this method.
        """
        onCurve = points[-1]
        offCurve = points[:-1]
        self.insertPoint(index, onCurve, type=type, smooth=smooth)
        for point in reversed(offCurve):
            self.insertPoint(index, offCurve, type="offCurve")

    def removeSegment(self, segment):
        """
        Remove segment from the contour.
        """
        if not isinstance(segment, int):
            segment = self.segment.index(point)
        segment = validators.validateIndex(point)
        if segment >= self._len__segments():
            raise FontPartsError("No segment located at index %d." % segment)
        self._removePoint(segment)

    def _removeSegment(self, segment, **kwargs):
        """
        segment will be a valid segment index.

        Subclasses may override this method.
        """
        segment = self.segments[segment]
        for point in segment.points:
            self.removePoint(point)

    def setStartSegment(self, segment):
        """
        Set the first segment on the contour.
        segment can be a segment object or an index.
        """
        segments = self.segments
        if not isinstance(segment, int):
            segmentIndex = segments.index(segment)
        else:
            segmentIndex = segment
        if len(self.segments) < 2:
            return
        if segmentIndex == 0:
            return
        if segmentIndex >= len(segments):
            raise FontPartsError("The contour does not contain a segment at index %d" % segmentIndex)
        self._setStartSegment(segmentIndex)

    def _setStartSegment(self, segmentIndex, **kwargs):
        """
        Subclasses may override this method.
        """
        segments = self.segments
        oldStart = self.segments[0]
        oldLast = self.segments[-1]
        # If the contour ends with a curve on top of a move,
        # delete the move.
        if oldLast.type == "curve" or oldLast.type == "qCurve":
            startOn = oldStart.onCurve
            lastOn = oldLast.onCurve
            if startOn.x == lastOn.x and startOn.y == lastOn.y:
                self.removeSegment(0)
                # Shift new the start index.
                segmentIndex = segmentIndex - 1
                segments = self.segments
        # If the first point is a move, convert it to a line.
        if segments[0].type == "move":
            segments[0].type = "line"
        # Reorder the points internally.
        segments = segments[segmentIndex:] + segments[:segmentIndex]
        points = []
        for segment in segments:
            for point in segment:
                points.append(((point.x, point.y), point.type, point.smooth, point.name, point.identifier))
        # Clear the points.
        for point in self.points:
            self.removePoint(point)
        # Add the points.
        for point in points:
            position, type, smooth, name, identifier = point
            self.appendPoint(
                position,
                type=type,
                smooth=smooth,
                name=name,
                identifier=identifier
            )

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

    def _setContourInPoint(self, point):
        if point.contour is None:
            point.contour = self

    points = dynamicProperty("points")

    def _get_points(self):
        """
        Subclasses may override this method.
        """
        return tuple([self._getitem__points(i) for i in range(self._len__points())])

    def _len__points(self):
        return self._lenPoints()

    def _lenPoints(self, **kwargs):
        """
        This must return an integer indicating
        the number of points in the contour.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _getitem__points(self, index):
        index = validators.validateIndex(index)
        if index >= self._len__points():
            raise FontPartsError("No point located at index %d." % index)
        point = self._getPoint(index)
        self._setContourInPoint(point)
        return point

    def _getPoint(self, index, **kwargs):
        """
        This must return a wrapped point.

        index will be a valid index.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _getPointIndex(self, point):
        for i, other in enumerate(self.points):
            if point == other:
                return i
        raise FontPartsError("The point could not be found.")

    def appendPoint(self, position, type="line", smooth=False, name=None, identifier=None):
        """
        Append a point to the contour.
        """
        self.insertPoint(len(self.points), position=position, type=type, smooth=smooth, name=name, identifier=identifier)

    def insertPoint(self, index, position, type="line", smooth=False, name=None, identifier=None):
        """
        Insert a point into the contour.
        """
        index = validators.validateIndex(index)
        position = validators.validateCoordinateTuple(position)
        type = validators.validatePointType(type)
        smooth = validators.validateBoolean(smooth)
        if name is not None:
            name = validators.validatePointName(name)
        if identifier is not None:
            identifier = validators.validateIdentifier(identifier)
        self._insertPoint(index, position=position, type=type, smooth=smooth, name=name, identifier=identifier)

    def _insertPoint(self, index, position, type="line", smooth=False, name=None, identifier=None):
        """
        position will be a valid position (x, y).
        type will be a valid type.
        smooth will be a valid boolean.
        name will be a valid name or None.
        identifier will be a valid identifier or None.
        The identifier will not have been tested for uniqueness.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def removePoint(self, point):
        """
        Remove the point from the contour.
        point can be a point object or an index.
        """
        if not isinstance(point, int):
            point = self.points.index(point)
        point = validators.validateIndex(point)
        if point >= self._len__points():
            raise FontPartsError("No point located at index %d." % point)
        self._removePoint(point)

    def _removePoint(self, index, **kwargs):
        """
        index will be a valid index.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()
