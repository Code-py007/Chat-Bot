from bs4 import BeautifulSoup
import requests
from tkinter import *


def check_custom_commands(command):
    
    bot_commands = ['/delete','/reload','/learn','/quit','/help','/math','/meaning','/weather']
    if command == bot_commands[0]:
        return 'delete'

    elif command == bot_commands[2]:
        return 'learn'
    
    elif command == bot_commands[1]:
        return 'reload'
    
    elif command == bot_commands[3]:
        quit()
    
    elif command == bot_commands[4]:
        return 'help'
    
    elif command == bot_commands[5]:
        return 'math'
    
    elif command == bot_commands[6]:
        return 'meaning'
    elif command == bot_commands[7]:
        return 'weather'
    else:
        return 'Nothing'
    
def meaning(word):

    url = 'https://www.dictionary.com/browse/'+word
    soup = requests.get(url)
    file = BeautifulSoup(soup.content,'html5lib')
    mid_section = file.find('section',class_='css-pnw38j e1hk9ate4')
    meaning = mid_section.text
    return meaning

def learn_from_user():
    learnWindow = Toplevel ( )
    learnWindow.geometry ('300x150')
    learnWindow.title ('Teach Me!')
    question = StringVar ( )
    answer = StringVar ( )
    ###################################

    def learned():

        with open ('aiml_files/botLearn.xml', 'r') as f2:
            data = f2.readlines ( )

        with open ('aiml_files/botLearn.xml', 'w') as f:
            for line in data:
                if line.strip ("\n") != "</aiml>":
                    f.write (line)
            f.write (
                '\n<category>\n<pattern>' + question.get() + '</pattern>\n<template>' + answer.get() + '</template>\n</category>\n')
            f.write ('</aiml>')
        learnWindow.destroy()

    ###############################

    Label (learnWindow, text="Question:").place (x="30", y="40")
    Label (learnWindow, text="Answer:").place (x="30", y="70")

    question_ = Entry (learnWindow, textvariable=question)
    question_.place (x="110", y="40")

    answer_ = Entry (learnWindow, textvariable=answer)
    answer_.place (x="110", y="70")

    loginB = Button (learnWindow, text="Learn", command=learned)
    loginB.place (x="100", y="100")

    return True

def do_math(eq1,sign,eq2):
    if sign == '+':
        if str(eq1).isnumeric() and str(eq2).isnumeric():
            return float(eq1) + float(eq2)

    elif sign == '-':
        if str(eq1).isnumeric() and str(eq2).isnumeric():
            return float(eq1) - float(eq2)

    elif sign == '*':
        if str(eq1).isnumeric() and str(eq2).isnumeric():
            return float(eq1) * float(eq2)

    elif sign == '/':
        if str(eq1).isnumeric() and str(eq2).isnumeric():
            return float(eq1) / float(eq2)

    else:
        return 'syntax is incorrect'






