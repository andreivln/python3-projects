from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}  
dict_words = {}  


# ---------------------------------------------------------Read data---------------------------------------------------#
try:
    data = pandas.read_csv("./data/word_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    dict_words = original_data.to_dict(orient="records")
else:
    dict_words = data.to_dict(orient="records") 

# ---------------------------------------------------------Next card---------------------------------------------------#
def next_word():
    global current_card, flip_timer
    screen.after_cancel(flip_timer) 

    current_card = random.choice(dict_words)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(background_card, image=image_card_front)
    flip_timer = screen.after(5000, flip_card)

# ---------------------------------------------------------Flip card---------------------------------------------------#
def flip_card():

    canvas.itemconfig(card_title, text="English", fill="#FFFFFF")
    canvas.itemconfig(card_word, text=current_card["English"], fill="#FFFFFF")
    canvas.itemconfig(background_card, image=image_card_back)

# ---------------------------------------------------------Next card---------------------------------------------------#
def is_known():
    dict_words.remove(current_card)

    data = pandas.DataFrame(dict_words)
    data.to_csv("data/word_to_learn.csv", index=False)
    next_word()


# ---------------------------------------------------------UI Set UP---------------------------------------------------#
screen = Tk()
screen.title("Capstone Project")
screen.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


image_wrong = PhotoImage(file="./images/wrong.png")
image_card_back = PhotoImage(file="./images/card_back.png")
image_card_front = PhotoImage(file="./images/card_front.png")
image_right = PhotoImage(file="./images/right.png")

# Canvas
canvas = Canvas(width=800, height=526)
background_card = canvas.create_image(400, 263, image=image_card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons

button_right = Button(image=image_right, highlightthickness=0, command=is_known)
button_right.grid(column=1, row=1)

button_wrong = Button(image=image_wrong, highlightthickness=0, command=next_word)
button_wrong.grid(column=0, row=1)


flip_timer = screen.after(5000, flip_card)
next_word()

screen.mainloop()
