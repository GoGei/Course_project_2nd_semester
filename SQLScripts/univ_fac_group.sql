drop database if exists course_database_bilous;
create database course_database_bilous;
use course_database_bilous;

drop table if exists university;
create table university
(
	university_id int not null,
    address varchar(100) not null,
    web_site varchar(200) not null,
    university_name varchar(150) not null,
    primary key(university_id)
);

drop table if exists faculty;
create table faculty
(
	faculty_id int not null,
	web_site varchar(200) not null,
	faculty_name varchar(150) not null,
    university_id int not null,
    primary key(faculty_id),
    foreign key (university_id) references university(university_id)
		on delete cascade on update cascade
);

drop table if exists group_table;
create table group_table
(
	group_id int not null,
    group_name varchar(30) not null,
    course int not null,
    faculty_id int not null,
    primary key(group_id),
    foreign key (faculty_id) references faculty(faculty_id) 
		on delete cascade on update cascade
);

drop table if exists student;
create table student
(
	record_card_id int not null unique,
    student_id int not null unique,
    scholarship float,
    student_name varchar(50),
    student_surname varchar(50),
    primary key (record_card_id, student_id)
);

drop table if exists group_students;
create table group_students
(
    group_id int not null,
    student_id int not null unique,
    primary key (group_id, student_id),
    foreign key (group_id) references group_table(group_id)
		on delete cascade on update cascade,
	foreign key (student_id) references student(student_id)
		on delete cascade on update cascade
);

drop table if exists group_classleader;
create table group_classleader
(
    group_id int not null unique,
    student_id int not null unique,
    primary key (group_id, student_id),
    foreign key (group_id) references group_table(group_id)
		on delete cascade on update cascade,
	foreign key (student_id) references student(student_id)
		on delete cascade on update cascade
);

drop table if exists subject_table;
create table subject_table
(
	subject_id int not null,
    name varchar(30) not null,
    primary key (subject_id)
);

drop table if exists lab;
create table lab
(
	lab_id int not null,
    subject_id int not null,
    max_mark int not null,
    topic varchar(50) not null,
    primary key(lab_id, subject_id),
    foreign key (subject_id) references subject_table(subject_id)
		on delete cascade on update cascade
);

drop table if exists control_work;
create table control_work
(
	control_work_id int not null,
    subject_id int not null,
    max_mark int not null,
    topic varchar(50) not null,
    primary key(control_work_id, subject_id),
    foreign key (subject_id) references subject_table(subject_id)
		on delete cascade on update cascade
);

drop table if exists group_labs;
create table group_labs
(
    lab_id int not null,
    group_id int not null,
    deadline date,
    primary key (lab_id, group_id),
    foreign key (lab_id) references lab(lab_id)
		on delete cascade on update cascade,
	foreign key (group_id) references group_table(group_id)
		on delete cascade on update cascade
);

drop table if exists group_controls;
create table group_controls
(
    control_work_id int not null,
    group_id int not null,
    deadline date,
    primary key (control_work_id, group_id),
    foreign key (control_work_id) references control_work(control_work_id)
		on delete cascade on update cascade,
	foreign key (group_id) references group_table(group_id)
		on delete cascade on update cascade
);

drop table if exists result_labs;
create table result_labs
(
    student_id int not null,
    lab_id int not null,
    mark int not null,
    primary key (student_id, lab_id),
    foreign key (student_id) references student(student_id)
		on delete cascade on update cascade,
	foreign key (lab_id) references lab(lab_id)
		on delete cascade on update cascade
);

drop table if exists result_controls;
create table result_controls
(
    student_id int not null,
    control_work_id int not null,
    mark int not null,
    primary key (student_id, control_work_id),
	foreign key (student_id) references student(student_id)
		on delete cascade on update cascade,
	foreign key (control_work_id) references control_work(control_work_id)
		on delete cascade on update cascade
);