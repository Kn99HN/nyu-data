import requests as re
import json
import sys

ROOT_URL = "https://schedge.a1liu.com/"
SUBJECT_URL = ROOT_URL + "subjects"
sems = ["fa", "su", "sp", "ja"]
res = re.get(SUBJECT_URL)
contents = json.loads(res.content)
data = []

sem = sys.argv[1]
year = sys.argv[2]
if sem not in sems:
    raise ValueError("Invalid semester for " + sem)

#handle error later
for subject in contents:
    for subjectCode in contents[subject]:
        print("Retrieving course data for " + subjectCode + "-" + subject)
        result = re.get(ROOT_URL + year + "/" + sem + "/" + subject + "/" + subjectCode)
        courses = json.loads(result.content)
        if not courses:
            print("No available data for " + subjectCode + "-" + subject)
        else:
            data.append(courses)

with open("data/" + year + sem + ".json", "w") as f:
    for course in data:
        f.write("%s\n" % course)

