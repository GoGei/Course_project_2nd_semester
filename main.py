import tkinter as tk
from Controller.MainWindow import MainWindow


if __name__ == '__main__':
    root = tk.Tk()
    root.option_add('*font', ('verdana', 40, 'bold'))
    root.title('Course project')
    root.geometry('720x580')
    app = MainWindow(root)
    root.mainloop()
