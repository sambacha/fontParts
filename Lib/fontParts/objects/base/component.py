import weakref
from errors import FontPartsError
from base import BaseObject, TransformationMixin, dynamicProperty

class BaseComponent(BaseObject, TransformationMixin):

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

    glyph = dynamicProperty("glyph", "The component's parent glyph.")

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

    layer = dynamicProperty("layer", "The component's parent layer.")

    def _get_layer(self):
        if self._glyph is None:
            return None
        return self.glyph.layer

    # Font

    font = dynamicProperty("font", "The component's parent font.")

    def _get_font(self):
        if self._glyph is None:
            return None
        return self.glyph.font

    # ----------
    # Attributes
    # ----------

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

    # --------------
    # Transformation
    # --------------

    def _transformBy(self, matrix, origin=None, originOffset=None, **kwargs):
        """
        Subclasses may override this method.
        """
        t = transform.Transform(*matrix)
        transformation = t.transform(self.transformation)
        self.transformation = tuple(transformation)
        if originOffset != (0, 0):
            self.moveBy(originOffset)

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
