use course_database_bilous;
SET SQL_SAFE_UPDATES = 0;

delete from university;
insert into university (university_id, address, web_site, university_name)
values
(1, 'Address of NTU KhPI', 'web-site NTU KhPI', 'NTU KhPI'),
(2, 'Address of KNURE', 'web-site KNURE', 'KNURE');

delete from faculty;
insert into faculty (faculty_id, web_site, faculty_name, university_id)
values
(1, 'web-site of KhPI/KN', 'KN', 1),
(2, 'web-site of KhPI/KIT', 'KIT', 1),
(3, 'web-site of KhPI/BEM', 'BEM', 1),
(4, 'web-site of KNURE/KN', 'KN', 2),
(5, 'web-site of KNURE/KIT', 'KIT', 2);

delete from group_table;
insert into group_table (group_id, group_name, course, faculty_id)
values
(1001, '218a', 2, 1), (1002, '218b', 2, 1), (1003, '218e', 2, 1),
(1004, '311', 1, 2), (1005, '312', 1, 2), (1006, '313', 1, 2),
(1007, '110', 3, 3), (1008, '111', 3, 3),

(2001, '37-a', 2, 4), (2002, '37-b', 2, 4), (2003, '37-c', 2, 4),
(2004, 'kt-1', 2, 5), (2005, 'kt-2', 2, 5), (2006, 'kt-3', 2, 5);

select * from group_data;

delete from student;
insert into student (student_id, record_card_id, student_name, student_surname, scholarship)
values
(1, 18001, 'Name', 'Surname', 1000.5), (2, 18002, 'Name', 'Surname', null), (3, 18003, 'Name', 'Surname', null), (4, 18004, 'Name', 'Surname', 1000.5), (5, 18005, 'Name', 'Surname', null), 
(6, 18006, 'Name', 'Surname', null), (7, 18007, 'Name', 'Surname', 1000.5), (8, 18008, 'Name', 'Surname', null), (9, 18009, 'Name', 'Surname', null), (10, 18010, 'Name', 'Surname', null), 
(11, 18011, 'Name', 'Surname', null), (12, 18012, 'Name', 'Surname', null), (13, 18013, 'Name', 'Surname', 1000.5), (14, 18014, 'Name', 'Surname', null), (15, 18015, 'Name', 'Surname', null), 
(16, 18016, 'Name', 'Surname', null), (17, 18017, 'Name', 'Surname', null), (18, 18018, 'Name', 'Surname', null), (19, 18019, 'Name', 'Surname', null), (20, 18020, 'Name', 'Surname', 1250.5), 
(21, 18021, 'Name', 'Surname', 1250.5), (22, 18022, 'Name', 'Surname', 1250.5), (23, 18023, 'Name', 'Surname', 1000.5), (24, 18024, 'Name', 'Surname', null), (25, 18025, 'Name', 'Surname', null), 
(26, 18026, 'Name', 'Surname', null), (27, 18027, 'Name', 'Surname', null), (28, 18028, 'Name', 'Surname', null), (29, 18029, 'Name', 'Surname', 1000.5), (30, 18030, 'Name', 'Surname', 1000.5), 
(31, 18031, 'Name', 'Surname', null), (32, 18032, 'Name', 'Surname', null), (33, 18033, 'Name', 'Surname', null), (34, 18034, 'Name', 'Surname', null), (35, 18035, 'Name', 'Surname', null), 
(36, 18036, 'Name', 'Surname', 1000.5), (37, 18037, 'Name', 'Surname', null), (38, 18038, 'Name', 'Surname', 1000.5), (39, 18039, 'Name', 'Surname', null), (40, 18040, 'Name', 'Surname', null), 
(41, 18041, 'Name', 'Surname', null), (42, 18042, 'Name', 'Surname', null), (43, 18043, 'Name', 'Surname', null), (44, 18044, 'Name', 'Surname', 1000.5), (45, 18045, 'Name', 'Surname', null), 
(46, 18046, 'Name', 'Surname', null), (47, 18047, 'Name', 'Surname', 1250.5), (48, 18048, 'Name', 'Surname', null), (49, 18049, 'Name', 'Surname', null), (50, 18050, 'Name', 'Surname', null), 
(51, 18051, 'Name', 'Surname', 1000.5), (52, 18052, 'Name', 'Surname', null), (53, 18053, 'Name', 'Surname', 1000.5), (54, 18054, 'Name', 'Surname', null), (55, 18055, 'Name', 'Surname', null), 
(56, 18056, 'Name', 'Surname', null), (57, 18057, 'Name', 'Surname', null), (58, 18058, 'Name', 'Surname', null), (59, 18059, 'Name', 'Surname', null), (60, 18060, 'Name', 'Surname', 1000.5), 
(61, 18061, 'Name', 'Surname', null), (62, 18062, 'Name', 'Surname', 1000.5), (63, 18063, 'Name', 'Surname', null), (64, 18064, 'Name', 'Surname', null), (65, 18065, 'Name', 'Surname', null), 
(66, 18066, 'Name', 'Surname', null), (67, 18067, 'Name', 'Surname', null), (68, 18068, 'Name', 'Surname', null), (69, 18069, 'Name', 'Surname', null), (70, 18070, 'Name', 'Surname', 1000.5);

