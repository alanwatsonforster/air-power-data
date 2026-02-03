import glob

for unit in glob.glob("*platoon.json") + glob.glob("*battery.json"):
    base = unit[:-12]
    print(base)
    with open(unit) as f:
        s = f.read()
    s = s.replace("platoon", "section")
    s = s.replace("battery", "section")
    with open(base + "section.json", "w") as f:
        f.write(s)
    s = s.replace("section", "squad")
    with open(base + "squad.json", "w") as f:
        f.write(s)
