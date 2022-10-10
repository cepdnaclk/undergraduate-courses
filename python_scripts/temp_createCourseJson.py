import json 
import os

semesters = json.load(open("../_data/semesters.json"))

statisticsTemplate = {
    "year": "NULL",
    "batch": "NULL",
    "lecturers": [ "lecturer@eng.pdn.ac.lk" ],
    "instructors": [ "instructor@eng.pdn.ac.lk" ],
    "grades": {
        "A+": 0, "A": 0, "A-": 0, "B+": 0, "B": 0, "B-": 0, "C+": 0, "C": 0, "C-": 0, "D+": 0, "D": 0, "D-": 0, "E": 0
    }
}
ILOsTemplate = {
    "Knowledge": "NULL",
    "Skill": "NULL",
    "Attitude": "NULL"
}

for semester in semesters:
    print(semester + "\n")
    semesterData = json.load(open("../_data/temp_courses/{0}.json".format(semester)))
    courses = semesterData['courses']
    
    for raw_course in courses:
        print('\t', raw_course['code'])

        courseCode = raw_course['code'].upper()
        url = "/{0}/{1}/".format(semester, courseCode)

        objectives = raw_course['objectives'] if 'objectives' in raw_course and raw_course['objectives']!="NULL" else []
        references = raw_course['references'] if 'references' in raw_course and raw_course['references']!="NULL" else []
        ILOs = raw_course['ILOs'] if 'ILOs' in raw_course else ILOsTemplate
        allocation = raw_course['allocation'] if 'allocation' in raw_course else "NULL"
        prerequisites = raw_course['prerequisites'] if 'prerequisites' in raw_course else []
        statistics = raw_course['statistics'] if 'statistics' in raw_course else [statisticsTemplate]
        marks = raw_course['marks'] if 'marks' in raw_course and raw_course['marks']!="NULL" else []

        modules = raw_course['modules']
        modulesList = list()

        if modules!='NULL':
            modulesList = list()
            for module in modules:
                ml = {
                    "topic": module["topic"],
                    "description": module["description"],
                    "allocation": {
                        "L": module["allocation"]["L"],
                        "T": module["allocation"]["T"],
                        "P": module["allocation"]["P"],
                        "A": module["allocation"]["A"],
                    }
                }
                modulesList.append(ml)

        course = {
            "code": courseCode,
            "name": raw_course['name'],
            "credits": raw_course['credits'],
            "type": raw_course['type'].upper(),
            "prerequisites": prerequisites,
            "content": raw_course['content'],
            "objectives": objectives,
            "ILOs": ILOs,
            "allocation": allocation,
            "modules": modulesList,
            "references": references,
            "marks": marks,
            "statistics": statistics, 
            "urls": {
                "edit": "/courses/{0}/{1}.json".format(semester, courseCode),
                "view": "/{0}/{1}/".format(semester, courseCode),
                "markdown": "/pages/courses/{0}/{1}".format(semester, courseCode)
            }
        }

        filename = "../courses/{0}/{1}.json".format(semester, courseCode)
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(json.dumps(course, indent = 4))




print("End of the script----------")