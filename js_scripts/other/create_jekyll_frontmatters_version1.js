/*
 1. Reads the data from _data/courses/semester1.json
 2. Creates a jekyll frontmatter for each course in the json file
 3. Saves the frontmatter in pages/courses/semester1/<course_code>.
*/

let semester3 = require('data/courses/semester1.json');

semester3.forEach(course => {
  let course_code = course.code;

  let course_name = course.name;
  let course_credits = course.credits;
  let core_or_elective = course.type;
  let prerequisties = course.prerequisites;

  // let content = thisCourse["content"]
  // let objectives = thisCourse["objectives"]

  let ilos_knowledge = course.ILOs.Knowledge;
  let ilos_skill = course.ILOs.Skill;
  let ilos_attitude = course.ILOs.Attitude;
  
  let textbooks_references = course.textbooks_references;

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

  let filePath = './pages/courses/semester1new/' + course_code + '.html';
  console.log(filePath);
  fs.writeFile(filePath, course_frontmatter, 'utf8', function(err) {
    if (err) {
      return console.log(err);
    }
  });
});