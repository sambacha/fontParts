from fontParts.test import testEnvironment
from fontParts.nonelab.anchor import RAnchor

classMapping = dict(
    Anchor=RAnchor
)

def noneLabObjectProvider(id, data):
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

if __name__ == "__main__":
    testEnvironment(noneLabObjectProvider)