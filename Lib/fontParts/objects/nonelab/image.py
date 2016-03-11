import defcon
from fontParts.objects.base import BaseImage, FontPartsError
from base import RBaseObject

class RImage(RBaseObject, BaseImage):

    wrapClass = defcon.Image

    def __init__(self, wrap=None):
        if wrap is None:
            wrap = self.wrapClass()
        self._wrapped = wrap

    # ----------
    # Attributes
    # ----------

    # Transformation

    def _get_transformation(self):
        return self.naked().transformation

    def _set_transformation(self, value):
        self.naked().transformation = value

    # Color

    def _get_color(self):
        value = self.naked().color
        if value is not None:
            value = tuple(value)
        return value

    def _set_color(self, value):
        self.naked().color = value

    # Data

    def _get_data(self):
        image = self.naked()
        images = self.font.naked().images
        fileName = image.fileName
        if fileName is None:
            return None
        return images[fileName]

    def _set_data(self, value):
        from ufoLib.validators import pngValidator
        if not pngValidator(data=value):
            raise FontPartsError("The image must be in PNG format.")
        image = self.naked()
        images = image.font.images
        fileName = images.findDuplicateImage(value)
        if fileName is None:
            fileName = images.makeFileName("image")
            images[fileName] = value
        image.fileName = fileName