import unittest
from copy import deepcopy

# ---------
# Test Case
# ---------

class BaseTestCase(unittest.TestCase):

    objectProvider = None

    def getTestObjects(self, id):
        data = self.testData[id]
        return self.objectProvider(id, data)


# ---------
# Test Data
# ---------

def registerTestData(registry, id, data):
    data = parseTestDataString(data, registry)
    registry[id] = data

def parseTestDataString(text, registry):
    data = dict(
        objects={},
        description=[]
    )
    for line in text.splitlines():
        line = line.strip()
        line = line.split("#")[0].strip()
        if not line:
            continue
        if line.startswith("+ base: "):
            line = line.split(":", 1)[1].strip()
            baseData = registry[line]
            data.update(deepcopy(baseData))
            data["description"] = baseData["description"].splitlines()
        elif line.startswith("+ object: "):
            line = line.split(":", 1)[1].strip()
            cls, name = line.split("=")
            data["objects"][name.strip()] = cls.strip()
        else:
            data["description"].append(line)
    data["description"] = "\n".join(data["description"])
    return data
