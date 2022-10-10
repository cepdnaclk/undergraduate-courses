import json 
import os


# Get the list of semesters 
semesterList = json.load(open("../_data/semesters.json"))

courses = {}

for semester in semesterList:
    print(semester)
    semester_info = semesterList[semester]
    semester_dir = "../courses/{0}".format(semester)

    # Scan through each semester folder to get the courses under that semester
    if os.path.isdir(semester_dir):
        semester_courses = []
        for course in os.listdir(semester_dir):
            print('\t', course)

            course_file = "../courses/{0}/{1}".format(semester, course)
            course_data = json.load(open(course_file))
            semester_courses.append(course_data)

            # TODO: Post-process Lecturer and Instructor details with info available at api.ce.pdn.ac.lk

        semester_courses.sort(key=lambda e:e['code']) 

        courses[semester] = { 
            "title": semester_info["title"], 
            "description": semester_info["description"], 
            "courses": semester_courses 
            }
    else:
        print("\t ERROR: {0} directory not exists".format(semester_dir))


# Generate the courses file 
filename = "../_data/courses.json"
os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as f:
    f.write(json.dumps(courses, indent = 4))