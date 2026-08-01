from tkinter import*
import calendar
def showCal():
    pass




#drivercode
#if __name__="__main__":
gui=Tk()
gui.config(background="white")
gui.title("calendar")
gui.geometry("500x250")

cal=Label(gui,text="CALENDAR",font=("times",20,"bold"))
year=Label(gui,text="enter year")
year_input=Entry(gui)

show_calendar=Button(gui,text="show calendar",command=None)                                 
exit_button=Button(gui,text="Exit",command=exit)

#positioning
cal.place(x=200,y=50)
year.place(x=200,y=100)
year_input.place(x=200,y=125)
show_calendar.place(x=75,y=175)
exit_button.place(x=325,y=175)

gui.mainloop()