from fontParts.nonelab.anchor import RAnchor

classMapping = dict(
    Anchor=RAnchor
)


class BaseTest(object):

    def getCaseObjects(self, id):
        data = self.cases[id]
        namespace = {}
        objects = {}
        for variable, cls in data["objects"].items():
            cls = classMapping[cls]
            obj = cls()
            namespace[variable] = obj
            objects[variable] = obj
        code = data["description"]
        exec code in namespace
        return objects
