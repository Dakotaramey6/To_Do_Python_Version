from tkinter import *

window = Tk()
title_of_todo = Label(window, text='My to do list',
                      width="250", font='Cursive')
title_of_todo['background'] = '#856ff8'
title_of_todo.pack()

user_input = Entry(window)
list_of_todo = []

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
            list_of_todo.append(i)


def save_to_file(what_to_save):
    list_of_todo.append(what_to_save)
    with open('task.txt', 'a') as save_file:
        save_file.write(f'o {what_to_save}\n')


def add_to_do(event):
    to_do_string = user_input.get()
    if len(to_do_string) > 0:
        items_in_list.insert(END, 'o '+to_do_string)
        save_to_file(to_do_string)
        user_input.delete(0, END)


def remove_to_do(event):
    string_of_slected_item = items_in_list.get(ACTIVE)
    items_in_list.delete(ACTIVE)

    for item_To_delete in list_of_todo:
        if item_To_delete == string_of_slected_item:
            list_of_todo.remove(item_To_delete)
    with open('task.txt', 'w') as file_remove_output:
        for i in list_of_todo:
            file_remove_output.writelines(i)


init()
remove_btn.bind('<Button-1>', remove_to_do)
window.bind('<Return>', add_to_do)
window.title('To Do List')
window.geometry('250x460+10+10')
window['background'] = '#856ff8'
window.mainloop()
