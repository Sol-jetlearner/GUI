from tkinter import*
root=Tk()
root.geometry("600x300")
root.title("restaurant")

#adding labels
food=Label(root,text="Food",bg="orange")
drink=Label(root,text="Drink",bg="pink")
dessert=Label(root,text="Dessert",bg="purple")

#entry boxes
user_food=Entry(root,width=20)
user_drink=Entry(root,width=20)
user_dessert=Entry(root,width=20)

btn=Button(root,text="submit",command=None)
btn.place(x=100,y=250)

#positioning
food.place(x=100,y=100)
drink.place(x=100,y=150)
dessert.place(x=100,y=200)
user_food.place(x=200,y=100)
user_drink.place(x=200,y=150)
user_dessert.place(x=200,y=200)
root.mainloop()