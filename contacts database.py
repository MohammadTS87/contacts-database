
from tkinter import *
from tkinter import messagebox
import db_database
root = Tk()
root.title('UI')
root.resizable(0 , 0)
root.geometry('600x400')
root.config(bg='purple')

db1 = db_database.Karmand('I://test//badbakhti.db')
# =========== Function =====================
#============insert=========================    
def insert(): 
    if ent1_fname.get()=='' or len(ent2_lname.get())==0:
        messagebox.showerror('EROR','fname or lname empty')
        return
    db1.insert(ent1_fname.get(), ent2_lname.get(), ent3_city.get(), ent4_phone.get())
    clear()
    Show()
#============show=======================
def Show():
    lst.delete(0 , END)
    records = db1.Show()
    for i in records:
        lst.insert(END, i)
#==========select========================
def select(event):
    try:
        global selected_item
        index = lst.curselection()
        selected_item = lst.get(index)
        ent1_fname.delete(0, END)
        ent1_fname.insert(END, selected_item[1])
        ent2_lname.delete(0, END)
        ent2_lname.insert(END, selected_item[2])
        ent3_city.delete(0, END)
        ent3_city.insert(END, selected_item[3])
        ent4_phone.delete(0, END)
        ent4_phone.insert(END, selected_item[4])
    except IndexError:
        pass
#=======update================================
def Update():
    up =  messagebox.askyesno('ERROR', 'are you sure who you want to update this object !!!!!!')
    if up :
        db1.Update(selected_item[0] , ent1_fname.get() , ent2_lname.get() , ent3_city.get() , ent4_phone.get())
        Show()
#==========select========================
def Search():
    Object = ent5_search.get()
    record = db1.Search(Object)
    lst.delete(0,END)
    lst.insert(0 ,record)
    ent5_search.delete(0 , END)
    ent5_search.focus_set()
    if len(record) == 0:
        messagebox.showerror('ERROR','this program we dont have any object !!!!!!!!!')
        Show()
    
#============== clear ========================
def clear():
    ent1_fname.delete(0,END)
    ent2_lname.delete(0,END)
    ent3_city.delete(0,END)
    ent4_phone.delete(0,END)
    ent1_fname.focus_set()
#============ delete =======================
def delete():
    index = lst.curselection()
    if index:
        data = lst.get(index)
        information = messagebox.askyesno('EROR', 'are you sure who you want to delite this data ? ')
        if information :
            db1.delete(data[0])
            Show()
    else:
        messagebox.showerror('EROR','please select one data !!!')
        Show()
#=============== exit =====================
def Exit():
    confirm_exit = messagebox.askyesno('are you sure','are you sure who you want to exit ? ')
    if confirm_exit:
        root.destroy()

# =========== Button =====================
btn1 = Button(root , text = 'Insert', width=16,bg='black',fg='yellow' ,command= insert)
btn2 = Button(root , text = 'Delete', width=16,bg='black',fg='yellow' , command= delete)
btn3 = Button(root , text = 'Update', width=16 ,bg='black',fg='yellow' , command= Update)
btn4 = Button(root , text = 'Show', width=16,bg='black',fg='yellow', command= Show)
btn5 = Button(root , text = 'Clear', width=16,bg='black',fg='yellow' , command= clear)
btn6 = Button(root , text = 'Exit', width=16 ,bg='black',fg='yellow' , command = Exit)
btn7 = Button(root , text = 'Search', width=16 ,bg='black',fg='yellow' , command = Search)
#==============lst================================
lst = Listbox(root , width = 80 , height= 10,bg='green',fg='black')
# =========== Label =====================
lbl1_fname = Label(root , text = 'Fname: ' ,bg='black',fg='yellow' , font='arial 14 bold',width=6)
lbl2_lname = Label(root , text = 'Lname: ',bg='black',fg='yellow' , font='arial 14 bold',width=6)
lbl3_city = Label(root , text = 'City: ',bg='black',fg='yellow' , font='arial 14 bold',width=6)
lbl4_tel = Label(root , text = 'Tel: ',bg='black',fg='yellow' , font='arial 14 bold',width=6)
# =========== Entry =====================
ent1_fname = Entry(root , bg='yellow',fg='black')
ent2_lname = Entry(root, bg='yellow',fg='black')
ent3_city = Entry(root, bg='yellow',fg='black')
ent4_phone = Entry(root, bg='yellow',fg='black')
ent5_search = Entry(root, bg='yellow',fg='black')
# =========== Place =====================
lbl1_fname.place(x = 10 , y = 10)
lbl2_lname.place(x = 10 , y = 50)
lbl3_city.place(x = 300 , y = 10)
lbl4_tel.place(x = 300 , y = 50)
#============ent============
ent1_fname.place(x = 100 , y = 10)
ent2_lname.place(x = 100 , y = 50)
ent3_city.place(x = 390 , y = 10)
ent4_phone.place(x = 390 , y = 50)
ent5_search.place(x = 200 , y =270)
#========== lst ======================
lst.place(x = 70 , y = 100)
#=========button======================
btn1.place(x = 10 , y = 300)
btn2.place(x = 10 , y = 350)
btn3.place(x = 200 , y = 300)
btn4.place(x = 200 , y = 350)
btn5.place(x = 390 , y = 300)
btn6.place(x = 390 , y = 350)
btn7.place(x = 390 , y = 270)
#=======select=========================
lst.bind('<<ListboxSelect>>', select)
#================mainloop===============
root.mainloop()
























