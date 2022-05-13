from bs4 import BeautifulSoup
import requests


def LiveWeather(country, city):
    falseVar = 'Unknown address'

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
            return "Wrong Location provided"

        else:
            head_temp = file.find ('div', class_='h2')
            compliment = file.find ('div', class_='bk-focus__qlook')

            temp = head_temp.text
            temp_type = compliment.p.text
            clt = compliment.findAll ("p")[1]
            clt2 = clt.text
            clt3 = clt2.split ('°C')

            return 'Temprature: ' + temp

    elif (c1 == True) and (c2 == False):

        splitCountry = country.split (' ')

        url = 'https://www.timeanddate.com/weather/' + splitCountry[0] + '-' + splitCountry[1] + '/' + city
        page = requests.get (url)
        file = BeautifulSoup (page.content, 'lxml')

        if falseVar in str (file):
            return "Wrong Location provided"

        else:
            head_temp = file.find ('div', class_='h2')
            compliment = file.find ('div', class_='bk-focus__qlook')

            temp = head_temp.text
            temp_type = compliment.p.text
            clt = compliment.findAll ("p")[1]
            clt2 = clt.text
            clt3 = clt2.split ('°C')

            return 'Temprature: ' + temp

    elif (c1 == False) and (c2 == True):

        splitCity = city.split (' ')

        url = 'https://www.timeanddate.com/weather/' + country + '/' + splitCity[0] + '-' + splitCity[1]
        page = requests.get (url)
        file = BeautifulSoup (page.content, 'lxml')

        if falseVar in str (file):
            return "Wrong Location provided"

        else:
            head_temp = file.find ('div', class_='h2')
            compliment = file.find ('div', class_='bk-focus__qlook')

            temp = head_temp.text
            temp_type = compliment.p.text
            clt = compliment.findAll ("p")[1]
            clt2 = clt.text
            clt3 = clt2.split ('°C')

            return 'Temprature: ' + temp
    else:

        url = 'https://www.timeanddate.com/weather/' + country + '/' + city
        page = requests.get (url)
        file = BeautifulSoup (page.content, 'lxml')

        if falseVar in str (file):
            return "Wrong Location provided"

        else:
            head_temp = file.find ('div', class_='h2')
            compliment = file.find ('div', class_='bk-focus__qlook')

            temp = head_temp.text
            temp_type = compliment.p.text
            clt = compliment.findAll ("p")[1]
            clt2 = clt.text
            clt3 = clt2.split ('°C')

            return 'Temprature: ' + temp

