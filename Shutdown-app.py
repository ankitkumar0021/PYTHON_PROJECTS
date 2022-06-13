from tkinter import *                            #For GUI
import os										 #For using operating system
#Using scripts of operating system
def Restart():
	os.system("shutdown /r /t 1")    
def Restart_Time():
	os.system("shutdown /r /t 20")
def Log_out():
	os.system("shutdown -1")
def Shutdown():
	os.system("shutdown /r /t 1") 

st=Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Blue")

#Making the buttons

r_button = Button(st,text="Restart",font=("Times New Roman",15,"bold"),
	relief=RAISED,cursor="plus",command=Restart)
r_button.place(x=200,y=60,height=40,width=180)

rt_button = Button(st,text="Restart with Time",font=("Times New Roman",15,"bold"),
	relief=RAISED,cursor="plus",command=Restart_Time)
rt_button.place(x=200,y=170,height=50,width=180)

lg_button = Button(st,text="Log out",font=("Times New Roman",15,"bold"),
	relief=RAISED,cursor="plus",command=Log_out)
lg_button.place(x=200,y=270,height=50,width=180)

lg_button = Button(st,text="ShutDown ",font=("Times New Roman",15,"bold"),
	relief=RAISED,cursor="plus",command=Shutdown)
lg_button.place(x=200,y=370,height=50,width=180)




st.mainloop()