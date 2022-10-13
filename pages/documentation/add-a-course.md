---
layout: documentation
permalink: /documentation/how-to-add-a-new-course/

question: How to add a new Course page ?
index: 101

title: How to add a new Course page ?
---

&nbsp;

##### Step 1:

You can visit this [link](https://github.com/cepdnaclk/undergraduate-courses/tree/main/courses), navigate into the correct _semester_ or _category_ and create a new file named `COURSECODE.json`

##### Step 2:

Next, you need to copy the following template and edit it, by replacing the `{}` with the right details. Please refer [CO324 Course](https://github.com/cepdnaclk/undergraduate-courses/tree/main/courses/semester5/CO321.json) to get an idea about it.

A detailed guide on how to filling the parameters available [here]({{ '/documentation/how-to-edit-a-course/' | relative_url }}).

```json
{
  "code": "{Course Code}",
  "name": "{Course Title}",
  "credits": 3,
  "type": "{ CORE | ELECTIVE | GENERAL }",
  "prerequisites": ["{Coure Code 1}", "{Course Code 2}"],
  "content": "{Description about the course}",
  "objectives": "{Objectives of the coures}",
  "ILOs": {
    "Knowledge": [
      "This is the first knowledge",
      "This is the second knowledge"
    ],
    "Skill": ["This is the first skill", "This is the second skill"],
    "Attitude": ["This is the first attitude"]
  },
  "allocation": "Lectures : 30h, Tutorial-Classes : 4h, Practical-Classes : 14h, Assignments : 10h",
  "modules": [
    {
      "topic": "{The topic of the module}",
      "description": "{A short description}",
      "allocation": {
        "L": "10",
        "T": "-",
        "P": "2",
        "A": "-"
      }
    }
  ],
  "references": ["{Reference 1}", "{Reference 2}"],
  "marks": [
    {
      "description": "Practicals",
      "allocation": ""
    },
    {
      "description": "Assignments",
      "allocation": ""
    },
    {
      "description": "Mid-Exam",
      "allocation": ""
    },
    {
      "description": "End-Exam",
      "allocation": ""
    }
  ],
  "statistics": [
    {
      "year": "{ The year that course was offered}",
      "batch": "{The batch(s) that studied the course}",
      "lecturers": ["roshanr@eng.pdn.ac.lk", "isurunawinne@eng.pdn.ac.lk"],
      "instructors": ["instructor@eng.pdn.ac.lk"],
      "grades": {
        "A+": 0,
        "A": 0,
        "A-": 0,
        "B+": 0,
        "B": 0,
        "B-": 0,
        "C+": 0,
        "C": 0,
        "C-": 0,
        "D+": 0,
        "D": 0,
        "E": 0
      }
    }
  ]
}
```

<div class="alert alert-warning d-flex align-items-top mb-2 mt-5" role="alert">
   <div>
       <h6>
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-exclamation-triangle-fill flex-shrink-0 me-2" viewBox="0 0 16 16" role="img" aria-label="Warning:"> <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/> </svg>
            Warning !
       </h6>
       <p>
            Once the JSON is edited, make sure the syntax is correct. you can use <a href="https://jsonformatter.curiousconcept.com/#" target="_blank">this</a> online tool for it. Please avoid <i>trailing commas</i> in the JSON file too.
       </p>
   </div>
</div>

&nbsp;

##### Step 3:

Finally, you can save by clicking on the **Commit changes** button below the text editor.

If you followed up all the procedures correctly, the course will be added to the site within a day.
