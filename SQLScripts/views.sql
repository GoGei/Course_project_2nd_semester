use course_database_bilous;

drop view if exists group_data;
create view group_data as
select group_table.group_id, group_table.group_name, group_table.course, faculty.faculty_name, university.university_name
from group_table, faculty, university
where group_table.faculty_id = faculty.faculty_id and faculty.university_id = university.university_id;

drop view if exists with_scholarship;
create view with_scholarship as
select record_card_id, concat(student_name, ' ' ,student_surname) as fullname, scholarship
from student where scholarship is not null and scholarship > 0;

drop view if exists students_data;
create view students_data as
select concat(student.student_name, ' ', student.student_surname) as fullname, student.record_card_id, 
	group_table.group_id, group_table.group_name, group_table.course, faculty.faculty_name, university.university_name
from student, group_students, group_table, faculty, university
where student.student_id = group_students.student_id and group_table.group_id = group_students.group_id 
	and group_table.faculty_id = faculty.faculty_id and faculty.university_id = university.university_id;

drop view if exists classleader_data;
create view classleader_data as
select concat(student.student_name, ' ', student.student_surname) as fullname, student.record_card_id, 
	group_table.group_id, group_table.group_name, group_table.course, faculty.faculty_name, university.university_name
from student, group_table, faculty, university, group_classleader
where student.student_id = group_classleader.student_id and group_table.group_id = group_classleader.group_id 
	and group_table.faculty_id = faculty.faculty_id and faculty.university_id = university.university_id;

drop view if exists subject_contence;
create view subject_contence as
select subject_table.name as 'name', lab.max_mark as 'Mark', lab.topic as 'Topic'
	from subject_table, lab
	where subject_table.subject_id = lab.subject_id
UNION
select subject_table.name as 'name', control_work.max_mark as 'Mark', control_work.topic as 'Topic'
	from subject_table, control_work
	where subject_table.subject_id = control_work.subject_id;

drop view if exists control_labs;
create view control_labs as
select subject_table.name as 'name', group_labs.group_id, group_labs.deadline, lab.max_mark, lab.topic
	from subject_table, group_labs, lab
	where group_labs.lab_id = lab.lab_id and lab.subject_id = subject_table.subject_id
UNION
select subject_table.name as 'name', group_controls.group_id, group_controls.deadline, control_work.max_mark, control_work.topic
	from subject_table, group_controls, control_work
	where group_controls.control_work_id = control_work.control_work_id and control_work.subject_id = subject_table.subject_id;

drop view if exists student_scores;
create view student_scores as
select student.student_id, student.record_card_id, concat(student_name, ' ' ,student_surname) as 'fullname',
	 result_labs.mark as 'Mark', lab.max_mark as 'Max', lab.topic as 'Topic', subject_table.subject_id as 'ID', subject_table.name as 'Name'
from student, result_labs, lab, subject_table
where result_labs.student_id = student.student_id and result_labs.lab_id = lab.lab_id and lab.subject_id = subject_table.subject_id
UNION
select student.student_id, student.record_card_id, concat(student_name, ' ' ,student_surname) as 'fullname',
	 result_controls.mark as 'Mark', control_work.max_mark as 'Max', control_work.topic as 'Topic', 
     subject_table.subject_id as 'ID', subject_table.name as 'Name'
from student, result_controls, control_work, subject_table
where result_controls.student_id = student.student_id and result_controls.control_work_id = control_work.control_work_id 
	and control_work.subject_id = subject_table.subject_id;

select * from group_data;
select * from with_scholarship;
select * from students_data;
select * from classleader_data;
select * from subject_contence;
select * from control_labs;
select * from student_scores;