#for each group 5 students
delete from group_students;
insert into group_students (group_id, student_id)
values
(1001, 1), (1001, 2), (1001, 3), (1001, 4), (1001, 5), 
(1002, 6), (1002, 7), (1002, 8), (1002, 9), (1002, 10), 
(1003, 11), (1003, 12), (1003, 13), (1003, 14), (1003, 15), 
(1004, 16), (1004, 17), (1004, 18), (1004, 19), (1004, 20), 
(1005, 21), (1005, 22), (1005, 23), (1005, 24), (1005, 25), 
(1006, 26), (1006, 27), (1006, 28), (1006, 29), (1006, 30), 
(1007, 31), (1007, 32), (1007, 33), (1007, 34), (1007, 35), 
(1008, 36), (1008, 37), (1008, 38), (1008, 39), (1008, 40), 
(2001, 41), (2001, 42), (2001, 43), (2001, 44), (2001, 45), 
(2002, 46), (2002, 47), (2002, 48), (2002, 49), (2002, 50), 
(2003, 51), (2003, 52), (2003, 53), (2003, 54), (2003, 55), 
(2004, 56), (2004, 57), (2004, 58), (2004, 59), (2004, 60), 
(2005, 61), (2005, 62), (2005, 63), (2005, 64), (2005, 65), 
(2006, 66), (2006, 67), (2006, 68), (2006, 69), (2006, 70);

delete from group_classleader;
insert into group_classleader (group_id, student_id)
values
(1001, 1), (1002, 6), (1003, 11),
(1004, 16), (1005, 21), (1006, 26),
(1007, 31), (1008, 36),

(2001, 41), (2002, 46), (2003, 51),
(2004, 56), (2005, 61), (2006, 66);

select * from with_scholarship;
select * from students_data;
select * from classleader_data;

#100 - for KhPI, 200 - KNURE
delete from subject_table;
insert into subject_table (subject_id, name)
values
(101, 'OOP'), (102, 'Algorythm'), (103, 'Math'), 
(201, 'OOP'), (202, 'Operations Research');

#prepared labs for groups. Specified names aimed on only this faculty groups
delete from lab;
insert into lab (lab_id, subject_id, max_mark, topic)
values
(1101, 101, 20, 'KhPI OOP1'), (1102, 101, 20, 'KhPI OOP2'), (1103, 101, 20, 'KhPI OOP3'), (1104, 101, 20, 'KhPI OOP4'), 
(1105, 101, 20, 'KhPI OOP5 KN'), (1106, 101, 10, 'KhPI OOP6 KIT'), (1107, 101, 10, 'KhPI OOP7 KIT'),
(1201, 102, 10, 'KhPI Algo1'), (1202, 102, 20, 'KhPI Algo2'), (1203, 102, 30, 'KhPI Algo3'),

(2201, 201, 10, 'KNURE OOP1'), (2202, 201, 20, 'KNURE OOP2'), (2203, 201, 30, 'KNURE OOP3'),
(2101, 202, 20, 'KNURE Oper. Research'), (2102, 202, 20, 'KNURE Oper. Research'), (2103, 202, 20, 'KNURE Oper. Research'), (2104, 202, 20, 'KNURE Oper. Research'), 
(2105, 202, 20, 'KNURE Oper. Research'), (2106, 202, 10, 'KNURE Oper. Research'), (2107, 202, 10, 'KNURE Oper. Research');

