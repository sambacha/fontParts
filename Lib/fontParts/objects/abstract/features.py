from base import BaseObject, dynamicProperty

class BaseFeatures(BaseObject):

    text = dynamicProperty("text", ".fea formatted text representing the features.")

    def _get_text(self):
        self.raiseNotImplementedError()

    def _set_text(self, value):
        self.raiseNotImplementedError()
