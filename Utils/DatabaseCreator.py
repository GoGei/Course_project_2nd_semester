import mysql.connector
import pymysql


class CreateScripts(object):
    def __init__(self, host='localhost', user='root', passwd=''):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = 'course_database_bilous'
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd
        )
        self.cursor = self.db.cursor()

    def create(self):
        self.cursor.execute('DROP DATABASE IF EXISTS {}'.format(self.database))
        self.cursor.execute('CREATE DATABASE {}'.format(self.database))
        self.db = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.database
        )
        self.cursor = self.db.cursor()
        self._create_tables()
        self._create_views()
        self._fill()
        self._create_users()

    def _create_tables(self):
        creator = CreateTableQueries()
        self.cursor.execute(creator.university)
        self.db.commit()
        self.cursor.execute(creator.faculty)
        self.db.commit()
        self.cursor.execute(creator.group_table)
        self.db.commit()
        self.cursor.execute(creator.student)
        self.db.commit()
        self.cursor.execute(creator.group_students)
        self.db.commit()
        self.cursor.execute(creator.group_classleader)
        self.db.commit()
        self.cursor.execute(creator.subject_table)
        self.db.commit()
        self.cursor.execute(creator.lab)
        self.db.commit()
        self.cursor.execute(creator.control_work)
        self.db.commit()
        self.cursor.execute(creator.group_labs)
        self.db.commit()
        self.cursor.execute(creator.group_controls)
        self.db.commit()
        self.cursor.execute(creator.result_labs)
        self.db.commit()
        self.cursor.execute(creator.result_controls)
        self.db.commit()

    def _create_views(self):
        creator = CreateViewQueries()
        self.cursor.execute(creator.group_data)
        self.db.commit()
        self.cursor.execute(creator.with_scholarship)
        self.db.commit()
        self.cursor.execute(creator.students_data)
        self.db.commit()
        self.cursor.execute(creator.classleader_data)
        self.db.commit()
        self.cursor.execute(creator.subject_contence)
        self.db.commit()
        self.cursor.execute(creator.control_labs)
        self.db.commit()
        self.cursor.execute(creator.student_scores)
        self.db.commit()

    def _fill(self):
        creator = FillDBQueries()
        self.cursor.execute(creator.univ_sql, creator.univ_val)
        self.db.commit()
        self.cursor.executemany(creator.fac_sql, creator.fac_val)
        self.db.commit()
        self.cursor.executemany(creator.group_sql, creator.group_val)
        self.db.commit()
        self.cursor.executemany(creator.stud_sql, creator.stud_val)
        self.db.commit()
        self.cursor.executemany(creator.group_stud_sql, creator.group_stud_val)
        self.db.commit()
        self.cursor.executemany(creator.group_class_sql, creator.group_class_val)
        self.db.commit()
        self.cursor.executemany(creator.subj_sql, creator.subj_val)
        self.db.commit()
        self.cursor.executemany(creator.lab_sql, creator.lab_val)
        self.db.commit()
        self.cursor.executemany(creator.cw_sql, creator.cw_val)
        self.db.commit()
        self.cursor.executemany(creator.group_lab_sql, creator.group_lab_val)
        self.db.commit()
        self.cursor.executemany(creator.group_cw_sql, creator.group_cw_val)
        self.db.commit()
        self.cursor.executemany(creator.res_lab_sql, creator.res_lab_val)
        self.db.commit()
        self.cursor.executemany(creator.res_cw_sql, creator.res_cw_val)
        self.db.commit()

    def _create_users(self):
        self.db = pymysql.connect(self.host, self.user, self.passwd, self.database)
        self.cursor = self.db.cursor()

        sql = "drop user if exists 'guest_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "drop user if exists 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "drop user if exists 'secretary_for_db_cp'@'localhost';"
        self.cursor.execute(sql)

        sql = "create user 'guest_for_db_cp'@'localhost' identified by '';"
        self.cursor.execute(sql)
        sql = "create user 'teacher_for_db_cp'@'localhost' identified by 'teacher';"
        self.cursor.execute(sql)
        sql = "create user 'secretary_for_db_cp'@'localhost' identified by 'secretary';"
        self.cursor.execute(sql)
        sql = "grant insert, delete, select on lab to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant insert, delete, select on control_work to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant insert, delete, select on group_labs to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant insert, delete, select on group_controls to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant insert, delete, select on result_labs to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant insert, delete, select on result_controls to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on subject_table to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on student to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on group_table to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant insert, delete, select on student to 'secretary_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant insert, delete, select on group_students to 'secretary_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant insert, delete, select on group_classleader to 'secretary_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on group_table to 'secretary_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on classleader_data to 'guest_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on control_labs to 'guest_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on group_data to 'guest_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on student_scores to 'guest_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on students_data to 'guest_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on subject_contence to 'guest_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on with_scholarship to 'guest_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on classleader_data to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on control_labs to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on group_data to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on student_scores to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on students_data to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on subject_contence to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on with_scholarship to 'teacher_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on classleader_data to 'secretary_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on control_labs to 'secretary_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on group_data to 'secretary_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on student_scores to 'secretary_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on students_data to 'secretary_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on subject_contence to 'secretary_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        sql = "grant select on with_scholarship to 'secretary_for_db_cp'@'localhost';"
        self.cursor.execute(sql)
        self.db.commit()


