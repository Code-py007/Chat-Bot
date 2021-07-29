from tkinter import *
from bs4 import BeautifulSoup
import requests
from PIL import Image, ImageTk


def LiveWeather():

    root = Tk ( )
    root.geometry ('500x400')
    root.config (bg="white")
    root.title ("Live Weather")

    falseVar = 'Unknown address'


    def get_temp():
        country = a.get ( )
        city = b.get ( )

        c1 = " " in country
        c2 = " " in city

        if (c1 == True) and (c2 == True):

            splitCountry = country.split (' ')
            splitCity = city.split (' ')

            url = 'https://www.timeanddate.com/weather/' + splitCountry[0] + '-' + splitCountry[1] + '/' + splitCity[
                0] + '-' + splitCountry[1]
            page = requests.get (url)
            file = BeautifulSoup (page.content, 'lxml')

            if falseVar in str (file):
                info.delete ('1.0', END)
                info.insert (1.0, "Wrong Location provided")

            else:
                head_temp = file.find ('div', class_='h2')
                compliment = file.find ('div', class_='bk-focus__qlook')

                temp = head_temp.text
                temp_type = compliment.p.text
                clt = compliment.findAll ("p")[1]
                clt2 = clt.text
                clt3 = clt2.split ('°C')

                info.delete ('1.0', END)

                info.insert (1.0, 'Temprature:' + temp + '\n')
                info.insert (2.0, temp_type + '\n')
                info.insert (3.0, clt3[0] + '°C' + '\n')
                info.insert (4.0, clt3[1] + '°C' + '\n')
                info.insert (5.0, clt3[2] + '\n')

        elif (c1 == True) and (c2 == False):

            splitCountry = country.split (' ')

            url = 'https://www.timeanddate.com/weather/' + splitCountry[0] + '-' + splitCountry[1] + '/' + city
            page = requests.get (url)
            file = BeautifulSoup (page.content, 'lxml')

            if falseVar in str (file):
                info.delete ('1.0', END)
                info.insert (1.0, "Wrong Location provided")

            else:
                head_temp = file.find ('div', class_='h2')
                compliment = file.find ('div', class_='bk-focus__qlook')

                temp = head_temp.text
                temp_type = compliment.p.text
                clt = compliment.findAll ("p")[1]
                clt2 = clt.text
                clt3 = clt2.split ('°C')

                info.delete ('1.0', END)

                info.insert (1.0, 'Temprature:' + temp + '\n')
                info.insert (2.0, temp_type + '\n')
                info.insert (3.0, clt3[0] + '°C' + '\n')
                info.insert (4.0, clt3[1] + '°C' + '\n')
                info.insert (5.0, clt3[2] + '\n')


        elif (c1 == False) and (c2 == True):

            splitCity = city.split (' ')

            url = 'https://www.timeanddate.com/weather/' + country + '/' + splitCity[0] + '-' + splitCity[1]
            page = requests.get (url)
            file = BeautifulSoup (page.content, 'lxml')

            if falseVar in str (file):
                info.delete ('1.0', END)
                info.insert (1.0, "Wrong Location provided")

            else:
                head_temp = file.find ('div', class_='h2')
                compliment = file.find ('div', class_='bk-focus__qlook')

                temp = head_temp.text
                temp_type = compliment.p.text
                clt = compliment.findAll ("p")[1]
                clt2 = clt.text
                clt3 = clt2.split ('°C')

                info.delete ('1.0', END)

                info.insert (1.0, 'Temprature:' + temp + '\n')
                info.insert (2.0, temp_type + '\n')
                info.insert (3.0, clt3[0] + '°C' + '\n')
                info.insert (4.0, clt3[1] + '°C' + '\n')
                info.insert (5.0, clt3[2] + '\n')

        else:

            url = 'https://www.timeanddate.com/weather/' + country + '/' + city
            page = requests.get (url)
            file = BeautifulSoup (page.content, 'lxml')

            if falseVar in str (file):
                info.delete ('1.0', END)
                info.insert (1.0, "Wrong Location provided")

            else:
                head_temp = file.find ('div', class_='h2')
                compliment = file.find ('div', class_='bk-focus__qlook')

                temp = head_temp.text
                temp_type = compliment.p.text
                clt = compliment.findAll ("p")[1]
                clt2 = clt.text
                clt3 = clt2.split ('°C')

                info.delete ('1.0', END)

                info.insert (1.0, 'Temprature:' + temp + '\n')
                info.insert (2.0, temp_type + '\n')
                info.insert (3.0, clt3[0] + '°C' + '\n')
                info.insert (4.0, clt3[1] + '°C' + '\n')
                info.insert (5.0, clt3[2] + '\n')


    image1 = Image.open ("Ui files/button.png")
    test = ImageTk.PhotoImage (image1)

    image3 = Image.open ("Ui files/Frame 2.png")
    test2 = ImageTk.PhotoImage (image3)

    image4 = Image.open ("Ui files/button2.png")
    test3 = ImageTk.PhotoImage (image4)

    ############################################
    image = Label (root, image=test, borderwidth='0').place (x="72", y="75")

    a = Entry (root, textvariable="country", borderwidth="0", bg="#D2D2D2")
    a.place (x="80", y="77", width="120")

    Label (root, text="Country:", bg="white").place (x="80", y="50")
    ##########################################################
    image2 = Label (root, image=test, borderwidth='0').place (x="230", y="77")

    b = Entry (root, textvariable="city", borderwidth=0, bg="#D2D2D2")
    b.place (x="240", y="79", width="120")

    Label (root, text="City:", bg="white").place (x="250", y="50")
    #############################################

    image3 = Label (root, image=test2, borderwidth='0').place (x="-60", y="100")

    info = Text (root, bg="white", borderwidth='0')
    info.config (font="Poppins")
    info.place (x="60", y="190", width="380", height="180")

    submit = Button (root, image=test3, borderwidth="0", command=get_temp).place (x="380", y="60", width="68", height='40')

    mainloop ( )

LiveWeather()
