from tkinter import messagebox
from Model.MySQLDatabase import MySQLDatabase
from View.ViewClasses import *
from Utils import utils


class TeacherWindow(object):
    def __init__(self):
        try:
            self.window.destroy()
        except AttributeError:
            pass

        self.window = tk.Toplevel()
        self.db = MySQLDatabase()
        self.window.title('Teachers bar')
        self.window.option_add(*utils.options)
        self.window.resizable(False, False)

        self._define_radiobuttons()
        self._define_entries()
        self._define_buttons()
        self._define_labels()
        self._define_select_drop_menu()
        self._define_grid()

    def _define_radiobuttons(self):
        self.var = tk.IntVar()
        self.var.set(1)

        self.lab_rb = tk.Radiobutton(self.window, text='laboratory work', variable=self.var, value=1)
        self.cw_rb = tk.Radiobutton(self.window, text='control work', variable=self.var, value=2)

    def _define_entries(self):
        self.subj_id_entry = tk.Entry(self.window, width=10)
        self.mark_entry = tk.Entry(self.window, width=10)
        self.topic_entry = tk.Entry(self.window, width=10)
        self.id_entry = tk.Entry(self.window, width=10)
        self.group_entry = tk.Entry(self.window, width=10)
        self.stud_id_entry = tk.Entry(self.window, width=10)

    def _define_buttons(self):
        self.add_button = tk.Button(self.window, text='Add lab/cw',
                                    width=15, command=lambda: self._handler('Add'))
        self.del_button = tk.Button(self.window, text='Delete lab/cw',
                                    width=15, command=lambda: self._handler('Del'))
        self.set_to_group_button = tk.Button(self.window, text='Set to group',
                                             width=15, command=lambda: self._handler('Set'))
        self.del_from_group__button = tk.Button(self.window, text='Delete from group',
                                                width=15, command=lambda: self._handler('Del_gr'))
        self.add_mark_button = tk.Button(self.window, text='Add mark',
                                         width=15, command=lambda: self._handler('Add mark'))
        self.del_mark_button = tk.Button(self.window, text='Delete mark',
                                         width=15, command=lambda: self._handler('Del mark'))

    def _handler(self, label):
        commands = dict()
        if self.var.get() == 1:
            commands = {
                'Add': lambda: self.db.add_lab((self.id_entry.get(),
                                                self.subj_id_entry.get(),
                                                self.mark_entry.get(),
                                                self.topic_entry.get())),
                'Del': lambda: self.db.del_lab((self.id_entry.get(), )),
                'Set': lambda: self.db.set_lab_to_group((self.id_entry.get(),
                                                         self.group_entry.get())),
                'Del_gr': lambda: self.db.del_lab_from_group((self.id_entry.get(),
                                                              self.group_entry.get())),
                'Add mark': lambda: self.db.add_mark_to_stud_lab((self.stud_id_entry.get(),
                                                                  self.id_entry.get(),
                                                                  self.mark_entry.get())),
                'Del mark': lambda: self.db.del_mark_from_stud_lab((self.id_entry.get(),
                                                                    self.stud_id_entry.get())),
            }
        elif self.var.get() == 2:
            commands = {
                'Add': lambda: self.db.add_cw((self.id_entry.get(),
                                               self.subj_id_entry.get(),
                                               self.mark_entry.get(),
                                               self.topic_entry.get())),
                'Del': lambda: self.db.del_cw((self.id_entry.get(), )),
                'Set': lambda: self.db.set_cw_to_group((self.id_entry.get(),
                                                        self.group_entry.get())),
                'Del_gr': lambda: self.db.del_cw_from_group((self.id_entry.get(),
                                                             self.group_entry.get())),
                'Add mark': lambda: self.db.add_mark_to_stud_cw((self.stud_id_entry.get(),
                                                                 self.id_entry.get(),
                                                                 self.mark_entry.get())),
                'Del mark': lambda: self.db.del_mark_from_stud_cw((self.id_entry.get(),
                                                                   self.stud_id_entry.get())),
            }
        try:
            if self.id_entry.get() == '':
                raise Exception
            commands[label]()
        except Exception:
            messagebox.showerror(title='Error', message='Query was failed')

        self.clear_entries()

    def _define_labels(self):
        self.label_subj_id = tk.Label(self.window, text='subject id: ')
        self.label_mark = tk.Label(self.window, text='max mark: ')
        self.label_topic = tk.Label(self.window, text='topic: ')
        self.label_id = tk.Label(self.window, text='id of lab/cw: ')
        self.label_group = tk.Label(self.window, text='group id: ')
        self.label_stud_id = tk.Label(self.window, text='student id: ')

    def _define_select_drop_menu(self):
        options = [
            'Subject',
            'Laboratory work',
            'Control work',
            'Group - lab relation table',
            'Group - CW relation table',
            'Student lab results',
            'Student cw results',
            'Group table',
            'Student table'
        ]
        commands = {
            'Subject': lambda: self.db.select_subjects(),
            'Laboratory work': lambda: self.db.select_labs(),
            'Control work': lambda: self.db.select_cw(),
            'Group - lab relation table': lambda: self.db.select_group_labs(),
            'Group - CW relation table': lambda: self.db.select_group_cws(),
            'Student lab results': lambda: self.db.select_res_labs(),
            'Student cw results': lambda: self.db.select_res_cws(),
            'Group table': lambda: self.db.select_groups(),
            'Student table': lambda: self.db.select_students()
        }

        self.drop_box = DropBox(parent=self.window,
                                options=options,
                                commands=commands,
                                dropbox_str='Select list',
                                window_str='Select',
                                db=self.db,
                                row=0,
                                column=3)

    def _define_grid(self):
        self.lab_rb.grid(row=6, column=0, columnspan=2)
        self.cw_rb.grid(row=7, column=0, columnspan=2)

        self.label_subj_id.grid(row=0, column=0)
        self.label_mark.grid(row=1, column=0)
        self.label_topic.grid(row=2, column=0)
        self.label_id.grid(row=3, column=0)
        self.label_group.grid(row=4, column=0)
        self.label_stud_id.grid(row=5, column=0)

        self.subj_id_entry.grid(row=0, column=1)
        self.mark_entry.grid(row=1, column=1)
        self.topic_entry.grid(row=2, column=1)
        self.id_entry.grid(row=3, column=1)
        self.group_entry.grid(row=4, column=1)
        self.stud_id_entry.grid(row=5, column=1)

        self.add_button.grid(row=0, column=2)
        self.del_button.grid(row=1, column=2)
        self.set_to_group_button.grid(row=2, column=2)
        self.del_from_group__button.grid(row=3, column=2)
        self.add_mark_button.grid(row=4, column=2)
        self.del_mark_button.grid(row=5, column=2)

    def clear_entries(self):
        self.subj_id_entry.delete(0, 'end')
        self.mark_entry.delete(0, 'end')
        self.topic_entry.delete(0, 'end')
        self.id_entry.delete(0, 'end')
        self.group_entry.delete(0, 'end')
        self.stud_id_entry.delete(0, 'end')