class CreateTableQueries(object):
    def __init__(self):
        self.university = "create table university\
                            (\
                                university_id int not null,\
                                address varchar(100) not null,\
                                web_site varchar(200) not null,\
                                university_name varchar(150) not null,\
                                primary key(university_id)\
                            )"
        self.faculty = 'create table faculty\
                        ( \
                            faculty_id int not null,\
                            web_site varchar(200) not null,\
                            faculty_name varchar(150) not null,\
                            university_id int not null,\
                            primary key(faculty_id),\
                            foreign key (university_id) references university(university_id)\
                                on delete cascade on update cascade\
                        )'
        self.group_table = 'create table group_table\
                            (\
                                group_id int not null,\
                                group_name varchar(30) not null,\
                                course int not null,\
                                faculty_id int not null,\
                                primary key(group_id),\
                                foreign key (faculty_id) references faculty(faculty_id) \
                                    on delete cascade on update cascade\
                            )'
        self.student = 'create table student\
                        (\
                            record_card_id int not null unique,\
                            student_id int not null unique,\
                            scholarship float,\
                            student_name varchar(50),\
                            student_surname varchar(50),\
                            primary key (record_card_id, student_id)\
                        )'
        self.group_students = 'create table group_students\
                                (\
                                    group_id int not null,\
                                    student_id int not null unique,\
                                    primary key (group_id, student_id),\
                                    foreign key (group_id) references group_table(group_id)\
                                        on delete cascade on update cascade,\
                                    foreign key (student_id) references student(student_id)\
                                        on delete cascade on update cascade\
                                )'
        self.group_classleader = 'create table group_classleader\
                                    (\
                                        group_id int not null unique,\
                                        student_id int not null unique,\
                                        primary key (group_id, student_id),\
                                        foreign key (group_id) references group_table(group_id)\
                                            on delete cascade on update cascade,\
                                        foreign key (student_id) references student(student_id)\
                                            on delete cascade on update cascade\
                                    )'
        self.subject_table = 'create table subject_table\
                                (\
                                    subject_id int not null,\
                                    name varchar(30) not null,\
                                    primary key (subject_id)\
                                )'
        self.lab = 'create table lab\
                    (\
                        lab_id int not null,\
                        subject_id int not null,\
                        max_mark int not null,\
                        topic varchar(50) not null,\
                        primary key(lab_id, subject_id),\
                        foreign key (subject_id) references subject_table(subject_id)\
                            on delete cascade on update cascade\
                    )'
        self.control_work = 'create table control_work\
                            (\
                                control_work_id int not null,\
                                subject_id int not null,\
                                max_mark int not null,\
                                topic varchar(50) not null,\
                                primary key(control_work_id, subject_id),\
                                foreign key (subject_id) references subject_table(subject_id)\
                                    on delete cascade on update cascade\
                            )'
        self.group_labs = 'create table group_labs\
                            (\
                                lab_id int not null,\
                                group_id int not null,\
                                deadline date,\
                                primary key (lab_id, group_id),\
                                foreign key (lab_id) references lab(lab_id)\
                                    on delete cascade on update cascade,\
                                foreign key (group_id) references group_table(group_id)\
                                    on delete cascade on update cascade\
                            )'
        self.group_controls = 'create table group_controls\
                                (\
                                    control_work_id int not null,\
                                    group_id int not null,\
                                    deadline date,\
                                    primary key (control_work_id, group_id),\
                                    foreign key (control_work_id) references control_work(control_work_id)\
                                        on delete cascade on update cascade,\
                                    foreign key (group_id) references group_table(group_id)\
                                    on delete cascade on update cascade\
                                )'
        self.result_labs = 'create table result_labs\
                            (\
                                student_id int not null,\
                                lab_id int not null,\
                                mark int not null,\
                                primary key (student_id, lab_id),\
                                foreign key (student_id) references student(student_id)\
                                    on delete cascade on update cascade,\
                                foreign key (lab_id) references lab(lab_id)\
                                    on delete cascade on update cascade\
                            )'
        self.result_controls = 'create table result_controls\
                                (\
                                    student_id int not null,\
                                    control_work_id int not null,\
                                    mark int not null,\
                                    primary key (student_id, control_work_id),\
                                    foreign key (student_id) references student(student_id)\
                                        on delete cascade on update cascade,\
                                    foreign key (control_work_id) references control_work(control_work_id)\
                                        on delete cascade on update cascade\
                                )'


