#Horoskop v1.0
#Aleksa Doderovic

import requests
import urllib
import re
from Tkinter import *
import tkMessageBox
import Tkinter
from bs4 import BeautifulSoup

top = Tk()
top.title("Daily Horoscope v1.0")
top.minsize(800, 600)
Lb = Listbox(top, selectmode="SINGLE")
Lb.config(height=12)
label = Label(top, text="Sign")
label.pack()
Lb.insert(1, "Aries")
Lb.insert(2, "Taurus")
Lb.insert(3, "Gemini")
Lb.insert(4, "Cancer")
Lb.insert(5, "Leo")
Lb.insert(6, "Virgo")
Lb.insert(7, "Libra")
Lb.insert(8, "Scorpio")
Lb.insert(9, "Saggitarius")
Lb.insert(10, "Capricorn")
Lb.insert(11, "Aquarius")
Lb.insert(12, "Pisces")
Lb.pack()
label2 = Label(top, text="Daily Horoscope")
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
    if(sign == "aries"):
        url = "http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=1"
    elif(sign == "taurus"):
        url = "http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=2"
    elif(sign == "gemini"):
        url = "http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=3"
    elif(sign == "cancer"):
        url = "http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=4"
    elif(sign == "leo"):
        url = "http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=5"
    elif(sign == "virgo"):
        url = "http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=6"
    elif(sign == "libra"):
        url = "http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=7"
    elif(sign == "scorpio"):
        url = "http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=8"
    elif(sign == "saggitarius"):
        url = "http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=9"
    elif(sign == "capricorn"):
        url = "http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=10"
    elif(sign == "aquarius"):
        url = "http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=11"
    elif(sign == "pisces"):
        url = "http://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign=12"
    if(url != ""):
        response = requests.get(url)
        html = response.content

        soup = BeautifulSoup(html, 'html.parser')
        soup = soup.find('div', {"class" : "block-horoscope-text"})
        
        result = soup.contents[0]
        result = result.lstrip()

    if result != "":
        text.delete(1.0, END)
        text.insert(1.0, result)
        text.pack()


top.mainloop()


