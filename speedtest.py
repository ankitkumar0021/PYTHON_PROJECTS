from tkinter import * 
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str( round(sp.dpwnload()/(10**6),3))+" Mbps"
    up = str( round(sp.dpwnload()/(10**6),3))+" Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)
    

sp = Tk()
sp.title("Internet speed test")
sp.geometry("500x550")
sp.config(bg="Pink")

lab = Label(sp,text="Internet speed test",font=("Times New Roman",20,"bold",),bg="Pink",fg="Blue")
lab.place(x=60,y=40,height=50,width=380)

lab = Label(sp,text="Download Speed",font=("Times New Roman",20,"bold",))
lab.place(x=60,y=130,height=50,width=380)

lab_down = Label(sp,text="00",font=("Times New Roman",20,"bold",))
lab_down.place(x=60,y=200,height=50,width=380)

lab = Label(sp,text="Upload speed test",font=("Times New Roman",20,"bold",))
lab.place(x=60,y=290,height=50,width=380)

lab_up = Label(sp,text="00",font=("Times New Roman",20,"bold",))
lab_up.place(x=60,y=360,height=50,width=380)

button = Button(sp,text="Check Speed",font=("Times New Roman",20,"bold",),relief=RAISED,bg="Light Green",command=speedcheck)
button.place(x=60,y=460,height=40,width=380)

sp.mainloop()