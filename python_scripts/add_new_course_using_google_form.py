# Author: E/18/227 Dinuka Mudalige - e18227@eng.pdn.ac.lk

import requests
import os
import gdown # pip install gdown
import json # to edit _data/eXX.json
# import add_new_course

courseCSV_link = ""
courseCSV = requests.get(courseCSV_link, headers = {
                            'Cache-Control': 'no-cache'}).text.split("\n")

# index of the CSV parameters
TIMESTAMP = 0
EMAIL = 1
ADMIN_NO = 2
COURSE_CODE = 3
COURSE_NAME = 4
SEMESTER = 5
YEAR = 6
CREDITS = 7
ELECTIVE = 8
DESCRIPTION = 9
ITEM1 = 10
ITEM2 = 11
ITEM3 = 12
ITEM4 = 13
ITEM5 = 14
ITEM6 = 15
ITEM7 = 16

i = 0
if __name__ == "__main__":
    for eachLine in courseCSV:
        courseData = eachLine.replace('\r', '').split(",")
        if len(courseData) != 17:
            print(f"Splitted csv is longer/shorter than it should be! {len(courseData)}")
            quit()

        if ":" not in studentData[0]:
            # if there is no timestamp in this line or this is the header line
            continue         

        # print(courseData)
        print("Processing: " + courseData[COURSE_CODE] + " " + courseData[COURSE_NAME])

        # get course code and semester
        course_code = courseData[COURSE_CODE]
        semester = courseData[SEMESTER]

        permalink = f"/semester/{course_code}"

        # # add 'EMPTY' to all empty fields
        # for i in range(0, URL+1):
        #     if courseData[i] == "":
        #         courseData[i] = "EMPTY"

        outputString = f"""---
layout: courses
permalink: "/courses/{semester}/{course_code.lower()}/"
title: {courseData[COURSE_NAME]}

course_number : {course_code.upper()} 
course_title : {courseData[COURSE_NAME]}
credits : {}
core_elective : {} 
prerequisites : {}
aims_objectives : {}
ilos_knowledge : {}
ilos_skill : {}
ilos_attitude : {}
textbooks_references : {}
---"""

        # write to html file
        file_url = "../"+f"pages/courses/{semester}/{course_code.lower()}.html"
        os.makedirs(os.path.dirname(file_url), exist_ok=True)
        htmlFile = open(file_url, "w")
        htmlFile.write(outputString)
        htmlFile.close()

        print("-------------")

