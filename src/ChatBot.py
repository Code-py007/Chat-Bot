from tkinter import *
import aiml
import os
from Bot_commands import *
import logging

# TODO: Start Logging
# Create and configure logger
logging.basicConfig (filename="newfile.log",
                     format='%(message)s',
                     filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel (logging.DEBUG)

window = Tk()
window.geometry("500x470")
window.configure(bg = "#ffffff")

entry_input = StringVar()

def send_input_msg():
    bot_commands = ['/delete', '/reload', '/learn', '/quit', '/help', '/math', '/meaning']
    delete = '/delete'
    reload = '/reload'
    learn = '/learn'
    quit_ = '/quit'
    help_ = '/help'
    math = '/math'
    meaning_ = '/meaning'
    x = ' '

    chat_area.config(state="normal")
    input_ = entry_input.get()
    chat_area.insert(INSERT,' You >> '+input_+'\n')
    
    entry1.delete(0,'end')

    if meaning_ in str(input_):
        # TODO split the input
        bot_input = input_.split(x)
        logger.debug(bot_input)
        logger.debug(input_)
        check_command = check_custom_commands(bot_input[0])
        
        # TODO check which command it is
        if check_custom_commands(bot_input[0]) == 'meaning':
            
            output = meaning(bot_input[1])
            chat_area.insert(INSERT,' Bot >> '+bot_input[1]+'\n'+output+"\n")

        else:
            chat_area.insert(Y,' Bot >> Not a custom command. Type "/help" for a list of possible commands\n')
            
    elif help_ in input_:
        # split the input
        bot_input = input_.split(x)
        logger.debug(bot_input)
        logger.debug(input_)
        check_command = check_custom_commands(bot_input[0])
        
        # check which command it is
        if check_custom_commands(bot_input[0]) == 'help':
            output = str(bot_commands)
            chat_area.insert(Y,' Bot >> '+output+"\n")
        else:
            chat_area.insert(Y,' Bot >> Not a custom command. Type "/help" for a list of possible commands\n')

        chat_area.config(state='disabled')
    
    elif delete in input_:

        # split the input
        bot_input = input_.split(x)
        logger.debug(bot_input)
        logger.debug(input_)
        check_command = check_custom_commands(bot_input[0])
        
        # check which command it is
        if check_custom_commands(bot_input[0]) == 'delete':

            chat_area.delete(1.0,END)
        else:
            chat_area.insert(Y,' Bot >> Not a custom command. Type "/help" for a list of possible commands\n')
            
        chat_area.config(state='disabled')
    
    elif learn in input_:

        # split the input
        bot_input = input_.split(x)
        logger.debug(bot_input)
        logger.debug(input_)
        check_command = check_custom_commands(bot_input[0])
        
        # check which command it is
        if check_custom_commands(bot_input[0]) == 'learn':
            output = learn_from_user()
            chat_area.insert(INSERT,' Bot >> Learned!\n')
        else:
            chat_area.insert(INSERT,' Bot >> Not a custom command. Type "/help" for a list of possible commands\n')
            
        chat_area.config(state='disabled')
    
    elif quit_ in input_:

        # split the input
        bot_input = input_.split(x)
        logger.debug(bot_input)
        logger.debug(input_)
        check_command = check_custom_commands(bot_input[0])
        
        # check which command it is
        if check_custom_commands(bot_input[0]) == 'quit':
            output = meaning()
            chat_area.insert(INSERT,' Bot >> '+output+'\n')
        else:
            chat_area.insert(INSERT,' Bot >> Not a custom command. Type "/help" for a list of possible commands\n')
            
        chat_area.config(state='disabled')
    
    elif math in input_:

        # split the input
        bot_input = input_.split(x)
        logger.debug(bot_input)
        logger.debug(input_)
        check_command = check_custom_commands(bot_input[0])
        
        # check which command it is
        if check_custom_commands(bot_input[0]) == 'math':
            output = do_math(bot_input[1],bot_input[2],bot_input[3])
            chat_area.insert(INSERT,' Bot >> '+str(output)+'\n')

        else:
            chat_area.insert(INSERT,' Bot >> Not a custom command. Type "/help" for a list of possible commands\n')
            
        chat_area.config(state='disabled')
    
    elif reload in input_:

        # split the input
        bot_input = input_.split(x)
        logger.debug(bot_input)
        logger.debug(input_)
        check_command = check_custom_commands(bot_input[0])
        
        # check which command it is
        if check_custom_commands(bot_input[0]) == 'reload':
            chat_area.insert(INSERT,' Bot >> Reloading...\n')
            os.remove('bot_brain.brn')
            kernel.bootstrap (learnFiles="std-startup.xml", commands="load aiml b")
            kernel.saveBrain ("bot_brain.brn")
            chat_area.insert(INSERT,' Bot >> Reloaded\n')

        else:
            chat_area.insert(INSERT,' Bot >> Not a custom command. Type "/help" for a list of possible commands\n')
            
        chat_area.config(state='disabled')

    else:
        chat_area.insert(INSERT,' Bot >> '+kernel.respond(input_)+'\n')
        
    chat_area.config(state='disabled')


kernel = aiml.Kernel()

canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 470,
    width = 500, 
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")

canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = "Ui files/img_textBox0.png")
entry0_bg = canvas.create_image(
    250.0, 223.5,
    image = entry0_img)



chat_area = Text(
    bd = 0,
    bg = "#d4d4d4",
    state='disabled',
    cursor='arrow',
    font = 'Poppins',
    highlightthickness = 0)

chat_area.place(
    x = 11, y = 61,
    width = 478,
    height = 323)

scroll  = Scrollbar(chat_area)
scroll.config(command= chat_area.yview)
scroll.place(relheight=1,relx = 0.98)

img0 = PhotoImage(file = "Ui files/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = send_input_msg,
    relief = "flat")

b0.place(
    x = 423, y = 416,
    width = 66,
    height = 48)

entry1_img = PhotoImage(file = "Ui files/img_textBox1.png")
entry1_bg = canvas.create_image(
    211.5, 440.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    font = 'Poppins',
    textvariable=entry_input,
    highlightthickness = 0)

entry1.place(
    x = 11, y = 416,
    width = 401,
    height = 46)

canvas.create_text(
    250.0, 31.5,
    text = "Chat Bot",
    fill = "#000000",
    font = ("Righteous", int(25.0)))


if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")


window.resizable(False, False)
window.mainloop()
