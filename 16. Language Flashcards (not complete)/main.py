from tkinter import *
import pandas
import random

COUNT_TIMER = 2
BACKGROUND_COLOR = "#B1DDC6"
LEARNING_LANGUAGE = "Korean"
MAIN_LANGUAGE = "English"

list_to_learn = []

# -------------- read data --------------
data = pandas.read_csv("data/Korean to English Frequency Dictionary - Sheet1.csv")
data_dict = data.to_dict(orient="records")
total_cards = len(data_dict)


# -------------- storing mechanism --------------
def store():
    pass


# -------------- countdown mechanism --------------
def count_down(count, card):
    canvas.itemconfig(counter_label, text=f"{count}")

    if count >= 0:
        window.after(1000, count_down, count - 1, card)
    else:
        canvas.itemconfig(counter_label, text=f"Times up!")
        canvas.itemconfig(title_label, fill="white")
        canvas.itemconfig(word_label, fill="white")
        canvas.itemconfig(counter_label, fill="white")
        canvas.itemconfig(background_image, image=card_back_img)
        canvas.itemconfig(title_label, text=MAIN_LANGUAGE)
        canvas.itemconfig(word_label, text=card)
    return


# -------------- next card function --------------
def next_card():
    canvas.itemconfig(background_image, image=card_front_img)
    canvas.itemconfig(title_label, fill="black")
    canvas.itemconfig(word_label, fill="black")
    canvas.itemconfig(counter_label, fill="black")
    random_choice = random.randint(0, total_cards - 1)
    new_korean_card = data_dict[random_choice][LEARNING_LANGUAGE]
    new_english_card = data_dict[random_choice][MAIN_LANGUAGE]
    canvas.itemconfig(title_label, text=LEARNING_LANGUAGE)
    canvas.itemconfig(word_label, text=new_korean_card)
    count_down(count=COUNT_TIMER, card=new_english_card)


# -------------- creating UI --------------
window = Tk()
window.title("Korean Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# front and back card image
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
background_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)  # change this later

# canvas labels
title_label = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))  # to be a variable
word_label = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "normal"))  # to be a variable
counter_label = canvas.create_text(400, 400, text="", font=("Ariel", 20, "normal"))  # to be a variable

# buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

window.mainloop()
