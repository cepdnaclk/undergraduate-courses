# Author: E/18/227 Dinuka Mudalige - e18227@eng.pdn.ac.lk

from ast import For
import os
import json # to get data from _data/semester#.json
# import requests

if __name__ == "__main__":

    print("Extracting data in _data/courses/semester#.json files to seperate jekyll frontmatters...")

    # select student from json file
    jsonPath = f"../_data/courses/semester1.json"
    dataInJSON = json.load(open(jsonPath))
    for thisCourse in dataInJSON:
        print(thisCourse)
        
    #     outputString = f"""---
    # layout: courses
    # permalink: "/courses/{semester}/{course_code.lower()}/"
    # title: {courseData[COURSE_NAME]}

    # course_number : {course_code.upper()} 
    # course_title : {courseData[COURSE_NAME]}
    # credits : {}
    # core_or_elective : {} 
    # prerequisites : {}
    # aims_objectives : {}
    # ilos_knowledge : {}
    # ilos_skill : {}
    # ilos_attitude : {}
    # textbooks_references : {}
    # ---"""

    #     # write to html file
    #     file_url = "../"+f"pages/courses/{semester}/{course_code.lower()}.html"
    #     os.makedirs(os.path.dirname(file_url), exist_ok=True)
    #     htmlFile = open(file_url, "w")
    #     htmlFile.write(outputString)
    #     htmlFile.close()

    #     print("-------------")