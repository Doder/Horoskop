#Horoskop v1.0
#Aleksa Doderovic

import requests
import urllib
import re
from Tkinter import *
import tkMessageBox
import Tkinter
from BeautifulSoup import BeautifulSoup

top = Tk()
top.title("Dnevni Horoskop v1.0")
top.minsize(300, 300)

Lb = Listbox(top, selectmode="SINGLE")
label = Label(top, text="Znak")
label.pack()
Lb.insert(1, "Jarac")
Lb.insert(2, "Ovan")
Lb.insert(3, "Ribe")
Lb.insert(4, "Strelac")
Lb.insert(5, "Skorpija")
Lb.insert(6, "Vaga")
Lb.insert(7, "Devica")
Lb.insert(8, "Vodolija")
Lb.insert(9, "Bik")
Lb.insert(10, "Lav")
Lb.insert(11, "Rak")
Lb.insert(12, "Blizanci")
Lb.pack()
label2 = Label(top, text="Dnevni horoskop")
label2.pack()

text = Text(top)
result = ""
url = ""
sign = ""

def onselect(evt):
    sign = Lb.get(Lb.curselection()[0])
    sign = sign.lower()
    find(sign)
Lb.bind('<<ListboxSelect>>', onselect)
def find(sign):
    if(sign == "jarac"):
        url = "http://www.horoskopius.com/dnevni-horoskop/jarac/"
    elif(sign == "ovan"):
        url = "http://www.horoskopius.com/dnevni-horoskop/ovan/"
    elif(sign == "lav"):
        url = "http://www.horoskopius.com/dnevni-horoskop/lav/"
    elif(sign == "bik"):
        url = "http://www.horoskopius.com/dnevni-horoskop/bik/"
    elif(sign == "strelac"):
        url = "http://www.horoskopius.com/dnevni-horoskop/strelac/"
    elif(sign == "devica"):
        url = "http://www.horoskopius.com/dnevni-horoskop/devica/"
    elif(sign == "vodolija"):
        url = "http://www.horoskopius.com/dnevni-horoskop/vodolija/"
    elif(sign == "vaga"):
        url = "http://www.horoskopius.com/dnevni-horoskop/vaga/"
    elif(sign == "blizanci"):
        url = "http://www.horoskopius.com/dnevni-horoskop/blizanci/"
    elif(sign == "rak"):
        url = "http://www.horoskopius.com/dnevni-horoskop/rak/"
    elif(sign == "skorpija"):
        url = "http://www.horoskopius.com/dnevni-horoskop/skorpija/"
    elif(sign == "ribe"):
        url = "http://www.horoskopius.com/dnevni-horoskop/ribe/"
    if(url != ""):
        response = requests.get(url)
        html = response.content

        soup = BeautifulSoup(html)
        soup = soup.find('div', {"class" : "horoscope-txt row"})
        
        result = soup.contents[0]

    if result != "":
        text.delete(1.0, END)
        text.insert(1.0, result)
        text.pack()


top.mainloop()


