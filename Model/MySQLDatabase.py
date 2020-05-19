import mysql.connector
from Utils.utils import Singleton


class MySQLDatabase(metaclass=Singleton):
    def __init__(self):
        self.host = 'localhost'
        self.user = 'guest_for_db_cp'
        self.password = ''
        self.database = 'course_database_bilous'
        self._login()
        print(self.user, self.password)
        print('login')

    def login_on_other_user(self, user, passwd):
        self.user = user
        self.password = passwd
        self._login()
        print(self.user, self.password)
        print('Relogin')

    def _login(self):
        try:
            self.db = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                database=self.database
            )
            self.cursor = self.db.cursor()
        except mysql.connector.errors.ProgrammingError:
            print('If DB is not created, it will be created')
            print('Access denied: user={}, passwd={}'.format(self.user, self.password))
            raise Exception('Access denied: user={}, passwd={}')

    def login_with_default(self):
        self.user = 'guest_for_db_cp'
        self.password = ''
        self._login()
        print(self.user, self.password)
        print('default login')

    def add_univ(self, vals=tuple()):
        sql = "insert into university (university_id, address, web_site, university_name)\
         values (%s, %s, %s, %s)"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def add_fac(self, vals=tuple()):
        sql = "insert into faculty (faculty_id, web_site, faculty_name, university_id)\
         values (%s, %s, %s, %s)"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def add_group(self, vals=tuple()):
        sql = "insert into group_table (group_id, group_name, course, faculty_id)\
         values (%s, %s, %s, %s)"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def add_subject(self, vals=tuple()):
        sql = "insert into subject_table values (%s, %s)"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def del_university(self, obj_id):
        sql = "delete from university where university_id = %s"
        self.cursor.execute(sql, obj_id)
        self.db.commit()

    def del_faculty(self, obj_id):
        sql = "delete from faculty where faculty_id = %s"
        self.cursor.execute(sql, obj_id)
        self.db.commit()

    def del_group(self, obj_id):
        sql = "delete from group_table where group_id = %s"
        self.cursor.execute(sql, obj_id)
        self.db.commit()

    def del_subject(self, obj_id):
        sql = "delete from subject_table where subject_id = %s"
        self.cursor.execute(sql, obj_id)
        self.db.commit()

    def add_stud(self, vals=tuple()):
        sql = "insert into student (record_card_id, student_id, scholarship, student_name, student_surname)\
         values (%s, %s, %s, %s, %s)"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def del_stud(self, obj_id):
        sql = "delete from student where student_id = %s"
        self.cursor.execute(sql, obj_id)
        self.db.commit()

    def add_stud_to_group(self, vals=tuple()):
        sql = "insert into group_students (group_id, student_id) values (%s, %s)"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def del_stud_from_group(self, obj_id):
        sql = "delete from group_students where student_id = %s"
        self.cursor.execute(sql, obj_id)
        self.db.commit()

    def add_class_leader(self, vals=tuple()):
        sql = "insert into group_classleader (group_id, student_id) values (%s, %s)"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def del_class_leader(self, obj_id):
        sql = "delete from group_classleader where student_id = %s"
        self.cursor.execute(sql, obj_id)
        self.db.commit()

    def add_lab(self, vals=tuple()):
        sql = "insert into lab (lab_id, subject_id, max_mark, topic) values (%s, %s, %s, %s)"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def add_cw(self, vals=tuple()):
        sql = "insert into control_work (control_work_id, subject_id, max_mark, topic) values (%s, %s, %s, %s)"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def del_lab(self, obj_id):
        sql = "delete from lab where lab_id = %s"
        self.cursor.execute(sql, obj_id)
        self.db.commit()

    def del_cw(self, obj_id):
        sql = "delete from control_work where control_work_id = %s"
        self.cursor.execute(sql, obj_id)
        self.db.commit()

    def set_lab_to_group(self, vals=tuple()):
        sql = "insert into group_labs (lab_id, group_id) values (%s, %s)"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def set_cw_to_group(self, vals=tuple()):
        sql = "insert into group_controls (control_work_id, group_id) values (%s, %s)"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def del_lab_from_group(self, vals=tuple()):
        sql = "delete from group_labs where lab_id = %s and group_id = %s"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def del_cw_from_group(self, vals=tuple()):
        sql = "delete from group_controls where control_work_id = %s and group_id = %s"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def add_mark_to_stud_lab(self, vals=tuple()):
        sql = "insert into result_labs (student_id, lab_id, mark) values (%s, %s, %s)"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def add_mark_to_stud_cw(self, vals=tuple()):
        sql = "insert into result_controls (student_id, control_work_id, mark) values (%s, %s, %s)"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def del_mark_from_stud_lab(self, vals=tuple()):
        sql = "delete from result_labs where lab_id = %s and student_id = %s"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def del_mark_from_stud_cw(self, vals=tuple()):
        sql = "delete from result_controls where control_work_id = %s and student_id = %s"
        self.cursor.execute(sql, vals)
        self.db.commit()

    def select_university(self):
        self.cursor.execute("SELECT * FROM university")
        result = self.cursor.fetchall()
        return result

    def select_faculty(self):
        self.cursor.execute("SELECT * FROM faculty")
        result = self.cursor.fetchall()
        return result

    def select_table(self):
        self.cursor.execute("SELECT * FROM group_table")
        result = self.cursor.fetchall()
        return result

    def select_students(self):
        self.cursor.execute("SELECT * FROM student")
        result = self.cursor.fetchall()
        return result

    def select_groups(self):
        self.cursor.execute("SELECT * FROM group_table")
        result = self.cursor.fetchall()
        return result

    def select_group_stud(self):
        self.cursor.execute("SELECT * FROM group_students")
        result = self.cursor.fetchall()
        return result

    def select_group_classlead(self):
        self.cursor.execute("SELECT * FROM group_classleader")
        result = self.cursor.fetchall()
        return result

    def select_subjects(self):
        self.cursor.execute("SELECT * FROM subject_table")
        result = self.cursor.fetchall()
        return result

    def select_labs(self):
        self.cursor.execute("SELECT * FROM lab")
        result = self.cursor.fetchall()
        return result

    def select_cw(self):
        self.cursor.execute("SELECT * FROM control_work")
        result = self.cursor.fetchall()
        return result

    def select_group_labs(self):
        self.cursor.execute("SELECT * FROM group_labs")
        result = self.cursor.fetchall()
        return result

    def select_group_cws(self):
        self.cursor.execute("SELECT * FROM group_controls")
        result = self.cursor.fetchall()
        return result

    def select_res_labs(self):
        self.cursor.execute("SELECT * FROM result_labs")
        result = self.cursor.fetchall()
        return result

    def select_res_cws(self):
        self.cursor.execute("SELECT * FROM result_controls")
        result = self.cursor.fetchall()
        return result

    def group_data_view(self):
        self.cursor.execute("SELECT * FROM group_data")
        result = self.cursor.fetchall()
        return result

    def with_scholarship_view(self):
        self.cursor.execute("SELECT * FROM with_scholarship")
        result = self.cursor.fetchall()
        return result

    def student_data_view(self):
        self.cursor.execute("SELECT * FROM students_data")
        result = self.cursor.fetchall()
        return result

    def class_leader_view(self):
        self.cursor.execute("SELECT * FROM classleader_data")
        result = self.cursor.fetchall()
        return result

    def subject_content_view(self):
        self.cursor.execute("SELECT * FROM subject_contence")
        result = self.cursor.fetchall()
        return result

    def cw_labs_view(self):
        self.cursor.execute("SELECT * FROM control_labs")
        result = self.cursor.fetchall()
        return result

    def scores_view(self):
        self.cursor.execute("SELECT * FROM student_scores")
        result = self.cursor.fetchall()
        return result
