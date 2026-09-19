from tkinter import*
import calendar
def showCal():
    new_gui=Tk()
    new_gui.title("new calendar")
    new_gui.geometry("750x1000")
    fetch_year=int(year_input.get())
    cal_content=calendar.calendar(fetch_year)
    cal_year=Label(new_gui,text=cal_content,font="consolas 10 bold")
    cal_year.grid(row=5,column=1,padx=20)


    new_gui.mainloop()
#drivercode
if __name__=="__main__":
    gui=Tk()
    gui.config(background="white")
    gui.title("calendar")
    gui.geometry("500x250")

    cal=Label(gui,text="CALENDAR",font=("times",20,"bold"))
    year=Label(gui,text="enter year")
    year_input=Entry(gui)

    show_calendar=Button(gui,text="show calendar",command=showCal)                                 
    exit_button=Button(gui,text="Exit",command=exit)

    #positioning
    cal.place(x=200,y=50)
    year.place(x=200,y=100)
    year_input.place(x=200,y=125)
    show_calendar.place(x=75,y=175)
    exit_button.place(x=325,y=175)

gui.mainloop()
