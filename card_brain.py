from tkinter import *
from tkinter import messagebox
from tkinter import font
import random
import pandas

BACKGROUND_COLOR = "#BAD7E9"


class CardBrain:

  def __init__(self):
    self.flip_timer = lambda x: 0  # A trick to flip the cards.
    self.i = 0  # Use this i to loop through the shuffled_rank while running different button commands.
    self.stack = None

    # Basic/static UI SETUP_________________________________________________________________
    self.window = Tk()
    self.window.title("Flash Cards")
    self.window.config(padx=30, pady=30, bg=BACKGROUND_COLOR, highlightthickness=0)

    self.canvas = Canvas(width=900, height=560, bg=BACKGROUND_COLOR, highlightthickness=0)
    self.canvas.grid(column=1, row=1, columnspan=4, rowspan=8)

    self.card_front_img = PhotoImage(file="images/card_front.png")
    self.card_back_img = PhotoImage(file="images/card_back.png")
    self.canvas_image = self.canvas.create_image(450, 280, image=self.card_front_img)
    self.card_title = self.canvas.create_text(435, 120, text="", fill="Black", font=("Arial", 30, "italic"))
    self.word_text = self.canvas.create_text(440, 280, text="", fill="Black", font=("Arial", 60, "normal"))
    self.progress = self.canvas.create_text(200, 7, text="", fill="Black", font=("Arial", 20, "normal"))
    self.button_style = font.Font(family='Helvetica', size=18, weight='bold')

    self.btn_stack_1 = Button(text=f"Cards 01 - 20", command=lambda: self.front_card("stack_1", True),
                              highlightbackground=BACKGROUND_COLOR, font=self.button_style, borderwidth=0)
    self.btn_stack_2 = Button(text=f"Cards 21 - 40", command=lambda: self.front_card("stack_2", True),
                              highlightbackground=BACKGROUND_COLOR, font=self.button_style, borderwidth=0)
    self.btn_stack_3 = Button(text=f"Cards 41 - 60", command=lambda: self.front_card("stack_3", True),
                              highlightbackground=BACKGROUND_COLOR, font=self.button_style, borderwidth=0)
    self.btn_stack_4 = Button(text=f"Cards 61 - 80", command=lambda: self.front_card("stack_4", True),
                              highlightbackground=BACKGROUND_COLOR, font=self.button_style, borderwidth=0)
    self.btn_stack_5 = Button(text=f"Cards 81 - 100", command=lambda: self.front_card("stack_5", True),
                              highlightbackground=BACKGROUND_COLOR, font=self.button_style, borderwidth=0)

    home_img = PhotoImage(file="images/home.png")
    home_button = Button(image=home_img, command=self.show_home_page, highlightthickness=0, bd=0)
    home_button.grid(column=0, row=0, pady=20)
    info_img = PhotoImage(file="images/info.png")
    info_button = Button(image=info_img, command=self.click_info, highlightthickness=0, bd=0)
    info_button.grid(column=5, row=0, pady=20)
    self.button_remembered = Button(text="I know this!", command=self.click_remembered, bd=0, highlightthickness=0,
                          highlightbackground=BACKGROUND_COLOR, font=self.button_style, padx=20, pady=5, borderwidth=0)
    self.button_need_review = Button(text="Need to review", command=self.click_need_review, bd=0, highlightthickness=0,
                          highlightbackground=BACKGROUND_COLOR, font=self.button_style, padx=10, pady=5, borderwidth=0)

    self.show_home_page()
    self.window.mainloop()

  # home page
  def show_home_page(self):
    # Hide widges from other pages
    self.canvas.itemconfig(self.card_title, state='hidden')
    self.canvas.itemconfig(self.word_text, state='hidden')
    self.canvas.itemconfig(self.progress, state='hidden')
    self.button_need_review.grid_forget()
    self.button_remembered.grid_forget()

    self.i = 0
    self.window.after_cancel(self.flip_timer)
    self.canvas.itemconfig(self.canvas_image, image=self.card_front_img)
    self.welcome_text = self.canvas.create_text(440, 180, text="Welcome! Please choose a stack of flash cards.", fill=
                                                "Black", font=("Arial", 30, "normal"))
    self.btn_stack_1.grid(column=1, row=5)
    self.btn_stack_2.grid(column=2, row=5)
    self.btn_stack_3.grid(column=3, row=5)
    self.btn_stack_4.grid(column=1, row=6)
    self.btn_stack_5.grid(column=2, row=6)

  def hide_home_page(self):
    self.canvas.itemconfig(self.welcome_text, state="hidden")
    self.btn_stack_1.grid_forget()
    self.btn_stack_2.grid_forget()
    self.btn_stack_3.grid_forget()
    self.btn_stack_4.grid_forget()
    self.btn_stack_5.grid_forget()

    # Show widgets for other pages
    self.canvas.itemconfig(self.card_title, state='normal')
    self.canvas.itemconfig(self.word_text, state='normal')
    self.canvas.itemconfig(self.progress, state='normal')
    self.button_need_review.grid(column=1, row=9)
    self.button_remembered.grid(column=4, row=9)

  # showing cards ___________________________________________________________________
  def front_card(self, stack, first_run=False):
    self.hide_home_page()

    self.stack = stack
    df = pandas.read_csv(f"data/{stack}.csv")

    if first_run:
      # shuffled_rank is a list of indice (aka rank of usage frequency from original list).
      self.shuffled_rank = df["Rank of Frequency"].tolist()
      random.shuffle(self.shuffled_rank)
      # use new_dict to save words NOT remembered (without messing with the stack of cards during the loop).
      self.new_dict = {}
      for index, row in df.iterrows():
          self.new_dict[row["Rank of Frequency"]] = [row["Rank of Frequency"], row["Nepali"], row["English"]]

    rank = self.shuffled_rank[self.i]
    self.window.after_cancel(self.flip_timer)
    self.canvas.itemconfig(self.canvas_image, image=self.card_front_img)
    self.canvas.itemconfig(self.card_title, text="Nepali", fill="Black")
    self.canvas.itemconfig(self.word_text, text=self.new_dict[rank][1], fill="Black", font=("Arial", 60, "normal"))
    self.canvas.itemconfig(self.progress, text=f"{20 - len(self.new_dict)} / 20 words remembered")
    self.button_need_review.grid(column=1, row=9)
    self.button_remembered.grid(column=4, row=9)
    self.flip_timer = self.window.after(4000, self.back_card)

  def back_card(self):
    self.hide_home_page()
    rank = self.shuffled_rank[self.i]
    self.canvas.itemconfig(self.canvas_image, image=self.card_back_img)
    self.canvas.itemconfig(self.card_title, text="English", fill="White")
    self.canvas.itemconfig(self.word_text, text=self.new_dict[rank][2], fill="White", font=("Arial", 60, "normal"))

  def end_of_cards(self):
    self.canvas.itemconfig(self.card_title, text="")
    self.canvas.itemconfig(self.canvas_image, image=self.card_front_img)
    self.canvas.itemconfig(self.word_text, text="Good job! You have gone through this stack.", font=("Arial", 24, "normal"))
    new_df = pandas.DataFrame.from_dict(self.new_dict, orient='index',
                                        columns=["Rank of Frequency", "Nepali", "English"])
    new_df.to_csv(f"data/{self.stack}.csv")

  def click_remembered(self):
    try:
      rank = self.shuffled_rank[self.i]
    except IndexError:
      return  # Disable the button when all cards are reviewed.
    self.new_dict.pop(rank)
    self.i += 1
    if self.i == len(self.shuffled_rank):
      self.end_of_cards()
    else:
      self.front_card(self.stack)

  def click_need_review(self):
    self.i += 1
    if self.i == len(self.shuffled_rank):
      self.end_of_cards()
    elif self.i > len(self.shuffled_rank):
      return  # Disable the button when all cards are reviewed.
    else:
      self.front_card(self.stack)

  def click_info(self):
      messagebox.showinfo(
        message="You have 4 seconds to look at the Nepali word then the English translation will be displayed.\n Click 'Need to review' if you don't remember the word. Click 'I know this!' if you have memorized the "
                "word; it will be removed from the stack of cards. Note that if you click 'home' before you go through a stack of cards your "
                "progress will not be saved.")