#prepared cr for groups. Specified names aimed on only this faculty groups
delete from control_work;
insert into control_work (control_work_id, subject_id, max_mark, topic)
values
(1201, 102, 10, 'KhPI Algo cr1 KN'), (1202, 102, 15, 'KhPI Algo cr2 KN'), (1203, 102, 15, 'KhPI Algo cr3 KN'),
(1204, 102, 20, 'KhPI Algo cr1 KIT'), (1205, 102, 20, 'KhPI Algo cr2 KIT'),
(1301, 103, 30, 'KhPI cr math1'), (1302, 103, 30, 'KhPI cr math2'), (1303, 103, 30, 'KhPI cr math3'), (1304, 103, 10, 'KhPI cr math4'),

(2101, 201, 20, 'KNURE OOP1'), (2102, 201, 20, 'KNURE OOP2');

select * from subject_contence;

#KhPI
#5 oop labs with 1100 id. 1-4common, 5 - KN, 6,7 - KIT
#3 common algo labs for KN and KIT with 1200 id
#KNURE
#3 common oop labs for KN and KIT with id 2200
#5 algo labs for  
insert into group_labs (lab_id, group_id) values
#KhPI
(1101, 1001), (1102, 1001), (1103, 1001), (1104, 1001), (1105, 1001),
(1101, 1002), (1102, 1002), (1103, 1002), (1104, 1002), (1105, 1002), 
(1101, 1003), (1102, 1003), (1103, 1003), (1104, 1003), (1105, 1003),

(1101, 1004), (1102, 1004), (1103, 1004), (1104, 1004), (1106, 1004), (1107, 1004),
(1101, 1005), (1102, 1005), (1103, 1005), (1104, 1005), (1106, 1005), (1107, 1005),
(1101, 1006), (1102, 1006), (1103, 1006), (1104, 1006), (1106, 1006), (1107, 1006),

(1201, 1001), (1201, 1002), (1201, 1003), (1201, 1004), (1201, 1005), (1201, 1006),
(1202, 1001), (1202, 1002), (1202, 1003), (1202, 1004), (1202, 1005), (1202, 1006),
(1203, 1001), (1203, 1002), (1203, 1003), (1203, 1004), (1203, 1005), (1203, 1006),
#KNURE
(2201, 2001), (2201, 2002), (2201, 2003), (2201, 2004), (2201, 2005), (2201, 2006),
(2202, 2001), (2202, 2002), (2202, 2003), (2202, 2004), (2202, 2005), (2202, 2006),
(2203, 2001), (2203, 2002), (2203, 2003), (2203, 2004), (2203, 2005), (2203, 2006),

(2101, 2001), (2102, 2001), (2103, 2001), (2104, 2001), (2105, 2001),
(2101, 2002), (2102, 2002), (2103, 2002), (2104, 2002), (2105, 2002),
(2101, 2003), (2102, 2003), (2103, 2003), (2104, 2003), (2105, 2003),

(2101, 2004), (2102, 2004), (2103, 2004), (2106, 2004), (2107, 2004),
(2101, 2005), (2102, 2005), (2103, 2005), (2106, 2005), (2107, 2005),
(2101, 2006), (2102, 2006), (2103, 2006), (2106, 2006), (2107, 2006);

#KhPI
#Algo cr :1201-1203 for KN, 1204-1205 for KIT
#Math cr for all with id 1300
#KNURE
#oop cr for all with id 2100
insert into group_controls (control_work_id, group_id) values
#KhPI
(1201, 1001), (1201, 1002), (1201, 1003),
(1202, 1001), (1202, 1002), (1202, 1003),
(1203, 1001), (1203, 1002), (1203, 1003),

(1204, 1004), (1204, 1005), (1204, 1006),
(1205, 1004), (1205, 1005), (1205, 1006),

(1301, 1001), (1302, 1001), (1303, 1001), (1304, 1001),
(1301, 1002), (1302, 1002), (1303, 1002), (1304, 1002),
(1301, 1003), (1302, 1003), (1303, 1003), (1304, 1003),
(1301, 1004), (1302, 1004), (1303, 1004), (1304, 1004),
(1301, 1005), (1302, 1005), (1303, 1005), (1304, 1005),
(1301, 1006), (1302, 1006), (1303, 1006), (1304, 1006),
(1301, 1007), (1302, 1007), (1303, 1007), (1304, 1007),
(1301, 1008), (1302, 1008), (1303, 1008), (1304, 1008),
#KNURE
(2101, 2001), (2101, 2002), (2101, 2003), (2101, 2004), (2101, 2005), (2101, 2006),
(2102, 2001), (2102, 2002), (2102, 2003), (2102, 2004), (2102, 2005), (2102, 2006);

select * from control_labs;