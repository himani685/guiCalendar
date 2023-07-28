# from tkinter import *
# import calendar





# root = Tk()
# root.title("Calendar 2023")
# root.geometry("300x300")

# def show():
#     a = int(spin1.get())
#     b = int(spin2.get())

#     cal = calendar.month(b,a)  #will have to pass year and then month value
#     txt.delete(0.0,END)
#     txt.insert(INSERT)

# label1 = Label(root,text="Month",font=("arial",9,"Bold")).place(x=15,y=0)
# label2 = Label(root,text="Year",font=("arial",9,"Bold")).place(x=115,y=0)
# spin1 = Spinbox(root,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=4)
# spin1.place(x=60,y=0)

# spin2 = Spinbox(root,from_1999,to=2100,width=4)
# spin2.place(x=150,y=0)

# #creating button
# btn=Button(root,text="show",font=("arial",9,"Bold"),command=show).place(x=100,y=30)

# txt =Text(root,width=24,height=8)
# txt.place(x=20,y=57)

# #import module
# from tkinter import *
# from tkcalendar import *
# hm = Tk()
# hm.title("Calendar Button")
# cl = Calendar(hm)
# def select_date():
#     date = cl.get_date()  #before it create label
#     print(date)

# button = Button(hm, text="Select Date", command= select_date)  #create functn of date

# hm.geometry("800x400")
# #show_button = Button(root,text="Select Date",fg="red".bg="black")
# cl.pack()
# hm.mainloop()


from tkinter import *
from tkcalendar import *
hm = Tk()
hm.geometry('800x400')
hm.title("Calendar Button")
cl = Calendar(hm)
cl.pack(pady=20)
def select_date():
    date.config(text=""+cl.get_date())  #before it create label
button = Button(hm, text="Select Date", command= select_date) #create functn of date
button.pack()
#show_button = Button(root,text="Select Date",fg="red".bg="black")
date=Label(hm,text="")
date.pack(pady=20)
hm.mainloop()




# import module
# import calendar

# yy = 2023
# mm = 4

# # display the calendar
# print(calendar.month(yy, mm))







