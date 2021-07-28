from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("500x470")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 470,
    width = 500, 
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")

canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"Ui files/generated_code/img_textBox0.png")
entry0_bg = canvas.create_image(
    250.0, 223.5,
    image = entry0_img)

entry0 = Text(
    bd = 0,
    bg = "#d4d4d4",
    highlightthickness = 0)

entry0.place(
    x = 11, y = 61,
    width = 478,
    height = 323)

img0 = PhotoImage(file = f"Ui files/generated_code/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 423, y = 416,
    width = 66,
    height = 48)

entry1_img = PhotoImage(file = f"Ui files/generated_code/img_textBox1.png")
entry1_bg = canvas.create_image(
    211.5, 440.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
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

window.resizable(False, False)
window.mainloop()
