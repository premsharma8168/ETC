# # to-do list

import tkinter as tk

class ToDoList:
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        mainwindow.title("To Do List")
        mainwindow.geometry("400x300")


        self.entry = tk.Entry(mainwindow)
        self.entry.grid(row=0, column=0)


        self.add_button = tk.Button(mainwindow, text="Add item", command=self.add_item)
        self.add_button.grid(row=0, column=1)

        self.delete_button = tk.Button(mainwindow, text="Delete item", command=self.delete_item)
        self.delete_button.grid(row=2, column=0)

        self.delete_all_button = tk.Button(mainwindow, text="Delete all items", command=self.delete_all_items)
        self.delete_all_button.grid(row=2, column=1)

        self.undo_button = tk.Button(mainwindow, text="Undo", command=self.undo)
        self.undo_button.grid(row=2, column=2)

        self.list_box = tk.Listbox(mainwindow, width=30)
        self.list_box.grid(row=1, columnspan=2)

    def add_item(self):
        data = self.entry.get()
        self.list_box.insert(tk.END, data)
        self.entry.delete(0, tk.END)

    def delete_item(self):
        select_index = self.list_box.curselection()
        self.deleted_item=self.list_box.get(select_index[0])
        if select_index:
            self.list_box.delete(select_index)

    def undo(self):
        self.list_box.insert(0,self.deleted_item)

    def delete_all_items(self):
        self.list_box.delete(0, tk.END)

root = tk.Tk()
todo_list = ToDoList(root)
root.mainloop()

