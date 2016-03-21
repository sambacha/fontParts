import os
import defcon
from fontParts.objects.base import BaseFont, FontPartsError
from base import RBaseObject
from kerning import RKerning
from layer import RLayer
from guideline import RGuideline


class RFont(RBaseObject, BaseFont):

    layerClass = RLayer
    kerningClass = RKerning
    guidelineClass = RGuideline

    # ---------------
    # File Operations
    # ---------------

    # Initialize

    def _init(self, pathOrObject=None, showInterface=True, **kwargs):
        if isinstance(pathOrObject, basestring):
            font = defcon.Font(pathOrObject)
        elif pathOrObject is None:
            font = defcon.Font()
        else:
            font = pathOrObject
        self._wrapped = font

    # path

    def _get_path(self, **kwargs):
        return self.naked().path

    # save

    def _save(self, path=None, showProgress=False, formatVersion=None, **kwargs):
        self.naked().save(path=path, formatVersion=formatVersion)

    # close

    def _close(self, **kwargs):
        del self._wrapped

    # -----------
    # Sub-Objects
    # -----------

    def _get_kerning(self):
        return self.kerningClass(wrap=self.naked().kerning)

    # ------
    # Layers
    # ------

    def _get_layers(self, **kwargs):
        return [self.layerClass(wrap=layer) for layer in self.naked().layers]

    # order

    def _get_layerOrder(self, **kwargs):
        return self.naked().layers.layerOrder

    def _set_layerOrder(self, value, **kwargs):
        self.naked().layers.layerOrder = value

    # default layer

    def _get_defaultLayer(self):
        return self.naked().layers.defaultLayer.name

    def _set_defaultLayer(self, value, **kwargs):
        for layer in self.layers:
            if layer.name == value:
                break
        layer = layer.naked()
        self.naked().layers.defaultLayer = layer

    # new

    def _newLayer(self, name, color, **kwargs):
        layers = self.naked().layers
        layer = layers.newLayer(name)
        layer.color = color
        return self.layerClass(wrap=layer)

    # remove

    def _removeLayer(self, name, **kwargs):
        layers = self.naked().layers
        del layers[name]

    # ----------
    # Guidelines
    # ----------

    def _lenGuidelines(self, **kwargs):
        return len(self.naked().info.guidelines)

    def _getGuideline(self, index, **kwargs):
        info = self.naked().info
        guideline = info.guidelines[index]
        return self.guidelineClass(guideline)

    def _appendGuideline(self, position, angle, name=None, color=None, **kwargs):
        info = self.naked().info
        guideline = self.guidelineClass().naked()
        guideline.x = position[0]
        guideline.y = position[1]
        guideline.name = name        
        guideline.color = color
        info.appendGuideline(guideline)
        return self.guidelineClass(guideline)

    def _removeGuideline(self, index, **kwargs):
        info = self.naked().info
        guideline = info.guidelines[index]
        info.removeGuideline(guideline)