class SecretaryWindow(object):
    def __init__(self):
        try:
            self.window.destroy()
        except AttributeError:
            pass

        self.window = tk.Toplevel()
        self.db = MySQLDatabase()
        self.window.title('Secretary bar')
        self.window.option_add(*utils.options)
        self.window.resizable(False, False)

        self._define_labels()
        self._define_entries()
        self._define_buttons()
        self._define_drop_box()
        self._define_grid()

    def _define_labels(self):
        self.label_stud_id = tk.Label(self.window, text='student id: ')
        self.label_rec_id = tk.Label(self.window, text='record card id: ')
        self.label_scholarsh = tk.Label(self.window, text='scholarship: ')
        self.label_name = tk.Label(self.window, text='name: ')
        self.label_surname = tk.Label(self.window, text='surname: ')
        self.label_group_id = tk.Label(self.window, text='group id: ')

    def _define_entries(self):
        self.entry_stud_id = tk.Entry(self.window, width=10)
        self.entry_rec_id = tk.Entry(self.window, width=10)
        self.entry_scholarsh = tk.Entry(self.window, width=10)
        self.entry_name = tk.Entry(self.window, width=10)
        self.entry_surname = tk.Entry(self.window, width=10)
        self.entry_group_id = tk.Entry(self.window, width=10)

    def _define_buttons(self):
        self.add_button = tk.Button(self.window, text='Add student',
                                    width=15, command=lambda: self._handler('Add'))
        self.del_button = tk.Button(self.window, text='Delete student',
                                    width=15, command=lambda: self._handler('Del'))
        self.add_to_gr_button = tk.Button(self.window, text='Add to group',
                                          width=15, command=lambda: self._handler('Add to gr'))
        self.del_from_gr_button = tk.Button(self.window, text='Delete from group',
                                            width=15, command=lambda: self._handler('Del from gr'))
        self.set_classlead_button = tk.Button(self.window, text='Set as class leader',
                                              width=15, command=lambda: self._handler('Add classlead'))
        self.del_classlead = tk.Button(self.window, text='Delete class leader',
                                       width=15, command=lambda: self._handler('Del classlead'))

    def _handler(self, label):
        commands = {
            'Add': lambda: self.db.add_stud((self.entry_rec_id.get(),
                                             self.entry_stud_id.get(),
                                             self.entry_scholarsh.get(),
                                             self.entry_name.get(),
                                             self.entry_surname.get())),
            'Del': lambda: self.db.del_stud((self.entry_stud_id.get(), )),
            'Add to gr': lambda: self.db.add_stud_to_group((self.entry_group_id.get(),
                                                            self.entry_stud_id.get())),
            'Del from gr': lambda: self.db.del_stud_from_group((self.entry_stud_id.get(), )),
            'Add classlead': lambda: self.db.add_class_leader((self.entry_group_id.get(),
                                                               self.entry_stud_id.get())),
            'Del classlead': lambda: self.db.del_class_leader((self.entry_stud_id.get(), )),
        }
        try:
            if self.entry_stud_id.get() == '':
                raise Exception
            commands[label]()
        except Exception:
            messagebox.showerror(title='Error', message='Query was failed')

        self.clear_entries()

    def _define_drop_box(self):
        options = [
            'Group table',
            'Student table',
            'Group - student relation table',
            'Group - class leader relation table',
        ]
        commands = {
            'Group table': lambda: self.db.select_table(),
            'Student table': lambda: self.db.select_students(),
            'Group - student relation table': lambda: self.db.select_group_stud(),
            'Group - class leader relation table': lambda: self.db.select_group_classlead(),
        }
        self.drop_box = DropBox(parent=self.window,
                                options=options,
                                commands=commands,
                                dropbox_str='Select list',
                                window_str='Select',
                                db=self.db,
                                row=0,
                                column=3)

    def _define_grid(self):
        self.label_stud_id.grid(row=0, column=0)
        self.label_rec_id.grid(row=1, column=0)
        self.label_scholarsh.grid(row=2, column=0)
        self.label_name.grid(row=3, column=0)
        self.label_surname.grid(row=4, column=0)
        self.label_group_id.grid(row=5, column=0)

        self.entry_stud_id.grid(row=0, column=1)
        self.entry_rec_id.grid(row=1, column=1)
        self.entry_scholarsh.grid(row=2, column=1)
        self.entry_name.grid(row=3, column=1)
        self.entry_surname.grid(row=4, column=1)
        self.entry_group_id.grid(row=5, column=1)

        self.add_button.grid(row=0, column=2)
        self.del_button.grid(row=1, column=2)
        self.add_to_gr_button.grid(row=2, column=2)
        self.del_from_gr_button.grid(row=3, column=2)
        self.set_classlead_button.grid(row=4, column=2)
        self.del_classlead.grid(row=5, column=2)

    def clear_entries(self):
        self.entry_stud_id.delete(0, 'end')
        self.entry_rec_id.delete(0, 'end')
        self.entry_scholarsh.delete(0, 'end')
        self.entry_name.delete(0, 'end')
        self.entry_surname.delete(0, 'end')
        self.entry_group_id.delete(0, 'end')


