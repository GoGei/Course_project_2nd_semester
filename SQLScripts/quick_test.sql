use course_database_bilous;
SET SQL_SAFE_UPDATES = 0;

delete from university;
delete from student;
delete from subject_table;

insert into university (university_id, address, web_site, university_name) values (1, 'address of KhPI', 'main web of KhPI', 'KhPI');
insert into faculty (faculty_id, web_site, faculty_name, university_id) values
(1001, 'KN web site', 'KN', 1),
(1002, 'KIT web site', 'KIT', 1);

insert into group_table (group_id, group_name, course, faculty_id) values
(101, '218a', 2, 1001),
(102, '218b', 2, 1001),
(103, '37-b', 1, 1002),
(104, '38-a', 1, 1002);

insert into student (record_card_id, student_id, scholarship, student_name, student_surname) values
(18001, 1, 0, 'Name', 'Surname'),
(18002, 2, 1000.8, 'Name', 'Surname'),
(18003, 3, 0, 'Name', 'Surname'),
(18004, 4, 1000.8, 'Name', 'Surname'),
(18005, 5, 1250.3, 'Name', 'Surname'),
(18006, 6, 0, 'Name', 'Surname'),
(18007, 7, 0.0, 'Name', 'Surname'),
(18008, 8, 0, 'Name', 'Surname'),
(18009, 9, 1000.8, 'Name', 'Surname'),
(18010, 10, 0, 'Name', 'Surname'),
(18011, 11, 0, 'Name', 'Surname');

insert into group_students (group_id, student_id) values
(101, 1), (101, 2), (101, 3),
(102, 4), (102, 5),
(103, 6), (103, 7), (103, 8), 
(104, 9), (104, 10), (104, 11);

insert into group_classleader (group_id, student_id)
values (101, 1), (102, 5), (103, 6), (104, 10);

select * from group_data;
select * from students_data;
select * from classleader_data;

insert into subject_table values (1, 'OOP'), (2, 'Algo');

insert into lab (lab_id, subject_id, max_mark, topic) values
(1001, 1, 30, 'OOP1'), (1002, 1, 30, 'OOP2'), (1003, 1, 30, 'OOP3'),
(2001, 1, 30, 'Algo1'), (2002, 1, 30, 'Algo2'), (2003, 1, 30, 'Algo3');

insert into control_work (control_work_id, subject_id, max_mark, topic) values
(1001, 1, 30, 'OOP1 cr'), (1002, 1, 30, 'OOP2 cr'), (1003, 1, 30, 'OOP3 cr'),
(2001, 2, 30, 'Algo1 cr'), (2002, 2, 30, 'Algo2 cr'), (2003, 2, 30, 'Algo3 cr');

insert into group_labs (lab_id, group_id) values
(1001, 101), (1001, 102), (1001, 103), (1001, 104),
(1002, 101), (1002, 102),
(1003, 103), (1003, 104),

(2001, 101), (2001, 102), (2001, 103), (2001, 104),
(2002, 101), (2002, 102),
(2003, 103), (2003, 104);

insert into group_controls (control_work_id, group_id) values
(1001, 101), (1001, 102), (1001, 103), (1001, 104),
(1002, 101), (1002, 102),
(1003, 103), (1003, 104),

(2001, 101), (2001, 102), (2001, 103), (2001, 104),
(2002, 101), (2002, 102),
(2003, 103), (2003, 104);

select * from group_labs;
select * from group_controls;
select * from subject_contence;
select * from control_labs;

#all labs have passed
delete from result_labs;
insert into result_labs (student_id, lab_id, mark) values
(1, 1001, 20), (1, 1002, 20), (1, 2001, 20), (1, 2002, 20),
(2, 1001, 20), (2, 1002, 20), (2, 2001, 20), (2, 2002, 20),
(3, 1001, 20), (3, 1002, 20), (3, 2001, 20), (3, 2002, 20),
(4, 1001, 20), (4, 1002, 20), (4, 2001, 20), (4, 2002, 20),
(5, 1001, 20), (5, 1002, 20), (5, 2001, 20), (5, 2002, 20),
(6, 1001, 20), (6, 1003, 20), (6, 2001, 20), (6, 2003, 20),
(7, 1001, 20), (7, 1003, 20), (7, 2001, 20), (7, 2003, 20),
(8, 1001, 20), (8, 1003, 20), (8, 2001, 20), (8, 2003, 20),
(9, 1001, 20), (9, 1003, 20), (9, 2001, 20), (9, 2003, 20),
(10, 1001, 20), (10, 1003, 20), (10, 2001, 20), (10, 2003, 20),
(11, 1001, 20), (11, 1003, 20), (11, 2001, 20), (11, 2003, 20);

#not all cr have passed
delete from result_controls;
insert into result_controls (student_id, control_work_id, mark) values
(1, 1001, 20), (1, 1002, 20), (1, 2001, 20), (1, 2002, 20),
(2, 1001, 20), 							     (2, 2002, 20),
(3, 1001, 20), (3, 1002, 20),
(4, 1001, 20), (4, 1002, 20), (4, 2001, 20), (4, 2002, 20),
(5, 1001, 20), 				  (5, 2001, 20), (5, 2002, 20),
(6, 1001, 20), (6, 1003, 20), (6, 2001, 20), (6, 2003, 20),
(7, 1001, 20), (7, 1003, 20),                (7, 2003, 20),
(8, 1001, 20), (8, 1003, 20), (8, 2001, 20), (8, 2003, 20),
							  (9, 2001, 20), (9, 2003, 20),
(10, 1001, 20), (10, 1003, 20), (10, 2001, 20), (10, 2003, 20),
(11, 1001, 20), 								(11, 2003, 20);

select * from student_scores;