from tkinter import*
root=Tk()
root.geometry("200x300")
btn=Button(root,text="click me",background="green",foreground="yellow",
           bd=7,activebackground="red",activeforeground="blue",command=root.destroy)
btn.pack()






root.mainloop()