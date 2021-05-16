from tkinter import *
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier



# Window Configuration
root = Tk()
root.title("Callify \U0001F600  !!!")


width = 1250
height = 750
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.configure(bg="#242424")


#==========================================================================================================#
NUMBER = StringVar()

#======================================Phase: User Moudle==================================================#

#==============================================Form for the Screen=========================================#
def mainForm():
	global mainFrame, lbl_header , lbl_header2 , lbl_result1 , lbl_result2, lbl_result3
	mainFrame = Frame(root,background="#747474")
	mainFrame.pack(side= TOP,pady=80)
	lbl_header = Label(mainFrame, text="Welcome to Callify",font=('Helvetica',36,'bold'),bd=18,bg="#747474",fg="#242424")
	lbl_header.grid(row=1,column=1,columnspan=2)
	lbl_header2 = Label(mainFrame,text="             Get the Information about any Phone Number",font=('Helvetica',16),bd=18,bg="#747474",fg="#242424")
	lbl_header2.grid(row=3,column=1)
	lbl_number = Label(mainFrame,text="Enter the Number:",font=('Comic Sans MS',20),bd=18,bg="#747474",fg="#242424")
	lbl_number.grid(row=5,column=0,columnspan=2)
	ent_number = Entry(mainFrame, font=('Helvetica', 20), textvariable=NUMBER,bg="lavender", width=20)
	ent_number.grid(row=5, column=2)
	lbl_result1 = Label(mainFrame, text="Try to enter the Phone Number with country Code with + sign", font=('Helvetica', 18),bg="#747474",fg="blue")
	lbl_result1.grid(row=7,column=1 , columnspan=2)
	lbl_result2 = Label(mainFrame, text="", font=('Helvetica', 20),bg="#747474",fg="#242424")
	lbl_result2.grid(row=9, column=1,columnspan=2)
	lbl_result3 = Label(mainFrame, text="", font=('Helvetica', 20),bg="#747474",fg="#242424")
	lbl_result3.grid(row=11, column=1,columnspan=2)
	btn_find = Button(mainFrame, text="Find Out", font=('Helvetica', 24),bg="#1473E6",fg="white",bd=5,activebackground="green1",cursor="hand2", width=20, command=mainMethod)
	btn_find.grid(row=13, columnspan=2, pady=20)
	btn_clear = Button(mainFrame, text="Clear", font=('Helvetica', 24),bg="#1473E6",fg="white",bd=5,activebackground="green1",cursor="hand2", width=20, command=clearMethod)
	btn_clear.grid(row=13, column=2,padx=20, pady=20)

#====================================================Driver Method==========================================#

def mainMethod():
	ph_number = NUMBER.get()
	if ph_number == "":
		lbl_result1.config(text="Please complete the required field !", fg="blue")
	else :
		countryName(ph_number)
		carrierName(ph_number)

		
#===================================================Clear Method=============================================#
def clearMethod():
	NUMBER.set("")
	lbl_result2.config(text="")
	lbl_result3.config(text="")



#========================================================Country Name Method==================================#
def countryName(ph_number):
	ch_number = phonenumbers.parse(ph_number,"CH")
	stringCountry = "This number is located in " + geocoder.description_for_number(ch_number,"en")
	lbl_result2.config(text=stringCountry, fg="blue")



#========================================================Carrier Name Method===================================#
def carrierName(ph_number):
	service_number = phonenumbers.parse(ph_number,"RO")
	stringCarrier = "Service provider of this number " + carrier.name_for_number(service_number, "en")
	lbl_result3.config(text=stringCarrier, fg="blue")


#========================================================Entry Point===========================================#
mainForm()

# =======================================================INITIALIZATION========================================#
if __name__ == '__main__':
    root.mainloop()
