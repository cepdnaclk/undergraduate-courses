'''
Author: Nuwan Jaliyagoda

- This script will collect all the JSON files in the directory '/courses', post-process and write into the
single JSON file, './_data/courses.json'. 
- Any validation to the JSON content can be done in this step.

'''

import json 
import os
import subprocess
from datetime import datetime

def getLastEditDate(filename):
    fileLastEditedDateSTR = str(subprocess.run(['git', 'log', '-1', '--pretty="format:%ci"', course_file], stdout=subprocess.PIPE).stdout)
    firstIndex = fileLastEditedDateSTR.find(":") + 1
    lastIndex = fileLastEditedDateSTR.find("\"", firstIndex)
    return fileLastEditedDateSTR[firstIndex:lastIndex]
    

# Get the list of semesters 
semesterList = json.load(open("../_data/semesters.json"))
courses = {}
courses_index = {}

for semester in semesterList:
    print(semester)
    semester_info = semesterList[semester]
    semester_dir = "../courses/{0}".format(semester)

    # Scan through each semester folder to get the courses under that semester
    if os.path.isdir(semester_dir):
        semester_courses = []
        for course in os.listdir(semester_dir):
            print('\t', course)

            try:
                course_file = "../courses/{0}/{1}".format(semester, course)
                course_data = json.load(open(course_file))

                course_code = course.replace(".json", "")

                course_data['urls'] = {}
                course_data['urls']['edit'] = f"/courses/{semester}/{course_code}.json"
                course_data['urls']['view'] = f"/{semester}/{course_code}/"
                course_data['urls']['markdown'] = f"/pages/courses/{semester}/{course_code}"
                
                # TODO: Post-process Lecturer and Instructor details with info available at api.ce.pdn.ac.lk


                # Update the last edit date and time 
                course_data['last_edit'] = getLastEditDate(course_file)
                
                semester_courses.append(course_data)
                courses_index[course_code] = course_data

            except Exception as err:
                print("ERROR:", err)
            
        semester_courses.sort(key=lambda e:e['code']) 

        courses[semester] = { 
            "title": semester_info["title"], 
            "description": semester_info["description"], 
            "courses": semester_courses 
            }
    else:
        print("\t ERROR: {0} directory not exists".format(semester_dir))


# Write the courses.json file
filename = "../_data/courses.json"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write(json.dumps(courses, indent = 4))

# Sort the course_index
sorted_course_index = {}
for key in sorted(courses_index):
    sorted_course_index[key] = courses_index[key]

# Write the courses_index.json file
filename = "../_data/courses_index.json"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write(json.dumps(sorted_course_index, indent = 4))
