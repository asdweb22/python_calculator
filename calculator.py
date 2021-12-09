# tkinter calculator


from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        scvalue.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.title("Calculator")
root.wm_iconbitmap("calculator1.ico")
root.geometry("250x500")
root.minsize(250, 500)
root.maxsize(250, 500)

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="gray")
b1 = Button(f, text="9", font="lucida 15 bold", padx=10)
b2 = Button(f, text="8", font="lucida 15 bold", padx=10)
b3 = Button(f, text="7", font="lucida 15 bold", padx=10)

b1.pack(side=LEFT, padx=18, pady=12)
b2.pack(side=LEFT, padx=18, pady=12)
b3.pack(side=LEFT, padx=18, pady=12)

b1.bind("<Button-1>", click)
b2.bind("<Button-1>", click)
b3.bind("<Button-1>", click)

f.pack(fill=X)


f = Frame(root, bg="gray")
b1 = Button(f, text="6", font="lucida 15 bold", padx=10)
b2 = Button(f, text="5", font="lucida 15 bold", padx=10)
b3 = Button(f, text="4", font="lucida 15 bold", padx=10)

b1.pack(side=LEFT, padx=18, pady=12)
b2.pack(side=LEFT, padx=18, pady=12)
b3.pack(side=LEFT, padx=18, pady=12)

b1.bind("<Button-1>", click)
b2.bind("<Button-1>", click)
b3.bind("<Button-1>", click)

f.pack(fill=X)


f = Frame(root, bg="gray")
b1 = Button(f, text="3", font="lucida 15 bold", padx=10)
b2 = Button(f, text="2", font="lucida 15 bold", padx=10)
b3 = Button(f, text="1", font="lucida 15 bold", padx=10)

b1.pack(side=LEFT, padx=18, pady=12)
b2.pack(side=LEFT, padx=18, pady=12)
b3.pack(side=LEFT, padx=18, pady=12)

b1.bind("<Button-1>", click)
b2.bind("<Button-1>", click)
b3.bind("<Button-1>", click)

f.pack(fill=X)


f = Frame(root, bg="gray")
b1 = Button(f, text="0", font="lucida 15 bold", padx=10)
b2 = Button(f, text="-", font="lucida 15 bold", padx=12)
b3 = Button(f, text="*", font="lucida 15 bold", padx=12)

b1.pack(side=LEFT, padx=18, pady=12)
b2.pack(side=LEFT, padx=18, pady=12)
b3.pack(side=LEFT, padx=18, pady=12)

b1.bind("<Button-1>", click)
b2.bind("<Button-1>", click)
b3.bind("<Button-1>", click)

f.pack(fill=X)


f = Frame(root, bg="gray")
b1 = Button(f, text="/", font="lucida 15 bold", padx=12)
b2 = Button(f, text="%", font="lucida 15 bold", padx=8)
b3 = Button(f, text="=", font="lucida 15 bold", padx=10)

b1.pack(side=LEFT, padx=18, pady=12)
b2.pack(side=LEFT, padx=18, pady=12)
b3.pack(side=LEFT, padx=18, pady=12)

b1.bind("<Button-1>", click)
b2.bind("<Button-1>", click)
b3.bind("<Button-1>", click)

f.pack(fill=X)


f = Frame(root, bg="gray")
b1 = Button(f, text="C", font="lucida 15 bold",
            padx=8, bg="#3af3e8", fg="white")
b2 = Button(f, text="+", font="lucida 15 bold", padx=10)
b3 = Button(f, text="00", font="lucida 15 bold", padx=6)


b1.pack(side=LEFT, padx=18, pady=12)
b2.pack(side=LEFT, padx=18, pady=12)
b3.pack(side=LEFT, padx=18, pady=12)

b1.bind("<Button-1>", click)
b2.bind("<Button-1>", click)
b3.bind("<Button-1>", click)

f.pack(fill=X)

root.mainloop()
