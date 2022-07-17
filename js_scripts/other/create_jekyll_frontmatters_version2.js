/*
 1. Reads the data from _data/courses/semester1.json
 2. Creates a jekyll frontmatter for each course in the json file
 3. Saves the frontmatter in pages/courses/semester1/<course_code>.
*/

let semester3 = require('data/courses/semester1.json');

// let fs = require('fs');
semester3.forEach(thisCourse => {
    let course_code = thisCourse["code"]

    let course_name = thisCourse["name"]
    let course_credits = thisCourse["credits"]
    let core_or_elective = thisCourse["type"]
    let prerequisties = thisCourse["prerequisites"]

    // let content = thisCourse["content"]
    // let objectives = thisCourse["objectives"]

    let ilos_knowledge = thisCourse["ILOs"]["Knowledge"]
    let ilos_skill = thisCourse["ILOs"]["Skill"]
    let ilos_attitude = thisCourse["ILOs"]["Attitude"]

    let textbooks_references = thisCourse["references"]

    let course_frontmatter = `---
    layout: courses
    permalink: /courses/semester1new/${course_code}
    title: ${course_name}

    course_number : ${course_code} 
    course_title : ${course_name} 
    credits : ${course_credits} 
    core_or_elective : ${core_or_elective} 
    prerequisites : ${prerequisties} 
    ilos_knowledge : ${ilos_knowledge} 
    ilos_skill : ${ilos_skill} 
    ilos_attitude : ${ilos_attitude} 
    textbooks_references : ${textbooks_references} 
    ---`;

    // fs.writeFileSync('pages/courses/semester1new/${course_code}.html', course_frontmatter);

    console.log(course_frontmatter);
});