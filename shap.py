from tkinter import *
top = Tk()
top.title("shkl")
entry = Entry(top)
entry.pack()
def shkl():
    if entry.get() == "oval":
    #--------------oval--------------------------
        def rsm():
            C = Canvas(top, height=800, width=800)
            a = int(z1.get())
            b = int(z2.get())
            c = int(z3.get())
            d = int(z4.get())
            coord = a,b,c,d
            arc = C.create_oval(coord, fill="Azure")
            C.pack()
        Label(top, text="Enter First Number").pack()
        z1=Entry(top)
        z1.pack()
        Label(top, text="Enter Second Number").pack()
        z2=Entry(top)
        z2.pack()
        Label(top, text="Enter  Number 3").pack()
        z3=Entry(top)
        z3.pack()
        Label(top, text="Enter  Number 4").pack()
        z4=Entry(top)
        z4.pack()
        Button(top, text="creat", command=rsm).pack()
    #---------------rectangel---------------------
    elif entry.get() == "rectangel":
        def rsm():
            C = Canvas(top, height=800, width=800)
            a = int(z1.get())
            b = int(z2.get())
            c = int(z3.get())
            d = int(z4.get())
            coord = a, b, c, d
            arc = C.create_rectangle(coord, fill="Cyan")
            C.pack()
        Label(top, text="Enter First Number").pack()
        z1=Entry(top)
        z1.pack()
        Label(top, text="Enter Second Number").pack()
        z2=Entry(top)
        z2.pack()
        Label(top, text="Enter  Number 3").pack()
        z3=Entry(top)
        z3.pack()
        Label(top, text="Enter  Number 4").pack()
        z4=Entry(top)
        z4.pack()
        Button(top, text="creat", command=rsm).pack()
    #--------------treangel------------------
    elif entry.get()== "treangel":
        def rsm():
            C = Canvas(top, height=1000, width=1000)
            a = int(z1.get())
            b = int(z2.get())
            c = int(z3.get())
            d = int(z4.get())
            e = int(z5.get())
            v = int(z6.get())
            f = int(z7.get())
            k = int(z8.get())
            coord = [a,b,c,d,e,v,f,k]
            C.create_polygon(coord, fill="green")
            C.pack()
        Label(top, text="Enter  number 1 ").pack()
        z1=Entry(top)
        z1.pack()
        Label(top, text="Enter  number 2").pack()
        z2=Entry(top)
        z2.pack()
        Label(top, text="Enter  number 3").pack()
        z3=Entry(top)
        z3.pack()
        Label(top, text="Enter  number 4").pack()
        z4=Entry(top)
        z4.pack()
        Label(top,text="Enter number 5").pack()
        z5=Entry(top) 
        z5.pack()
        Label(top, text="Enter number 6").pack()
        z6=Entry(top)
        z6.pack()
        Label(top, text="Enter number 7").pack()
        z7=Entry(top)
        z7.pack()
        Label(top, text="Enter number 8").pack()
        z8=Entry(top)
        z8.pack()  
        Button(top, text="creat", command=rsm).pack()
    else:
        ntf = Label(top,text="not found")
        ntf.pack()
ans = Button(top,text="Search",command=shkl)
ans.pack()
top.mainloop()