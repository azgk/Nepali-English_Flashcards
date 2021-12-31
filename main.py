from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
row = 0

# Basic/static UI SETUP_________________________________________________
window = Tk()
window.title("Flash Cards")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR, highlightthickness=0)

canvas = Canvas(width=900, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")

# showing card using word list_________________________________________________
df = pandas.read_csv("data/french_words.csv")


def front_card():
    global row
    random_row = random.randint(1, len(df.index))

    row = random_row

    canvas.create_image(450, 280, image=card_front_img)
    canvas.create_text(435, 120, text="French", fill="Black", font=("Arial", 30, "italic"))
    canvas.create_text(440, 280, text=f"{df.iloc[random_row, 0]}", fill="Black", font=("Arial", 40, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)

    window.after(3000, back_card, random_row)


def back_card(random_row):
    canvas.create_image(450, 280, image=card_back_img)
    canvas.create_text(435, 120, text="English", fill="Black", font=("Arial", 30, "italic"))
    canvas.create_text(440, 280, text=f"{df.iloc[random_row, 1]}", fill="Black", font=("Arial", 40, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)


# Buttons_________________________________________________


def click_right():
    global row
    df.drop(index=row, inplace=True)
    df.to_csv("data/french_words.csv", index=False)
    front_card()


right_img = PhotoImage(file="images/right.png")
button_right = Button(image=right_img, highlightthickness=0, command=
                      click_right, bd=0)
button_right.grid(column=1, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_img, highlightthickness=0, command=
                      front_card, bd=0)
button_wrong.grid(column=0, row=1)

front_card()

window.mainloop()
