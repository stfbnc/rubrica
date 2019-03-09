from Tkinter import *
import tkMessageBox

# callback for search button
def Search(event = None):
    search_name = name_to_search.get()
    if search_name == '':
        tkMessageBox.showinfo("","Insert name or number!")
    else:
        names = []
        phones = []
        for i in name_phone:
            if search_name.lower() in i.lower():
                cols = i.split(sep)
                names.append(cols[0])
                phones.append(cols[1])
        if len(names) != 0:
            all_text.config(state = 'normal')
            all_text.delete('1.0',END)
            for i in range(len(names)):
                all_text.insert(END,names[i] + ' ' + phones[i] + '\n')
            all_text.config(state = 'disabled')
        else:
            tkMessageBox.showinfo("","Not found!")

# callback for add button
def Add():
    def Add_button(event = None):
        add_name = entry_name.get()
        add_number = entry_number.get()
        if (add_name == '') or (add_number == ''):
            tkMessageBox.showinfo("","Insert name or number!")
        else:
            add_window.destroy()
            name_phone.append(add_name + sep + add_number)
            message = add_name + ' added!'
            tkMessageBox.showinfo("",message)
    add_window = Toplevel()
    add_window.title("Add name and number")
    Label(add_window,text = "Insert name").grid(row = 0,column = 0,sticky = W)
    entry_name = Entry(add_window)
    entry_name.grid(row = 0,column = 1)
    Label(add_window,text = "Insert number").grid(row = 1,column = 0,sticky = W)
    entry_number = Entry(add_window)
    entry_number.grid(row = 1,column = 1)
    Button(add_window,text = "Add",command = Add_button).grid(row = 2,column = 0,sticky = W)
    add_window.bind('<Return>',Add_button)
    Button(add_window,text = "Quit",command = add_window.destroy).grid(row = 2,column = 1,sticky = W)

# callback for remove button
def Remove():
    def Remove_button(event = None):
        remove_name = entry_name.get()
        if remove_name == '':
            tkMessageBox.showinfo("","Insert name or number!")
        else:
            remove_window.destroy()
            check = 0
            for i in name_phone:
                cols = i.split(sep)
                if (remove_name.lower() == cols[0].lower()) or (remove_name.lower() == cols[1].lower()):
                    name_phone.remove(i)
                    message = remove_name + ' removed!'
                    tkMessageBox.showinfo("",message)
                    check = 1
                    break
            if check == 0:
                tkMessageBox.showinfo("","Not found!")
    remove_window = Toplevel()
    remove_window.title("Remove name and number")
    Label(remove_window,text = "Insert name or number").grid(row = 0,column = 0,sticky = W)
    entry_name = Entry(remove_window)
    entry_name.grid(row = 0,column = 1)
    Button(remove_window,text = "Remove",command = Remove_button).grid(row = 2,column = 0,sticky = W)
    remove_window.bind('<Return>',Remove_button)
    Button(remove_window,text = "Quit",command = remove_window.destroy).grid(row = 2,column = 1,sticky = W)

# callback for replace button
def Replace():
    def Replace_button(event = None):
        replace_name = entry_name.get()
        replace_number = entry_number.get()
        if (replace_name == '') or (replace_number == ''):
            tkMessageBox.showinfo("","Insert name or number!")
        else:
            replace_window.destroy()
            check = 0
            for i in range(len(name_phone)):
                cols = name_phone[i].split(sep)
                if (replace_name.lower() == cols[0].lower()) or (replace_number.lower() == cols[1].lower()):
                    name_phone[i] = replace_name + sep + replace_number
                    message = replace_name + ' replaced!'
                    tkMessageBox.showinfo("",message)
                    check = 1
                    break
            if check == 0:
                tkMessageBox.showinfo("","Not found!")
    replace_window = Toplevel()
    replace_window.title("Replace number")
    Label(replace_window,text = "Insert name").grid(row = 0,column = 0,sticky = W)
    entry_name = Entry(replace_window)
    entry_name.grid(row = 0,column = 1)
    Label(replace_window,text = "Insert number").grid(row = 1,column = 0,sticky = W)
    entry_number = Entry(replace_window)
    entry_number.grid(row = 1,column = 1)
    Button(replace_window,text = "Replace",command = Replace_button).grid(row = 2,column = 0,sticky = W)
    replace_window.bind('<Return>',Replace_button)
    Button(replace_window,text = "Quit",command = replace_window.destroy).grid(row = 2,column = 1,sticky = W)

# callback for quit button
def Quit():
    f = open(file_name,'w')
    for i in name_phone:
        f.write('%s\n' % (i))
    f.close()
    root.quit()

# main
root = Tk()
root.wm_title("Phone book")
root.geometry("500x300")
root.resizable(width = False, height = False)

topframe = Frame(root)
topframe.grid(row = 0,column = 0)
photo = PhotoImage(file = "phone.gif")
Label(topframe,image = photo).grid(row = 0,column = 0)

midframe1 = Frame(root)
midframe1.grid(row = 1,column = 0)
name_to_search = Entry(midframe1)
name_to_search.grid(row = 0,column = 0)
Button(midframe1,text = "Search",command = Search).grid(row = 0,column = 1)
root.bind('<Return>',Search)

midframe2 = Frame(root)
midframe2.grid(row = 2,column = 0)
Button(midframe2,text = "Add",command = Add).grid(row = 0,column = 0)
Button(midframe2,text = "Remove",command = Remove).grid(row = 0,column = 1)
Button(midframe2,text = "Replace",command = Replace).grid(row = 0,column = 2)

bottomframe = Frame(root)
bottomframe.grid(row = 3,column = 0)
Button(bottomframe,text = "Quit",command = Quit).grid(row = 0,column = 0)

file_name = 'rubrica.txt'
sep = ' -> '
name_phone = []
f = open(file_name,'r')
for line in f:
    name_phone.append(line.rstrip())
f.close()
all_text = Text(topframe,height = 10,width = 40)
all_text.see(END)
all_text.grid(row = 0,column = 1)
all_text.config(state = 'disabled')

root.mainloop()
