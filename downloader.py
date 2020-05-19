import requests as re
import json

ROOT_URL = "https://schedge.a1liu.com/"
SUBJECT_URL = ROOT_URL + "subjects"
sem = "fa"
year = "2020"
sems = ["fa", "su", "sp", "ja"]

res = re.get(SUBJECT_URL)
contents = json.loads(res.content)

data = []

#handle error later
for subject in contents:
    for subjectCode in contents[subject]:
        print("Retrieving course data for " + subjectCode + "-" + subject)
        result = re.get(ROOT_URL + year + "/" + sem + "/" + subject + "/" + subjectCode)
        courses = json.loads(result.content)
        data.append(courses)

with open(year + sem + ".json", "w") as f:
    for course in data:
        if not not course: 
            f.write("%s\n" % course)

