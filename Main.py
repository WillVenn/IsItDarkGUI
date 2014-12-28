from tkinter import *
import time
#---------------------------------------------------------

#Window code:
root = Tk()
root.title("Is it dark outside? - Will Venn")
root.geometry("850x500")
img = PhotoImage(file='nightday.gif') #Setting the application icon
root.tk.call('wm', 'iconphoto', root._w, img) #setting icon still...
photo = PhotoImage(file="nightday.gif") #Is the python logo in the middle/boottom of the window
w = Label(root, image=photo)
w.photo = photo
w.pack()

#---------------------------------------------------------
#labels:
label_intro = Label(root, text="Is it dark outside?").pack()
label_introCont = Label(root, text="Because who opens the curtains nowadays!").pack()
#---------------------------------------------------------
#Light/Dark times:

#Month_number : Sunset_hour

dark = {
	1:16,
	2:17,
	3:18,
	4:19,
	5:19,
	6:20,
	7:20,
	8:19,
	9:18,
	10:17,
	11:16,
	12:16
	}

#Month_number : Sunrise_hour

light = {
	1:8,
	2:7,
	3:6,
	4:5,
	5:4,
	6:4,
	7:4,
	8:5,
	9:6,
	10:6,
	11:7,
	12:8
	}

#---------------------------------------------------------
#Getting current time, using 'time' modules
time_now = time.localtime()
#---------------------------------------------------------

#Light/Dark algorithim

#Use the 'light' 'dark' dictionaries

#It's dark if the hour is later than or equal to the sunset time
#or earlier than the sunrise time

def darkOrLight():
	if time_now.tm_hour >=dark[time_now.tm_mon] or time_now.tm_hour < light[time_now.tm_mon]:
		print ("Yes")
		label_yes = Label(root, text="Yes it is!").pack()
		photo = PhotoImage(file="moon.gif") #Is the python logo in the middle/boottom of the window
		w = Label(root, image=photo)
		w.photo = photo
		w.pack()
		##yesWin = Tk()
		##yesWin.title("Yes it is!")
		##label_yes = Label(yesWin, text="Yes it is!").pack()
	else:
		print ("No")
		label_no = Label(root, text="No, no it is not.").pack()
		photo = PhotoImage(file="sun.gif") #Is the python logo in the middle/boottom of the window
		w = Label(root, image=photo)
		w.photo = photo
		w.pack()
		##noWin = Tk()
		##noWin.title("No it is not.")
		##label_no = Label(noWin, text="No, no it is not.").pack()

#---------------------------------------------------------
#Buttons
Button_darkLight = Button(root, text="Is it dark outside?", bd=3, command=darkOrLight).pack()
#---------------------------------------------------------


#---------------------------------------------------------
#Loops:
root.mainloop()
#---------------------------------------------------------