class RootWindow(object):
    def __init__(self):
        self.window = tk.Toplevel()
        self.db = MySQLDatabase()
        self.window.title('Root bar')
        self.window.option_add(*utils.options)
        self.window.resizable(False, False)

        self.secretary_button = tk.Button(self.window, text='Secretary panel', command=self.secretary)
        self.teacher_button = tk.Button(self.window, text='Teacher panel', command=self.teacher)
        self.del_university = tk.Button(self.window, text='Del university', command=self.del_university)
        self.del_faculty = tk.Button(self.window, text='Del faculty', command=self.del_faculty)
        self.del_group = tk.Button(self.window, text='Del group', command=self.del_group)
        self.del_subject = tk.Button(self.window, text='Del subject', command=self.del_subject)

        self.add_university = tk.Button(self.window, text='Add university', command=self.add_university)
        self.add_faculty = tk.Button(self.window, text='Add faculty', command=self.add_faculty)
        self.add_group = tk.Button(self.window, text='Add group', command=self.add_group)
        self.add_subject = tk.Button(self.window, text='Add subject', command=self.add_subject)

        self.add_university.grid(row=1, column=0)
        self.add_faculty.grid(row=1, column=1)
        self.add_group.grid(row=1, column=2)
        self.add_subject.grid(row=1, column=3)

        self.del_university.grid(row=2, column=0)
        self.del_faculty.grid(row=2, column=1)
        self.del_group.grid(row=2, column=2)
        self.del_subject.grid(row=2, column=3)

        self.secretary_button.grid(row=3, column=0, columnspan=2)
        self.teacher_button.grid(row=3, column=2, columnspan=2)

        self._define_drop_box()

    def secretary(self):
        try:
            self.secretary_window.window.destroy()
        except AttributeError:
            pass
        finally:
            self.secretary_window = SecretaryWindow()

    def teacher(self):
        try:
            self.teacher_window.window.destroy()
        except AttributeError:
            pass
        finally:
            self.teacher_window = TeacherWindow()

    def del_university(self):
        try:
            delete_id = utils.inputbox('Delete university', 'university id', 'Enter')
            self.db.del_university((delete_id,))
        except Exception:
            messagebox.showerror(title='Error', message='Query was failed')

    def del_faculty(self):
        try:
            delete_id = utils.inputbox('Delete faculty', 'faculty id', 'Enter')
            self.db.del_faculty((delete_id,))
        except Exception:
            messagebox.showerror(title='Error', message='Query was failed')

    def del_group(self):
        try:
            delete_id = utils.inputbox('Delete group', 'group id', 'Enter')
            self.db.del_group((delete_id,))
        except Exception:
            messagebox.showerror(title='Error', message='Query was failed')

    def del_subject(self):
        try:
            delete_id = utils.inputbox('Delete subject', 'subject id', 'Enter')
            self.db.del_subject((delete_id,))
        except Exception:
            messagebox.showerror(title='Error', message='Query was failed')

    def add_university(self):
        try:
            data = utils.inputbox_4fields('Add university', messages=['id: ', 'address: ', 'web: ', 'name: '])
            if data[0] == '':
                raise Exception
            self.db.add_univ(data)
        except Exception:
            messagebox.showerror(title='Error', message='Query was failed')

    def add_faculty(self):
        try:
            data = utils.inputbox_4fields('Add faculty', messages=['id: ', 'web: ', 'name: ', 'university id: '])
            if data[0] == '':
                raise Exception
            self.db.add_fac(data)
        except Exception:
            messagebox.showerror(title='Error', message='Query was failed')

    def add_group(self):
        try:
            data = utils.inputbox_4fields('Add group', messages=['id: ', 'name: ', 'course: ', 'faculty id: '])
            if data[0] == '':
                raise Exception
            self.db.add_group(data)
        except Exception:
            messagebox.showerror(title='Error', message='Query was failed')

    def add_subject(self):
        try:
            data = utils.inputbox_2fields('Add subject', messages=['id: ', 'name: '])
            if data[0] == '':
                raise Exception
            self.db.add_subject(data)
        except Exception:
            messagebox.showerror(title='Error', message='Query was failed')

    def _define_drop_box(self):
        options = [
            'University table',
            'Faculty table',
            'Group table',
            'Subject',
        ]
        commands = {
            'University table': lambda: self.db.select_university(),
            'Faculty table': lambda: self.db.select_faculty(),
            'Group table': lambda: self.db.select_groups(),
            'Subject': lambda: self.db.select_subjects(),
        }
        self.drop_box = DropBox(parent=self.window,
                                options=options,
                                commands=commands,
                                dropbox_str='Select list',
                                window_str='Select',
                                db=self.db,
                                row=0,
                                column=0,
                                columnspan=4)
