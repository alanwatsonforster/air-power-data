import json
import re


def readjsonfile(jsonfilename):
    with open(jsonfilename, "r", encoding="utf-8") as f:
        s = f.read(-1)
        # Strip whole-line // comments.
        r = re.compile("^[ \t]*//.*$", re.MULTILINE)
        s = re.sub(r, "", s)
        return json.loads(s)


alllist = readjsonfile("collections/all.json")
for element in alllist:
    if element[0] == "type":
        typename = element[1]
        with open("types/%s.json" % typename, "w") as f:
            json.dump([["prolog", False], element], f)
