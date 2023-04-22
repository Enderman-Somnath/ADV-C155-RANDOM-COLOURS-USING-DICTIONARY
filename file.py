#Linking
from tkinter import *
import random
root=Tk()

#Configuring Window
root.title("Random Color Generator")
root.geometry("800x600")

#Function
def colorchange():
    #Attempt Code
    random1 = random.randint(0,9)
    random2 = random.randint(0,9)
    random3 = random.randint(0,9)
    random4 = random.randint(0,9)
    random5 = random.randint(0,9)
    random6 = random.randint(0,9)
    random7 = random.randint(0,9)
    random8 = random.randint(0,9)
    color1 = "#" + str(random1) + str(random2) + str(random3) + str(random4) + str(random5) + str(random6) + str(random7) + str(random8)
    
    #With help of ChatGPT
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    root.configure(background=color)
    
#Button
button = Button(root,text="Click this button to change color",command=colorchange,bg="#333333",fg="#ffffff",  bd=0)
button.place(relx=0.5,rely=0.5,anchor=CENTER)
#To make app functional
root.mainloop()