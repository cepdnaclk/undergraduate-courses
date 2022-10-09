# Author: E/18/227 Dinuka Mudalige - e18227@eng.pdn.ac.lk
from importlib.resources import contents
import os
import json

# Delete the existing folder 
dir_path = "../pages/courses/"
try:
    shutil.rmtree(dir_path)
except:
    print("Error: Courses Folder Not Found!")


# Get the list of Semesters 
semesters = json.load(open("../_data/semesters.json"))
courses = json.load(open("../_data/courses.json"))
for semester in semesters:
    dataInJSON = courses[semester]['courses']
    print("- " + courses[semester]['title'] + " -\n")

    for thisCourse in dataInJSON:
        # print(thisCourse)

        course_code = thisCourse["code"]
        # print(course_code)
        # course_title = thisCourse["name"]
        # course_credits = thisCourse["credits"]
        # type = thisCourse["type"]
        prerequisties = thisCourse["prerequisites"] if "prerequisites" in thisCourse else "NULL" 
        # content = thisCourse["content"]
        # objectives = thisCourse["objectives"]
        # ilos_knowledge = thisCourse["ILOs"]["Knowledge"]
        # ilos_skill = thisCourse["ILOs"]["Skill"]
        # ilos_attitude = thisCourse["ILOs"]["Attitude"]

        modules = thisCourse["modules"]
        marks = thisCourse["marks"]
        statistics = thisCourse["statistics"]
        
        pageURL = thisCourse["urls"]["view"]
 
        outputString = f"""---
layout: course
permalink: "{ pageURL }"

title: {thisCourse["name"]}
semester: {semester}
course_code : {thisCourse["code"].upper()} 
course_title : {thisCourse["name"]}

credits : {thisCourse["credits"]}
type : {thisCourse["type"]} 
prerequisites : {prerequisties}
aims_and_objectives: {thisCourse["objectives"]}
ilos_knowledge : {thisCourse["ILOs"]["Knowledge"]}
ilos_skill : {thisCourse["ILOs"]["Skill"]}
ilos_attitude : {thisCourse["ILOs"]["Attitude"]}
modules: {thisCourse["modules"]}
textbooks_references : {thisCourse["references"]}
marks: {marks}
statistics: {statistics}
---"""

        # Write into file
        file_url = f"../pages/courses/{semester}/{course_code.upper()}.html"
        os.makedirs(os.path.dirname(file_url), exist_ok=True)
        htmlFile = open(file_url, "w")
        htmlFile.write(outputString)
        htmlFile.close()
        print("Generated: " + course_code.upper() + ".html")

    print("")
