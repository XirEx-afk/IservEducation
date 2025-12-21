from tkinter import*
from PIL import ImageTk, Image



root = Tk()
root.title("Котики")
root.geometry('800x720')
root.resizable(width=False, height=False)

imgs = {1: Image.open('Python/Lesson_9/images/ef.png'),
        2: Image.open('Python/Lesson_9/images/image.png'),
        3: Image.open('Python/Lesson_9/images/max.png'),
        4: Image.open('Python/Lesson_9/images/weg.png')}


img_b1 = imgs[1].resize((150,150))
img_b1 = ImageTk.PhotoImage(img_b1)

img_b2 = imgs[2].resize((150,150))
img_b2 = ImageTk.PhotoImage(img_b2)

img_b3 = imgs[3].resize((150,150))
img_b3 = ImageTk.PhotoImage(img_b3)

img_b4 = imgs[4].resize((150,150))
img_b4 = ImageTk.PhotoImage(img_b4)

variant = {1: img_b1, 2: img_b2, 3: img_b3, 4: img_b4}

var = IntVar()
var.set(0)

b1 = Radiobutton(width=150, height=150, indicatoron=0, variable=var, value=1, image=img_b1)
b1.place(relx=0.12, rely=0.75)

b2 = Radiobutton(width=150, height=150, indicatoron=0, variable=var, value=2, image=img_b2)
b2.place(relx=0.32, rely=0.75)

b3 = Radiobutton(width=150, height=150, indicatoron=0, variable=var, value=3, image=img_b3)
b3.place(relx=0.52, rely=0.75)

b4 = Radiobutton(width=150, height=150, indicatoron=0, variable=var, value=4, image=img_b4)
b4.place(relx=0.72, rely=0.75)

root.mainloop()