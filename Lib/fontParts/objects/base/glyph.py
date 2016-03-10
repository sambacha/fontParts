import weakref
from base import BaseObject, dynamicProperty, FontPartsError
import validators
from color import Color

class BaseGlyph(BaseObject):

    """
    XXX

    - angledLeftMargin (add this?)
    - angledRightMargin (add this?)

    XXX
    """

    def copy(self):
        """
        Copy this glyph by duplicating the data into
        a glyph that does not belong to a font.
        """

    # -------
    # Parents
    # -------

    def getParent(self):
        """
        This is a backwards compatibility method.
        """
        return self.font

    # Layer

    _layer = None

    layer = dynamicProperty("layer", "The glyph's parent layer.")

    def _get_layer(self):
        if self._layer is None:
            return None
        return self._layer()

    def _set_layer(self, layer):
        assert self._layer is None
        if layer is not None:
            layer = weakref.ref(layer)
        self._layer = layer

    # Font

    font = dynamicProperty("font", "The glyph's parent font.")

    def _get_font(self):
        if self._layer is None:
            return None
        return self.layer.font

    # --------------
    # Identification
    # --------------

    # Name

    name = dynamicProperty("base_name", "The glyph's name.")

    def _get_base_name(self):
        value = self._get_name()
        if value is not None:
            value = validators.validateGlyphName(value)
        return value

    def _set_base_name(self, value):
        if value == self.name:
            return
        value = validators.validateGlyphName(value)
        layer = self.layer
        if value in layer:
            raise FontPartsError("A glyph with the name %r already exists." % value)
        self._set_name(value)

    def _get_name(self):
        """
        Get the name of the glyph.
        This must return a unicode string.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_name(self, value):
        """
        Set the name of the glyph.
        This will be a unicode string.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # Unicodes

    unicodes = dynamicProperty("base_unicodes", "The glyph's unicode values in order from most to least important.")

    def _get_base_unicodes(self):
        value = self._get_unicodes()
        value = validators.validateGlyphUnicodes(value)
        value = tuple(value)
        return value

    def _set_base_unicodes(self, value):
        value = validators.validateGlyphUnicodes(value)
        value = list(value)
        self._set_unicodes(value)

    def _get_unicodes(self):
        """
        Get the unicodes assigned to the glyph.
        This must return a list of zero or more integers.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_unicodes(self, value):
        """
        Assign the unicodes to the glyph.
        This will be a list of zero or more integers.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    unicode = dynamicProperty("base_unicode", "The glyph's primary unicode value.")

    def _get_base_unicode(self):
        value = self._get_unicode()
        if value is not None:
            value = validators.validateGlyphUnicode(value)
        return value

    def _set_base_unicode(self, value):
        if value is not None:
            value = validators.validateGlyphUnicode(value)
        self._set_unicode(value)

    def _get_unicode(self):
        """
        Get the primary unicode assigned to the glyph.
        This must return an integer or None.

        Subclasses may override this method.
        """
        values = self.unicodes
        if values:
            return values[0]
        return None

    def _set_unicode(self, value):
        """
        Assign the primary unicode to the glyph.
        This will be an integer or None.

        Subclasses may override this method.
        """
        values = list(self.unicodes)
        if value in values:
            values.remove(value)
        values.insert(0, value)
        self.unicodes = values

    def autoUnicodes(self):
        """
        Use heuristics to determine the Unicode values for the glyph.
        Environments will define their own heuristics for automatically
        determining values.
        """
        self.raiseNotImplementedError()

    # -------
    # Metrics
    # -------

    # horizontal

    width = dynamicProperty("base_width", "The glyph's width.")

    def _get_base_width(self):
        value = self._get_width()
        value = validators.validateGlyphWidth(value)
        return value

    def _set_base_width(self, value):
        value = validators.validateGlyphWidth(value)
        self._set_width(value)

    def _get_width(self):
        """
        This must return an int or float.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_width(self, value):
        """
        value will be an int or float.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    leftMargin = dynamicProperty("base_leftMargin", "The glyph's left margin.")

    def _get_base_leftMargin(self):
        value = self._get_leftMargin()
        value = validators.validateGlyphLeftMargin(value)
        return value

    def _set_base_leftMargin(self, value):
        value = validators.validateGlyphLeftMargin(value)
        self._set_leftMargin(value)

    def _get_leftMargin(self):
        """
        This must return an int or float.

        XXX define equation

        Subclasses may override this method.
        """
        xMin, yMin, xMax, yMax = self.box
        return xMin

    def _set_leftMargin(self, value):
        """
        value will be an int or float.

        XXX define equation

        Subclasses may override this method.
        """
        diff = value - self.leftMargin
        self.move((diff, 0))
        self.width += diff

    rightMargin = dynamicProperty("base_rightMargin", "The glyph's right margin.")

    def _get_base_rightMargin(self):
        value = self._get_rightMargin()
        value = validators.validateGlyphRightMargin(value)
        return value

    def _set_base_rightMargin(self, value):
        value = validators.validateGlyphRightMargin(value)
        self._set_rightMargin(value)

    def _get_rightMargin(self):
        """
        This must return an int or float.

        XXX define equation

        Subclasses may override this method.
        """
        xMin, yMin, xMax, yMax = self.box
        if xMin == 0 and xMax == 0:
            return self.width
        return self.width - xMax

    def _set_rightMargin(self, value):
        """
        value will be an int or float.

        XXX define equation

        Subclasses may override this method.
        """
        xMin, yMin, xMax, yMax = self.box
        if xMin == 0 and xMax == 0:
            self.width = value
        else:
            self.width = xMax + value

    # vertical

    height = dynamicProperty("base_height", "The glyph's height.")

    def _get_base_height(self):
        value = self._get_height()
        value = validators.validateGlyphHeight(value)
        return value

    def _set_base_width(self, value):
        value = validators.validateGlyphHeight(value)
        self._set_height(value)

    def _get_height(self):
        """
        This must return an int or float.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_height(self, value):
        """
        value will be an int or float.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    bottomMargin = dynamicProperty("base_bottomMargin", "The glyph's bottom margin.")

    def _get_base_bottomMargin(self):
        value = self._get_bottomMargin()
        value = validators.validateGlyphBottomMargin(value)
        return value

    def _set_base_bottomMargin(self, value):
        value = validators.validateGlyphBottomMargin(value)
        self._set_bottomMargin(value)

    def _get_bottomMargin(self):
        """
        This must return an int or float.

        XXX define equation

        Subclasses may override this method.
        """
        xMin, yMin, xMax, yMax = self.box
        return yMin

    def _set_bottomMargin(self, value):
        """
        value will be an int or float.

        XXX define equation

        Subclasses may override this method.
        """
        diff = value - self.bottomMargin
        self.move((0, diff))
        self.height += diff

    topMargin = dynamicProperty("base_topMargin", "The glyph's top margin.")

    def _get_base_topMargin(self):
        value = self._get_topMargin()
        value = validators.validateGlyphTopMargin(value)
        return value

    def _set_base_rightMargin(self, value):
        value = validators.validateGlyphTopMargin(value)
        self._set_topMargin(value)

    def _get_topMargin(self):
        """
        This must return an int or float.

        XXX define equation

        Subclasses may override this method.
        """
        xMin, yMin, xMax, yMax = self.box
        if yMin == 0 and yMax == 0:
            return self.height
        return self.height - yMax

    def _set_topMargin(self, value):
        """
        value will be an int or float.

        XXX define equation

        Subclasses may override this method.
        """
        xMin, yMin, xMax, yMax = self.box
        if yMin == 0 and yMax == 0:
            self.height = value
        else:
            self.height = yMax + value

    # ----
    # Pens
    # ----

    def getPen(self):
        """
        Return a Pen object for modifying the glyph.
        """
        self.raiseNotImplementedError()

    def getPointPen(self):
        """
        Return a PointPen object for modifying the glyph.
        """
        self.raiseNotImplementedError()

    def draw(self, pen, contours=True, components=True):
        """
        Draw the glyph with the given Pen.
        """

    def drawPoints(self, pen, contours=True, components=True):
        """
        Draw the glyph with the given PointPen.
        """

    # -----------------------------------------
    # Contour, Component and Anchor Interaction
    # -----------------------------------------

    def clear(self, contours=True, components=True, anchors=True, guidelines=True):
        """
        Clear all contours, components, anchors and guidelines from the glyph.
        """
        self._clear()

    def _clear(self, contours=True, components=True, anchors=True, guidelines=True):
        """
        Subclasses may override this method.
        """
        if contours:
            self.clearContours()
        if components:
            self.clearComponents()
        if anchors:
            self.clearAnchors()
        if guidelines:
            self.clearGuidelines()

    def appendGlyph(self, other, offset=None):
        """
        Append copies of the contours, components,
        anchors and guidelines from other.

        offset indicates the offset that should
        be applied to the appended data. The default
        is (0, 0).
        """

    # Contours

    def _setGlyphInContour(self, contour):
        if contour.glyph is None:
            contour.glyph = self

    contours = dynamicProperty("contours")

    def _get_contours(self):
        """
        Subclasses may override this method.
        """
        return tuple([self[i] for i in range(len(self))])

    def __len__(self):
        """
        The number of contours in the glyph.
        """
        return self._lenContours()

    def _lenContours(self, **kwargs):
        """
        This must return an integer.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def __iter__(self):
        """
        Iterate through the contours in the glyph.
        """
        return self._iter()

    def _iterContours(self, **kwargs):
        """
        This must return an iterator that returns wrapped contours.

        Subclasses may override this method.
        """
        count = len(self)
        index = 0
        while count:
            yield self[index]
            count -= 1
            index += 1

    def __getitem__(self, index):
        """
        Get the contour located at index from the glyph.
        """
        index = validators.validateContourIndex(index)
        if index >= len(self):
            raise FontPartsError("No contour located at index %d." % index)
        contour = self._getContour(index)
        self._setGlyphInContour(contour)
        return contour

    def _getContour(self, index, **kwargs):
        """
        This must return a wrapped contour.

        index will be a valid index.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def appendContour(self, contour, offset=None):
        """
        A copy of the given contour to the glyph.

        offset indicates the distance that the
        contour should be offset when added to
        the glyph. The default is (0, 0).

        XXX need to define what data comes in from the contour.
        """
        contour = validateContour(contour)
        if offset is None:
            offset = (0, 0)
        offset = validators.validateTransformationOffset(offset)
        return self._appendContour(contour, offset)

    def _appendContour(self, contour, offset=None, **kwargs):
        """
        contour will be an object with a drawPoints method.

        offset will be a valid offset (x, y).

        This must return the new contour.

        Subclasses may override this method.
        """
        copy = contour.copy()
        if offset != (0, 0):
            copy.move(offset)
        pointPen = self.getPointPen()
        contour.drawPoints(pointPen)
        return self[-1]

    def removeContour(self, index):
        """
        Remove the contour with index from the glyph.
        """
        index = validators.validateContourIndex(index)
        if index >= len(self):
            raise FontPartsError("No contour located at index %d." % index)
        self._removeContour(index)

    def _removeContour(self, index, **kwargs):
        """
        index will be a valid index.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def clearContours(self):
        """
        Clear all contours.
        """
        self._clearContours()

    def _clearContours(self):
        """
        Subclasses may override this method.
        """
        for i in range(len(self)):
            self.removeContour(-1)

    def removeOverlap(self):
        """
        Perform a remove overlap operation on the contours.
        """
        self.raiseNotImplementedError()

    # Components

    def _setGlyphInComponent(self, component):
        if component.glyph is None:
            component.glyph = self

    components = dynamicProperty("components")

    def _get_components(self):
        """
        Subclasses may override this method.
        """
        return tuple([self._getitem__component(i) for i in range(self._len__components())])

    def _len__components(self):
        return self._lenComponents()

    def _lenComponents(self, **kwargs):
        """
        This must return an integer indicating
        the number of components in the glyph.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _getitem__component(self, index):
        index = validators.validateComponentIndex(index)
        if index >= self._len__components():
            raise FontPartsError("No component located at index %d." % index)
        component = self._getComponent(index)
        self._setGlyphInComponent(component)
        return component

    def _getComponent(self, index, **kwargs):
        """
        This must return a wrapped contour.

        index will be a valid index.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _getComponentIndex(self, component):
        for i, other in enumerate(self.components):
            if component == other:
                return i
        raise FontPartsError("The component could not be found.")

    def appendComponent(self, baseGlyph, offset=None, scale=None):
        """
        Append a new component to the glyph.

        baseGlyph indicates the glyph that the
        component will reference.

        offset indictaes the offset that should
        be defined in the component. The default
        is (0, 0).

        scale indicates the scale that should be
        defined in the component. The default is
        (1.0, 1.0).

        XXX need to define what data comes in from the component.
        """
        baseGlyph = validators.validateGlyphName(baseGlyph)
        if self.name == baseGlyph:
            raise FontPartsError("A glyph cannot contain a component referencing itself.")
        if offset is None:
            offset = (0, 0)
        if scale is None:
            scale = (1, 1)
        offset = validators.validateTransformationOffset(offset)
        scale = validators.validateTransformationScale(scale)
        return self._appendComponent(baseGlyph, offset=offset, scale=scale)

    def _appendComponent(self, baseGlyph, offset=None, scale=None, **kwargs):
        """
        baseGlyph will be a valid glyph name.
        The baseGlyph may or may not be in the layer.

        offset will be a valid offset (x, y).
        scale will be a valid scale (x, y).

        This must return the new component.

        Subclasses may override this method.
        """
        ox, oy = offset
        sx, sy = scale
        transformation = (sx, 0, 0, sy, ox, oy)
        pointPen = self.getPointPen()
        pointPen.addComponent(baseGlyph, transformation=transformation)
        return self.components[-1]

    def removeComponent(self, component):
        """
        Remove component from the glyph.

        component can be a component object or an
        integer representing the component index.
        """
        if isinstance(component, int):
            index = component
        else:
            index = self._getComponentIndex(component)
        index = validators.validateComponentIndex(index)
        if index >= self._len__components():
            raise FontPartsError("No component located at index %d." % index)
        self._removeComponent(index)

    def _removeComponent(self, index, **kwargs):
        """
        index will be a valid index.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def clearComponents(self):
        """
        Clear all components.
        """
        self._clearComponents()

    def _clearComponents(self):
        """
        Subclasses may override this method.
        """
        for i in range(self._len__components()):
            self.removeComponent(-1)

    def decompose(self):
        """
        Decompose all components.
        """

    # Anchors

    def _setGlyphInAnchor(self, anchor):
        if anchor.glyph is None:
            anchor.glyph = self

    anchors = dynamicProperty("anchors")

    def _get_anchors(self):
        """
        Subclasses may override this method.
        """
        return tuple([self._getitem__anchor(i) for i in range(self._len__anchors())])

    def _len__anchors(self):
        return self._lenAnchors()

    def _lenAnchors(self, **kwargs):
        """
        This must return an integer indicating
        the number of anchors in the glyph.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _getitem__anchor(self, index):
        index = validators.validateAnchorIndex(index)
        if index >= self._len__anchors():
            raise FontPartsError("No anchor located at index %d." % index)
        anchor = self._getAnchor(index)
        self._setGlyphInAnchor(anchor)
        return anchor

    def _getAnchor(self, index, **kwargs):
        """
        This must return a wrapped anchor.

        index will be a valid index.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _getAnchorIndex(self, anchor):
        for i, other in enumerate(self.anchors):
            if anchor == other:
                return i
        raise FontPartsError("The anchor could not be found.")

    def appendAnchor(self, name, position, color=None):
        """
        Append a new anchor to the glyph.

        name indicates the name that should be
        assigned to the anchor.

        position is an (x, y) tuple defining
        the position for the anchor.

        color is None or a color tuple.
        """
        name = validators.validateAnchorName(name)
        position = validators.validateCoordinateTuple(position)
        if color is not None:
            color = validators.validateColor(color)
        return self._appendAnchor(name, position=position, color=color)

    def _appendAnchor(self, name, position=None, color=None, **kwargs):
        """
        name will be a valid anchor name.
        position will be a valid position (x, y).
        color will be None or a valid color.

        This must return the new anchor.

        Subclasses may override this method.
        """
        self.raiseNotImplementedError()

    def removeAnchor(self, anchor):
        """
        Remove anchor from the glyph.

        anchor can be a anchor object or an
        integer representing the anchor index.
        """
        if isinstance(anchor, int):
            index = anchor
        else:
            index = self._getAnchorIndex(anchor)
        index = validators.validateAnchorIndex(index)
        if index >= self._len__anchors():
            raise FontPartsError("No anchor located at index %d." % index)
        self._removeAnchor(index)

    def _removeAnchor(self, index, **kwargs):
        """
        index will be a valid index.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def clearAnchors(self):
        """
        Clear all anchors.
        """
        self._clearAnchors()

    def _clearAnchors(self):
        """
        Subclasses may override this method.
        """
        for i in range(self._len__anchors()):
            self.removeAnchor(-1)

    # ----------
    # Guidelines
    # ----------

    def _setGlyphInGuideline(self, guideline):
        if guideline.glyph is None:
            guideline.glyph = self

    guidelines = dynamicProperty("guidelines")

    def _get_guidelines(self):
        """
        Subclasses may override this method.
        """
        return tuple([self._getitem__guideline(i) for i in range(self._len__guidelines())])

    def _len__guidelines(self):
        return self._lenGuidelines()

    def _lenGuidelines(self, **kwargs):
        """
        This must return an integer indicating
        the number of guidelines in the glyph.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _getitem__guideline(self, index):
        index = validators.validateGuidelineIndex(index)
        if index >= self._len__guidelines():
            raise FontPartsError("No guideline located at index %d." % index)
        guideline = self._getGuideline(index)
        self._setGlyphInGuideline(guideline)
        return guideline

    def _getGuideline(self, index, **kwargs):
        """
        This must return a wrapped guideline.

        index will be a valid index.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _getGuidelineIndex(self, guideline):
        for i, other in enumerate(self.guidelines):
            if guideline == other:
                return i
        raise FontPartsError("The guideline could not be found.")

    def appendGuideline(self, position, angle, name=None, color=None):
        """
        Append a new guideline to the glyph.

        position (x, y) indicates the position of the guideline.

        angle indicates the angle of the guideline.

        name indicates the name for the guideline.

        color indicates the color for the guideline.
        """
        position = validators.validateCoordinateTuple(position)
        angle = validators.validateGuidelineAngle(angle)
        if name is not None:
            name = validators.validateGuidelineName(name)
        if color is not None:
            color = validators.validateColor(color)
        return self._appendGuideline(position, angle, name=name, color=color)

    def _appendGuideline(self, position, angle, name=None, color=None, **kwargs):
        """
        position will be a valid position (x, y).
        angle will be a valida angle.
        name will be a valid guideline name or None.
        color will be None or a valid color.

        This must return the new guideline.

        Subclasses may override this method.
        """
        self.raiseNotImplementedError()

    def removeGuideline(self, guideline):
        """
        Remove guideline from the glyph.

        guideline can be a guideline object or an
        integer representing the guideline index.
        """
        if isinstance(guideline, int):
            index = guideline
        else:
            index = self._getGuidelineIndex(anchor)
        index = validators.validateGuidelineIndex(index)
        if index >= self._len__guidelines():
            raise FontPartsError("No guideline located at index %d." % index)
        self._removeGuideline(index)

    def _removeGuideline(self, index, **kwargs):
        """
        index will be a valid index.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def clearGuidelines(self):
        """
        Clear all guidelines.
        """
        self._clearGuidelines()

    def _clearGuidelines(self):
        """
        Subclasses may override this method.
        """
        for i in range(self._len__guidelines()):
            self.removeGuideline(-1)

    # ------------------
    # Data Normalization
    # ------------------

    def round(self):
        """
        Round coordinates in all contours, components, anchors and guidelines.
        """

    def correctDirection(self, trueType=False):
        """
        Correct the direction of the contours in the glyph.
        """

    def autoContourOrder(self):
        """
        Sort the contours based on their centers.
        """

    # ---------------
    # Transformations
    # ---------------

    def transform(self, matrix, contours=True, components=True, anchors=True, guidelines=True):
        """
        Transform the glyph with the transformation matrix.
        The matrix must be a tuple defining a 2x2 transformation
        plus offset, aka Affine transform.
        """

    def move(self, value, contours=True, components=True, anchors=True, guidelines=True):
        """
        Move the contours, components, anchors and guidelines
        in the glyph by value. Value must be a tuple
        defining x and y values.
        """

    def scale((x, y), center=None, contours=True, components=True, anchors=True, guidelines=True):
        """
        Scale the contours, components, anchors and guidelines
        in the glyph by value. Value must be a tuple
        defining x and y values or a number.

        center defines the (x, y) point at which the
        scale should originate. The default is (0, 0).
        """

    def rotate(self, angle, offset=None, contours=True, components=True, anchors=True, guidelines=True):
        """
        Rotate the contours, components, anchors and guidelines
        in the glyph by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the rotation.
        """

    def skew(self, angle, offset=None, contours=True, components=True, anchors=True, guidelines=True):
        """
        Skew the contours, components, anchors and guidelines
        in the glyph by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the skew.
        """

    # -------------
    # Interpolation
    # -------------

    def interpolate(self, factor, minGlyph, maxGlyph, suppressError=True, analyzeOnly=False):
        """
        Interpolate all possible data in the glyph. The interpolation
        occurs on a 0 to 1.0 range where minGlyph is located at
        0 and maxGlyph is located at 1.0.

        factor is the interpolation value. It may be less than 0
        and greater than 1.0. It may be a number (integer, float)
        or a tuple of two numbers. If it is a tuple, the first
        number indicates the x factor and the second number
        indicates the y factor.

        suppressError indicates if incompatible data should be ignored
        or if an error should be raised when such incompatibilities are found.

        analyzeOnly indicates if the intrpolation should only be a
        compatibiltiy check with no interpolation actually performed.
        If this is True, a dict of compatibility problems will
        be returned.
        """

    def isCompatible(self, otherGlyph, report=True):
        """
        Returns a boolean indicating if the glyph is compatible for
        interpolation with otherGlyph. If report is True, a list
        of errors will be returned with the boolean.
        """

    # ------------
    # Data Queries
    # ------------

    def pointInside(self, point, evenOdd=False):
        """
        Determine if point is in the black or white of the glyph.

        point must be an (x, y) tuple.
        XXX define evenOdd
        """

    box = dynamicProperty("box", "The bounding box of the glyph: (xMin, yMin, xMax, yMax) or None.")

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

    # -----------------
    # Layer Interaction
    # -----------------

    layers = dynamicProperty("layers", "The glyph's layers. Each layer will be a glyph object.")

    def _get_layers(self):
        """
        XXX

        this needs to return a special immutable list
        only len, __iter__ and __getitem__ should work.
        we don't want that list being manipulated.
        manipulation should happen in the font/glyph.

        XXX
        """
        self.raiseNotImplementedError()

    def getLayer(self, name):
        """
        Get the layer with name.
        """

    def newLayer(self, name, color=None):
        """
        Make a new layer with name and color.
        """
        self.raiseNotImplementedError()

    def removeLayer(self, layer):
        """
        Remove the layer from the glyph (not the font).
        """
        self.raiseNotImplementedError()

    # ----
    # Misc
    # ----

    markColor = dynamicProperty("base_markColor", "The mark color for the glyph.")

    def _get_base_markColor(self):
        value = self._get_markColor()
        if value is not None:
            value = validators.validateColor(value)
            value = Color(value)
        return value

    def _set_base_markColor(self, value):
        if value is not None:
            value = validators.validateColor(value)
        self._set_markColor(value)

    def _get_markColor(self):
        """
        Return the mark color value as a color tuple or None.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    def _set_markColor(self, value):
        """
        value will be a color tuple or None.

        Subclasses must override this method.
        """
        self.raiseNotImplementedError()

    # Note

    note = dynamicProperty("note", "A note for the glyph.")

    def _get_note(self):
        self.raiseNotImplementedError()

    def _set_note(self, value):
        self.raiseNotImplementedError()

    # Lib

    lib = dynamicProperty("lib", "The lib for the glyph.")

    def _get_lib(self):
        self.raiseNotImplementedError()

    # Image

    image = dynamicProperty("image", "The image for the glyph.")

    def _get_image(self):
        self.raiseNotImplementedError()

    def _set_image(self, value):
        self.raiseNotImplementedError()
