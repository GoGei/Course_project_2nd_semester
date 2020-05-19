from Model.AdditionalWindows import *
from Utils.DatabaseCreator import CreateScripts
from Utils.utils import inputbox_2fields


class MainWindow(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        try:
            self.db = MySQLDatabase()
        except Exception:
            user, passwd = inputbox_2fields('Create DB', ['Root name: ', 'Passwd: '])
            runner = CreateScripts(user=user, passwd=passwd)
            runner.create()
            self.db = MySQLDatabase()

        self.login_button = tk.Button(self.parent, text='Login', width=15, command=self.login_window).pack()
        self.logout_button = tk.Button(self.parent, text='Logout', width=15, command=self.logout).pack()
        self.views_button = tk.Button(self.parent, text='Views', width=15, command=self.views_window).pack()
        self.use_permissions_button = tk.Button(self.parent, text='Interact with DB', width=15, command=self.permissions).pack()
        self.exit_button = tk.Button(self.parent, text='Exit', width=15, command=exit).pack()

    def login_window(self):
        try:
            self.login_window.destroy()
        except AttributeError:
            pass

        self.login_window = tk.Toplevel()
        self.login_window.title('Login database: {}'.format(self.db.database))
        self.login_window.option_add(*utils.options)
        self.login_window.resizable(False, False)

        label_user = tk.Label(self.login_window, text='User: ')
        label_passwd = tk.Label(self.login_window, text='Password: ')

        user_entry = tk.Entry(self.login_window)
        passwd_entry = tk.Entry(self.login_window)

        user, passwd = 'user', 'passw'

        def get_data():
            nonlocal user, passwd
            user = user_entry.get()
            passwd = passwd_entry.get()
            try:
                self.db.login_on_other_user(user, passwd)
            except Exception as error:
                messagebox.showerror(title='Error', message=repr(error))
            self.login_window.destroy()

        enter = tk.Button(self.login_window, text='login', command=lambda: get_data())

        label_user.grid(row=0, column=0, padx=10, pady=10)
        label_passwd.grid(row=1, column=0, padx=10, pady=10)
        user_entry.grid(row=0, column=1)
        passwd_entry.grid(row=1, column=1)
        enter.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def logout(self):
        self.db.login_with_default()

    def views_window(self):
        VIEW_OPTIONS = [
            'Group view',
            'Students with scholarship',
            'Students data',
            'Class leaders',
            'Subject content',
            'CW and labs view',
            'Scores'
        ]
        try:
            self.view_window.destroy()
        except AttributeError:
            pass

        self.view_window = tk.Toplevel()
        self.view_window.title('Views of database: {}'.format(self.db.database))
        self.view_window.option_add(*utils.options)

        commands = {
            'Group view': lambda: self.db.group_data_view(),
            'Students with scholarship': lambda: self.db.with_scholarship_view(),
            'Students data': lambda: self.db.student_data_view(),
            'Class leaders': lambda: self.db.class_leader_view(),
            'Subject content': lambda: self.db.subject_content_view(),
            'CW and labs view': lambda: self.db.cw_labs_view(),
            'Scores': lambda: self.db.scores_view(),
        }

        def execute(label):
            result = commands[label]()
            table.set_new(utils.heads_for_table_by_label[label], result)

        view_string = tk.StringVar()
        view_string.set('Views drop box')
        views_dropbox = tk.OptionMenu(self.view_window, view_string, *VIEW_OPTIONS,
                                      command=execute)
        views_dropbox.pack()
        table = TableClass(self.view_window, headings=('column1', 'column2', 'column3', 'column4', 'column5'))

    def permissions(self):
        try:
            self.permission_window.window.destroy()
        except AttributeError:
            pass

        if self.db.user == 'teacher_for_db_cp':
            self.permission_window = TeacherWindow()
        elif self.db.user == 'secretary_for_db_cp':
            self.permission_window = SecretaryWindow()
        elif self.db.user == 'root':
            self.permission_window = RootWindow()
        else:
            print('0 permission')