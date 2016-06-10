import unittest
from copy import deepcopy


class BaseTestCase(unittest.TestCase):

    objectProvider = None

    def getTestObjects(self, id):
        data = self.testData[id]
        return self.objectProvider(id, data)


def parseTestDataString(text):
    cases = {}
    currentCase = None
    for line in text.splitlines():
        line = line.split("#")[0].strip()
        if not line:
            continue
        if line == ">>>":
            currentCase = {
                "objects" : {},
                "description" : []
            }
        elif line == "<<<":
            currentCase["description"] = "\n".join(currentCase["description"])
            currentCase = None
        elif line.startswith("+ id: "):
            line = line.split(":", 1)[1].strip()
            cases[line] = currentCase
        elif line.startswith("+ base: "):
            line = line.split(":", 1)[1].strip()
            baseCase = cases[line]
            currentCase.update(deepcopy(baseCase))
            currentCase["description"] = currentCase["description"].splitlines()
        elif line.startswith("+ object: "):
            line = line.split(":", 1)[1].strip()
            cls, name = line.split("=")
            currentCase["objects"][name.strip()] = cls.strip()
        else:
            currentCase["description"].append(line)
    return cases
