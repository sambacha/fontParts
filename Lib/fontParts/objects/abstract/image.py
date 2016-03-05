from base import BaseObject, dynamicProperty

color = image.color
image.color = color
data = image.data
image.data = data

class BaseImage(BaseObject):

    def __repr__(self):
        pass

    # Name

    name = dynamicProperty("name", "The image's name.")

    def _get_name(self):
        self.raiseNotImplementedError()

    def _set_name(self, value):
        self.raiseNotImplementedError()

    # Transformation

    transformation = dynamicProperty("transformation", "The image's transformation matrix.")

    def _get_transformation(self):
        self.raiseNotImplementedError()

    def _set_transformation(self, value):
        self.raiseNotImplementedError()

    offset = dynamicProperty("offset", "The image's offset.")

    def _get_offset(self):
        pass

    def _set_offset(self, value):
        pass

    scale = dynamicProperty("scale", "The image's scale.")

    def _get_scale(self):
        pass

    def _set_scale(self, value):
        pass

    # Color

    color = dynamicProperty("color", "The image's color. XXX need to determine the data type")

    def _get_color(self):
        self.raiseNotImplementedError()

    def _set_color(self):
        self.raiseNotImplementedError()

    # Data

    data = dynamicProperty("data", "The image's raw byte data in PNG format.")

    def _get_data(self):
        self.raiseNotImplementedError()

    def _set_data(self):
        self.raiseNotImplementedError()

    # ---------------
    # Transformations
    # ---------------

    def transform(self, matrix):
        """
        Transform the image with the transformation matrix.
        The matrix must be a tuple defining a 2x2 transformation
        plus offset, aka Affine transform.
        """

    def move(self, value):
        """
        Move the image by value. Value must
        be a tuple defining x and y values.
        """

    def scale(self, value, center=None):
        """
        Scale the image by value. Value must be a
        tuple defining x and y values.

        center defines the (x, y) point at which the
        scale should originate. The default is (0, 0).
        """

    def rotate(self, angle, offset=None):
        """
        Rotate the image by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the rotation.
        """

    def skew(self, angle, offset=None):
        """
        Skew the image by angle.

        XXX define angle parameters.
        XXX is anything using offset?
        XXX it should be possible to define the center point for the skew.
        """

    # ----
    # Misc
    # ----

    def copy(self):
        """
        Copy this image by duplicating the data into
        a image that does not belong to a glyph.
        """
