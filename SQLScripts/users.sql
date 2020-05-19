use course_database_bilous;

drop user if exists 'guest_for_db_cp'@'localhost';
drop user if exists 'teacher_for_db_cp'@'localhost';
drop user if exists 'secretary_for_db_cp'@'localhost';

create user 'guest_for_db_cp'@'localhost' identified by '';
create user 'teacher_for_db_cp'@'localhost' identified by 'teacher';
create user 'secretary_for_db_cp'@'localhost' identified by 'secretary';

grant insert, delete, select on lab to 'teacher_for_db_cp'@'localhost';
grant insert, delete, select on control_work to 'teacher_for_db_cp'@'localhost';
grant insert, delete, select on group_labs to 'teacher_for_db_cp'@'localhost';
grant insert, delete, select on group_controls to 'teacher_for_db_cp'@'localhost';
grant insert, delete, select on result_labs to 'teacher_for_db_cp'@'localhost';
grant insert, delete, select on result_controls to 'teacher_for_db_cp'@'localhost';
grant select on subject_table to 'teacher_for_db_cp'@'localhost';
grant select on student to 'teacher_for_db_cp'@'localhost';
grant select on group_table to 'teacher_for_db_cp'@'localhost';

grant insert, delete, select on student to 'secretary_for_db_cp'@'localhost';
grant insert, delete, select on group_students to 'secretary_for_db_cp'@'localhost';
grant insert, delete, select on group_classleader to 'secretary_for_db_cp'@'localhost';
grant select on group_table to 'secretary_for_db_cp'@'localhost';

grant select on classleader_data to 'guest_for_db_cp'@'localhost';
grant select on control_labs to 'guest_for_db_cp'@'localhost';
grant select on group_data to 'guest_for_db_cp'@'localhost';
grant select on student_scores to 'guest_for_db_cp'@'localhost';
grant select on students_data to 'guest_for_db_cp'@'localhost';
grant select on subject_contence to 'guest_for_db_cp'@'localhost';
grant select on with_scholarship to 'guest_for_db_cp'@'localhost';

grant select on classleader_data to 'teacher_for_db_cp'@'localhost';
grant select on control_labs to 'teacher_for_db_cp'@'localhost';
grant select on group_data to 'teacher_for_db_cp'@'localhost';
grant select on student_scores to 'teacher_for_db_cp'@'localhost';
grant select on students_data to 'teacher_for_db_cp'@'localhost';
grant select on subject_contence to 'teacher_for_db_cp'@'localhost';
grant select on with_scholarship to 'teacher_for_db_cp'@'localhost';

grant select on classleader_data to 'secretary_for_db_cp'@'localhost';
grant select on control_labs to 'secretary_for_db_cp'@'localhost';
grant select on group_data to 'secretary_for_db_cp'@'localhost';
grant select on student_scores to 'secretary_for_db_cp'@'localhost';
grant select on students_data to 'secretary_for_db_cp'@'localhost';
grant select on subject_contence to 'secretary_for_db_cp'@'localhost';
grant select on with_scholarship to 'secretary_for_db_cp'@'localhost';