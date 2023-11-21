from cProfile import label
from tkinter import *

window = Tk()

user_input = Entry(window, text='o ')

user_input.pack(pady=4, padx=4)
items_in_list = Listbox(window, height=22, width=30)
items_in_list.pack(pady=4, padx=4)
remove_btn = Button(window, text="Delete selected item")
remove_btn.pack()


def init():
    with open('task.txt', 'r') as get_values:
        items = get_values.readlines()
        for i in items:
            items_in_list.insert(END, i)


def save_to_file(what_to_save):
    with open('task.txt', 'a') as save_file:
        save_file.write(f'{what_to_save}\n')


def add_to_do(event):
    to_do_string = user_input.get()
    if len(to_do_string) > 0:
        items_in_list.insert(END, to_do_string)
        save_to_file(to_do_string)
        user_input.delete(0, END)


def remove_to_do(event):
    items_in_list.delete(ACTIVE)
    with open('task.txt', 'r+') as file_remove_output:
        lines = file_remove_output.readlines()

        file_remove_output.truncate()
        for line in lines:
            if items_in_list.get(ACTIVE) == line:
                lines.remove(line)
            file_remove_output.write(line)


init()
remove_btn.bind('<Button-1>', remove_to_do)
window.bind('<Return>', add_to_do)
window.title('To Do List')
window.geometry('250x440+10+10')
window['background'] = '#856ff8'
window.mainloop()
