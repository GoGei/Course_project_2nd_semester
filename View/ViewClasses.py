import tkinter as tk
from tkinter.ttk import *
from Utils import utils


class TableClass(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=list()):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self._init_table(headings, rows)

    def _init_table(self, headings, rows):
        self.cols = headings
        self.table = Treeview(self.parent, columns=self.cols, show='headings')
        for col in self.cols:
            self.table.heading(col, text=col)
        self.table.pack(fill=tk.BOTH, expand=1)
        self.insert(rows)

    def treeview_sort_column(self, col, reverse):
        l = [(self.table.set(k, col), k) for k in self.table.get_children('')]
        l.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):
            self.table.move(k, '', index)

        # reverse sort next time
        self.table.heading(col, text=col, command=lambda _col=col: \
            self.treeview_sort_column(_col, not reverse))

    def set_new(self, headings, rows):
        self.table.destroy()
        self._init_table(headings, rows)

    def insert(self, rows):
        for values in rows:
            self.table.insert("", "end", values=values)

    def clear(self):
        self.table.delete(*self.table.get_children())


class DropBox(tk.Frame):
    def __init__(self, parent, options, commands, dropbox_str, window_str, db, row, column, columnspan=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.options = options
        self.commands = commands
        self.drop_str = dropbox_str,
        self.title = window_str
        self.db = db

        self.dropbox_str = tk.StringVar()
        self.dropbox_str.set(self.drop_str)
        self.dropbox = tk.OptionMenu(self.parent, self.dropbox_str, *self.options, command=self._get_select)

        self.dropbox.grid(row=row, column=column)
        if columnspan is not None:
            self.dropbox.grid(row=row, column=column, columnspan=columnspan)

    def _get_select(self, label):
        try:
            self.window.destroy()
        except AttributeError:
            pass

        self.window = tk.Toplevel()
        self.window.title(self.title)
        self.window.option_add(*utils.options)

        self.table = TableClass(self.window, headings=('column1', 'column2', 'column3', 'column4', 'column5'))
        self.result = self.commands[label]()
        self.table.set_new(utils.heads_for_table_by_label[label], self.result)