class CreateViewQueries(object):
    def __init__(self):
        self.group_data = 'create view group_data as \
select group_table.group_id, group_table.group_name, \
group_table.course, faculty.faculty_name, university.university_name \
from group_table, faculty, university \
where group_table.faculty_id = faculty.faculty_id and \
faculty.university_id = university.university_id'

        self.with_scholarship = "create view with_scholarship as \
select record_card_id, concat(student_name, ' ' ,student_surname) as fullname, scholarship \
from student \
where scholarship is not null and scholarship > 0"

        self.students_data = "create view students_data as \
select concat(student.student_name, ' ', student.student_surname) as fullname, student.record_card_id, \
group_table.group_id, group_table.group_name, group_table.course, faculty.faculty_name, university.university_name \
from student, group_students, group_table, faculty, university \
where student.student_id = group_students.student_id and group_table.group_id = group_students.group_id \
and group_table.faculty_id = faculty.faculty_id and faculty.university_id = university.university_id"

        self.classleader_data = "create view classleader_data as \
select concat(student.student_name, ' ', student.student_surname) as fullname, student.record_card_id, \
group_table.group_id, group_table.group_name, group_table.course, faculty.faculty_name, university.university_name \
from student, group_table, faculty, university, group_classleader \
where student.student_id = group_classleader.student_id and group_table.group_id = group_classleader.group_id \
and group_table.faculty_id = faculty.faculty_id and faculty.university_id = university.university_id"

        self.subject_contence = "create view subject_contence as \
select subject_table.name as 'name', lab.max_mark as 'Mark', lab.topic as 'Topic' \
from subject_table, lab \
where subject_table.subject_id = lab.subject_id \
UNION \
select subject_table.name as 'name', control_work.max_mark as 'Mark', control_work.topic as 'Topic' \
from subject_table, control_work \
where subject_table.subject_id = control_work.subject_id"

        self.control_labs = "create view control_labs as \
select subject_table.name as 'name', group_labs.group_id, group_labs.deadline, lab.max_mark, lab.topic \
from subject_table, group_labs, lab \
where group_labs.lab_id = lab.lab_id and lab.subject_id = subject_table.subject_id \
UNION \
select subject_table.name as 'name', group_controls.group_id, \
group_controls.deadline, control_work.max_mark, control_work.topic \
from subject_table, group_controls, control_work \
where group_controls.control_work_id = control_work.control_work_id and \
control_work.subject_id = subject_table.subject_id"

        self.student_scores = "create view student_scores as \
select student.student_id, student.record_card_id, concat(student_name, ' ' ,student_surname) as 'fullname', \
result_labs.mark as 'Mark', lab.max_mark as 'Max', lab.topic as 'Topic', \
subject_table.subject_id as 'ID', subject_table.name as 'Name' \
from student, result_labs, lab, subject_table \
where result_labs.student_id = student.student_id and result_labs.lab_id = lab.lab_id and \
lab.subject_id = subject_table.subject_id \
UNION \
select student.student_id, student.record_card_id, concat(student_name, ' ' ,student_surname) as 'fullname', \
result_controls.mark as 'Mark', control_work.max_mark as 'Max', control_work.topic as 'Topic', \
subject_table.subject_id as 'ID', subject_table.name as 'Name' \
from student, result_controls, control_work, subject_table \
where result_controls.student_id = student.student_id and result_controls.control_work_id = control_work.control_work_id \
and control_work.subject_id = subject_table.subject_id"


