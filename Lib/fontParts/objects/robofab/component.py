class BaseComponent(BaseObject):

    # ----------
    # Attributes
    # ----------
    """
    - selected
    - index
    - baseGlyph
    - offset
    - scale
    - transformation
    """

    def __repr__(self):
        pass

    # ----
    # Pens
    # ----

    def draw(self, pen):
        pass

    def drawPoints(self, pen):
        pass

    # ---------------
    # Transformations
    # ---------------

    def transform(matrix):
        """
        Transform this component. (use a Transform matrix object from ``robofab.transform``)

        - don't require a matrix object. accept a tuple.
        """

    def move((x, y)):
        """
        Move the component.
        """

    def scale((x, y), center=(0, 0)):
        """
        Scale the component.
        """

    def rotate(angle, offset=None):
        """
        Rotate the component.

        - the center should be definable.
        """

    def skew(angle, offset=None):
        """
        Skew the component.

        - the center should be definable.
        """

    # ----
    # Misc
    # ----

    def decompose(self):
        pass

    def round(self):
        pass

    def copy(self, aParent=None):
        """
        Duplicate this component
        """