# Author: E/18/227 Dinuka Mudalige - e18227@eng.pdn.ac.lk

from importlib.resources import contents
import os
import json # to get data from _data/courses/semester#.json
# import requests

if __name__ == "__main__":

    print("Extracting data in _data/courses/semester#.json files to create jekyll frontmatters...")

    # jsonPath = f"../_data/courses/semester3.json"
    # dataInJSON = json.load(open(jsonPath))
    dataInJSON = json.load(open("_data/courses/semester3.json"))

    for thisCourse in dataInJSON:
        # print(thisCourse)

        course_code = thisCourse["code"]
        # print(course_code)

        # course_title = thisCourse["name"]
        # course_credits = thisCourse["credits"]
        # core_or_elective = thisCourse["type"]
        # prerequisties = thisCourse["prerequisites"]

        # content = thisCourse["content"]
        # objectives = thisCourse["objectives"]

        # ilos_knowledge = thisCourse["ILOs"]["Knowledge"]
        # ilos_skill = thisCourse["ILOs"]["Skill"]
        # ilos_attitude = thisCourse["ILOs"]["Attitude"]

        modulesList = list()
        ml = list()
        modules = thisCourse["modules"]

        for module in modules:
            ml.append(module["topic"])
            ml.append(module["description"])
            ml.append(module["allocation"]["L"])
            ml.append(module["allocation"]["T"])
            ml.append(module["allocation"]["P"])
            ml.append(module["allocation"]["A"])
            modulesList.append(ml)
            ml = list()



        marksList = list()
        markl = list()
        marks = thisCourse["marks"]

        for mark in marks:
            markl.append(mark["description"])
            markl.append(mark["allocation"])
            marksList.append(markl)
            markl = list()
        # textbooks_references = thisCourse["references"]
        # practicals_marks = thisCourse["marks"]["Practicals"]
        # assignments_marks = thisCourse["marks"]["Assignments"]
        # mid_exam_marks = thisCourse["marks"]["Mid-Exam"]
        # end_exam_marks = thisCourse["marks"]["End-Exam"]

        # lecturers = thisCourse["lecturers"]
        
        outputString = f"""---
layout: courses
permalink: "/courses/semester3/{thisCourse["code"].lower()}/"
title: {thisCourse["name"]}

course_number : {thisCourse["code"].upper()} 
course_title : {thisCourse["name"]}
credits : {thisCourse["credits"]}
core_or_elective : {thisCourse["type"]} 
prerequisites : {thisCourse["prerequisites"]}

aims_and_objectives: {thisCourse["objectives"]}

ilos_knowledge : {thisCourse["ILOs"]["Knowledge"]}
ilos_skill : {thisCourse["ILOs"]["Skill"]}
ilos_attitude : {thisCourse["ILOs"]["Attitude"]}

modules: {modulesList}

textbooks_references : {thisCourse["references"]}

marks: {marksList}
---"""
        # print(outputString)

        # write to html file (jekyll frontmatter)
        # file_url = "../"+f"pages/courses/semester3/{course_code.lower()}.html"
        file_url = f"pages/courses/semester3/{course_code.lower()}.html"
        os.makedirs(os.path.dirname(file_url), exist_ok=True)
        htmlFile = open(file_url, "w")
        htmlFile.write(outputString)
        htmlFile.close()
        print("Create or Update file: " + course_code.lower() + ".html")
        print("---------------------------------")