class FillDBQueries(object):
    def __init__(self):
        self.univ_sql = "insert into university (university_id, address, web_site, university_name) \
         values (%s, %s, %s, %s)"
        self.fac_sql = "insert into faculty (faculty_id, web_site, faculty_name, university_id) \
         values (%s, %s, %s, %s)"
        self.group_sql = "insert into group_table (group_id, group_name, course, faculty_id) \
         values (%s, %s, %s, %s)"
        self.stud_sql = "insert into student (record_card_id, student_id, scholarship, student_name, student_surname) \
         values (%s, %s, %s, %s, %s)"
        self.group_stud_sql = "insert into group_students (group_id, student_id) \
         values (%s, %s)"
        self.group_class_sql = "insert into group_classleader (group_id, student_id) \
         values (%s, %s)"
        self.subj_sql = "insert into subject_table values (%s, %s)"
        self.lab_sql = "insert into lab (lab_id, subject_id, max_mark, topic) values (%s, %s, %s, %s)"
        self.cw_sql = "insert into control_work (control_work_id, subject_id, max_mark, topic) values (%s, %s, %s, %s)"
        self.group_lab_sql = "insert into group_labs (lab_id, group_id) values (%s, %s)"
        self.group_cw_sql = "insert into group_controls (control_work_id, group_id) values (%s, %s)"
        self.res_lab_sql = "insert into result_labs (student_id, lab_id, mark) values (%s, %s, %s)"
        self.res_cw_sql = "insert into result_controls (student_id, control_work_id, mark) values (%s, %s, %s)"

        self.univ_val = (1, 'address of KhPI', 'main web of KhPI', 'KhPI')
        self.fac_val = [
            (1001, 'KN web site', 'KN', 1),
            (1002, 'KIT web site', 'KIT', 1)
        ]
        self.group_val = [
            (101, '218a', 2, 1001),
            (102, '218b', 2, 1001),
            (103, '37-b', 1, 1002),
            (104, '38-a', 1, 1002)
        ]
        self.stud_val = [
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
            (18011, 11, 0, 'Name', 'Surname')
        ]
        self.group_stud_val = [
            (101, 1), (101, 2), (101, 3),
            (102, 4), (102, 5),
            (103, 6), (103, 7), (103, 8),
            (104, 9), (104, 10), (104, 11)
        ]
        self.group_class_val = [
            (101, 1), (102, 5), (103, 6), (104, 10)
        ]
        self.subj_val = [
            (1, 'OOP'), (2, 'Algo')
        ]
        self.lab_val = [
            (1001, 1, 30, 'OOP1'), (1002, 1, 30, 'OOP2'), (1003, 1, 30, 'OOP3'),
            (2001, 1, 30, 'Algo1'), (2002, 1, 30, 'Algo2'), (2003, 1, 30, 'Algo3')
        ]
        self.cw_val = [
            (1001, 1, 30, 'OOP1 cr'), (1002, 1, 30, 'OOP2 cr'), (1003, 1, 30, 'OOP3 cr'),
            (2001, 2, 30, 'Algo1 cr'), (2002, 2, 30, 'Algo2 cr'), (2003, 2, 30, 'Algo3 cr')
        ]
        self.group_lab_val = [
            (1001, 101), (1001, 102), (1001, 103), (1001, 104),
            (1002, 101), (1002, 102),
            (1003, 103), (1003, 104),

            (2001, 101), (2001, 102), (2001, 103), (2001, 104),
            (2002, 101), (2002, 102),
            (2003, 103), (2003, 104)
        ]
        self.group_cw_val = [
            (1001, 101), (1001, 102), (1001, 103), (1001, 104),
            (1002, 101), (1002, 102),
            (1003, 103), (1003, 104),

            (2001, 101), (2001, 102), (2001, 103), (2001, 104),
            (2002, 101), (2002, 102),
            (2003, 103), (2003, 104)
        ]
        self.res_lab_val = [
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
            (11, 1001, 20), (11, 1003, 20), (11, 2001, 20), (11, 2003, 20)
        ]
        self.res_cw_val = [
            (1, 1001, 20), (1, 1002, 20), (1, 2001, 20), (1, 2002, 20),
            (2, 1001, 20), (2, 2002, 20),
            (3, 1001, 20), (3, 1002, 20),
            (4, 1001, 20), (4, 1002, 20), (4, 2001, 20), (4, 2002, 20),
            (5, 1001, 20), (5, 2001, 20), (5, 2002, 20),
            (6, 1001, 20), (6, 1003, 20), (6, 2001, 20), (6, 2003, 20),
            (7, 1001, 20), (7, 1003, 20), (7, 2003, 20),
            (8, 1001, 20), (8, 1003, 20), (8, 2001, 20), (8, 2003, 20),
            (9, 2001, 20), (9, 2003, 20),
            (10, 1001, 20), (10, 1003, 20), (10, 2001, 20), (10, 2003, 20),
            (11, 1001, 20), (11, 2003, 20)
        ]