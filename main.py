from cProfile import label
from tkinter import *

window = Tk()
title_of_gui = Label(
    text='To Do List \nDouble click to remove items')
user_input = Entry(window, text='o ')
title_of_gui.pack()
user_input.pack(pady=4, padx=4)
items_in_list = Listbox(window, height=22, width=30)
items_in_list.pack(pady=4, padx=4)


def save_to_file(what_to_save):
    with open('task.txt', 'a') as save_file:
        save_file.write(f'\n{what_to_save}')


def add_to_do(event):
    to_do_string = user_input.get()
    items_in_list.insert(END, to_do_string)
    user_input.delete(0, END)
    save_to_file(to_do_string)


def remove_to_do(event):
    items_in_list.delete(ACTIVE)
    with open('task.txt', 'r+') as file_remove_output:
        lines = file_remove_output.readlines()

        file_remove_output.truncate()
        for line in lines:
            if items_in_list.get(ACTIVE) == line[:-2]:
                lines.remove(line)
            file_remove_output.write(line)

        file_remove_output.close()


items_in_list.bind('<Double-Button-1>', remove_to_do)
window.bind('<Return>', add_to_do)
window.title('To Do List')
window.geometry('250x400+10+10')
window['background'] = '#856ff8'
window.mainloop()
