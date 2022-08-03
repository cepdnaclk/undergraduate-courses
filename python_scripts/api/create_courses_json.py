import json
import os
import shutil

import requests  # pip install requests

# Where the API is available
apiIndex = 'https://localhost:8080/peraprojects/courses/1.0.0/'

# Where JSON files are available
jsonData = f"../data"

# Where the data is available
apiSource = 'https://cepdnaclk.github.io/Undergraduate-Courses/api/courses/'

# Validate and format the course codes
# def validate_course_code(course_code):

# Delete the old JSON file

# def delete_old_json():
# try:
#     os.remove(jsonData)
# except OSError:
#     pass
def delete_old_json():
    try:
        shutil.rmtree(jsonData)
    except error as e:
        print(e)
        pass

# Create the new JSON file
# def create_json_files():
#     try:
#         os.makedirs(jsonData)
#     except OSError:
#         pass
def create_json_files(courses_data):
    try:
        filename = "../data/index.json"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            # f.write(json.dumps({}))
            f.write(json.dumps(courses_data, indent=4))
    except error as e:
        print(e)
        pass

# ------------------------------------------------------------------------------

# # Delete the existing files first
# delete_old_json()

r = requests.get(apiSource)

# Fetch the data from 'apiSource'
if r.status_code == 200:
    dataInJSON = json.loads(r.text)
    print(dataInJSON)

    # for thisSemester in dataInJSON:
        # print(thisSemester) 
        # print("-------")
        # for thisCourse in thisSemester:
        #     print(thisCourse)
        #     print("########")

            # course_code = thisCourse["code"]
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