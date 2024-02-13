from tkinter import *
import pandas as pd
import random

current_card = {}
to_learn = {}

try: 
    data = pd.read_csv("flash_card_project/data/korean_words.csv")
except FileNotFoundError: 
    original_data = pd.read_csv("flash_card_project/data/korean_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else: 
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(5000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("flash_card_project/data/korean_words.csv", index=False)
    next_card()


window = Tk()
window.title("French Flashcard")
window.config(padx=50, pady=50)

flip_timer = window.after(5000, func=flip_card)

canvas = Canvas(width=800, height=600)
card_front_img = PhotoImage(file="flash_card_project/images/card_front.png")
card_back_img = PhotoImage(file="flash_card_project/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="flash_card_project/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="flash_card_project/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()

