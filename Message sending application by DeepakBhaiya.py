import requests
import json

from tkinter import *
from tkinter.messagebox import showerror,showinfo


def send_sms(number , message):
	url:'https://www.fast2sms.com/dev/bulk'
	params = {
	'authorization':'PASTE_here_your_API_KEY',
	'sender_id':'FASTSMS',
	'message':message,
	'language':'english',
	'route':'p',
	'numbers':number
	}

	response = requests.get(url , params = params)
	dic = response.json()
	print(dic)
	return dic.get('return') #if message will be send then it will be return TRUE, Else return FALSE
	
	
#send_sms("8693878309","Hello bhaiya , write your message here")



#Button function
def btn_click():
	num = text_number.get()
	msg = txt_message.get("1.0",END)
	r = send_sms(num,msg)
	if r==True:
		showinfo("Done!","Send Successfully!")
	else:
		showerror("Error!","Something went wrong!\n Please try again..!")
	


#Creating GUI
root = Tk() #Object of the Tkinter class
root.title("Message Sender") #set the title
root.geometry("400x550") #Set size
font=("Helvetica",22,"bold") #Font_family_name , Font_size , Font_Type

text_number = Entry(root , font=font)
text_number.pack(fill=X,pady=20)


txt_message = Text(root)
txt_message.pack(fill=X)


btn = Button(root , text="Send SMS", command=btn_click)
btn.pack()



root.mainloop()