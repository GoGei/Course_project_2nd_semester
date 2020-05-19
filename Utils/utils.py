import tkinter as tk


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def inputbox(title, message, button_text):
    root = tk.Tk()
    root.title(title)
    root.option_add('*font', ('verdana', 12, 'bold'))
    root.resizable(False, False)
    label = tk.Label(root, text=message)
    label.pack()
    text = ''

    def on_return():
        nonlocal text
        text = textbox.get()
        root.quit()
        root.destroy()

    textbox = tk.Entry(root, width=40)
    textbox.bind('<Return>', on_return)
    textbox.pack()
    textbox.focus_set()
    button = tk.Button(root, text=button_text, command=on_return)
    button.pack()
    root.mainloop()
    return text


def inputbox_4fields(title, messages=list(), button_text='Enter'):
    root = tk.Tk()
    root.title(title)
    root.option_add('*font', ('verdana', 12, 'bold'))
    root.resizable(False, False)
    text = tuple()
    def on_return():
        nonlocal text
        text = (textbox1.get(), textbox2.get(), textbox3.get(), textbox4.get())
        root.quit()
        root.destroy()

    label1 = tk.Label(root, text=messages[0])
    label2 = tk.Label(root, text=messages[1])
    label3 = tk.Label(root, text=messages[2])
    label4 = tk.Label(root, text=messages[3])

    textbox1 = tk.Entry(root, width=18)
    textbox2 = tk.Entry(root, width=18)
    textbox3 = tk.Entry(root, width=18)
    textbox4 = tk.Entry(root, width=18)

    button = tk.Button(root, text=button_text, command=on_return)
    textbox1.bind('<Return>', on_return)
    textbox1.focus_set()
    textbox2.bind('<Return>', on_return)
    textbox2.focus_set()
    textbox3.bind('<Return>', on_return)
    textbox3.focus_set()
    textbox4.bind('<Return>', on_return)
    textbox4.focus_set()

    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)
    label3.grid(row=2, column=0)
    label4.grid(row=3, column=0)
    textbox1.grid(row=0, column=1)
    textbox2.grid(row=1, column=1)
    textbox3.grid(row=2, column=1)
    textbox4.grid(row=3, column=1)
    button.grid(row=4, column=0, columnspan=2)

    root.mainloop()
    return text


def inputbox_2fields(title, messages=list(), button_text='Enter'):
    root = tk.Tk()
    root.title(title)
    root.option_add('*font', ('verdana', 12, 'bold'))
    root.resizable(False, False)
    text = tuple()

    def on_return():
        nonlocal text
        text = (textbox1.get(), textbox2.get())
        root.quit()
        root.destroy()

    label1 = tk.Label(root, text=messages[0])
    label2 = tk.Label(root, text=messages[1])
    textbox1 = tk.Entry(root, width=18)
    textbox2 = tk.Entry(root, width=18)
    button = tk.Button(root, text=button_text, command=on_return)
    textbox1.bind('<Return>', on_return)
    textbox1.focus_set()
    textbox2.bind('<Return>', on_return)
    textbox2.focus_set()

    label1.grid(row=0, column=0)
    label2.grid(row=1, column=0)
    textbox1.grid(row=0, column=1)
    textbox2.grid(row=1, column=1)
    button.grid(row=2, column=0, columnspan=2)

    root.mainloop()
    return text


heads_for_table_by_label = {
    'University table': ('university_id', 'address', 'web_site', 'university_name'),
    'Faculty table': ('faculty_id', 'web_site', 'faculty_name', 'university_id'),
    'Group table': ('group_id', 'group_name', 'course', 'faculty_id'),
    'Student table': ('record_card_id', 'student_id', 'scholarship', 'student_name', 'student_surname'),
    'Group - student relation table': ('group_id', 'student_id'),
    'Group - class leader relation table': ('group_id', 'student_id'),
    'Subject': ('subject_id', 'name'),
    'Laboratory work': ('lab_id', 'subject_id', 'max_mark', 'topic'),
    'Control work': ('control_work_id', 'subject_id', 'max_mark', 'topic'),
    'Group - lab relation table': ('lab_id', 'group_id', 'deadline'),
    'Group - CW relation table': ('control_work_id', 'group_id', 'deadline'),
    'Group view': ('group id', 'group name', 'course', 'faculty', 'university'),
    'Students with scholarship': ('record card', 'fullname', 'scholarship'),
    'Students data': ('fullname', 'record card', 'group id', 'group name', 'course', 'faculty', 'university'),
    'Class leaders': ('fullname', 'record card', 'group id', 'group name', 'course', 'faculty', 'university'),
    'Subject content': ('Name', 'Mark', 'Topic'),
    'CW and labs view': ('Subject', 'group id', 'deadline', 'Max', 'Topic'),
    'Scores': ('student id', 'record card', 'fullname', 'Mark', 'Max', 'Topic', 'ID', 'Subject'),
    'Student lab results': ('student id', 'lab id', 'mark'),
    'Student cw results': ('student id', 'CW id', 'mark'),
}

options = ('*font', ('verdana', 12, 'bold'))
