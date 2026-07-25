from tkinter import*
root=Tk()
root.geometry("600x300")
root.title("login")
root.config(background="blue")
#adding labels
user_name=Label(root,text="UserName",bg="orange",fg="purple")
password=Label(root,text="Password",bg="pink",fg="green")

#entry boxes
user_inputbox=Entry(root,width=30)
user_password=Entry(root,width=30,show="*")

btn=Button(root,text="submit",bd=9,command=None)
btn.place(x=100,y=200)

#positioning
user_name.place(x=100,y=100)
password.place(x=100,y=150)
user_inputbox.place(x=200,y=100)
user_password.place(x=200,y=150)
root.mainloop()