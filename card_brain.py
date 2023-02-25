from tkinter import *
from tkinter import messagebox
from tkinter import font

BACKGROUND_COLOR = "#BAD7E9"


class CardBrain:

  def __init__(self, shuffled_rank, new_dict):
    #TODO: add UI for welcome msg and selection of stacks (list? or something SIMPLE)
    #TODO: pass user choice (stack) to go_thru_stack (change names) to generate shuffle and something.
    self.shuffled_rank = shuffled_rank
    self.new_dict = new_dict
    # output
    self.words_in_question = {}
    self.new_dict = new_dict
    # a trick to flip the cards.
    self.flip_timer = lambda x: 0
    # use this i to loop through the shuffled_rank while running different button commands.
    self.i = 0

    # Basic/static UI SETUP_________________________________________________________________
    self.window = Tk()
    self.window.title("Flash Cards")
    self.window.config(padx=30, pady=30, bg=BACKGROUND_COLOR, highlightthickness=0)

    self.canvas = Canvas(width=900, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
    self.canvas.grid(column=0, row=1, columnspan=3)

    self.card_front_img = PhotoImage(file="images/card_front.png")
    self.card_back_img = PhotoImage(file="images/card_back.png")
    self.canvas_image = self.canvas.create_image(450, 280, image=self.card_front_img)
    self.card_title = self.canvas.create_text(435, 120, text="", fill="Black", font=("Arial", 30, "italic"))
    self.word_text = self.canvas.create_text(440, 280, text="", fill="Black", font=("Arial", 60, "normal"))

    self.button_style = font.Font(family='Helvetica', size=20, weight='bold')

    info_img = PhotoImage(file="images/info.png")
    info_button = Button(image=info_img, command=self.click_info, highlightthickness=0, bd=0)
    info_button.grid(column=3, row=0, pady=20)

    self.home_page()
    self.window.mainloop()

  # home page
  def home_page(self):
    self.btn_stack_1 = Button(text="Words 1 - 20", command=self.front_card, bd=0, highlightthickness=0,
                          highlightbackground=BACKGROUND_COLOR, font=self.button_style, padx=10, pady=5, borderwidth=0)
    # TODO: FLAG start here. refactor this to make a function to make 5 buttons.
    #  self.btn_stack_1.grid(column=0, row=1)

  def hide_stack_btn(self):
    self.btn_stack_1.grid_forget()

  # showing cards ___________________________________________________________________
  def front_card(self):
    rank = self.shuffled_rank[self.i]
    self.window.after_cancel(self.flip_timer)
    self.canvas.itemconfig(self.canvas_image, image=self.card_front_img)
    self.canvas.itemconfig(self.card_title, text="Nepali", fill="Black")
    self.canvas.itemconfig(self.word_text, text=self.new_dict[rank][1], fill="Black")
    self.hide_stack_btn()
    self.flip_timer = self.window.after(4000, self.back_card)
    button_wrong = Button(text="Need to review", command=self.click_right, bd=0, highlightthickness=0,
                          highlightbackground=BACKGROUND_COLOR, font=self.button_style, padx=10, pady=5, borderwidth=0)
    button_wrong.grid(column=0, row=3)
    button_right = Button(text="I know this!", command=self.click_right, bd=0, highlightthickness=0,
                          highlightbackground=BACKGROUND_COLOR, font=self.button_style, padx=20, pady=5, borderwidth=0)
    button_right.grid(column=2, row=3)

  def back_card(self):
    rank = self.shuffled_rank[self.i]
    self.canvas.itemconfig(self.canvas_image, image=self.card_back_img)
    self.canvas.itemconfig(self.card_title, text="English", fill="White")
    self.canvas.itemconfig(self.word_text, text=self.new_dict[rank][2], fill="White")
    self.hide_stack_btn()

  # Buttons_____________________________________________________________________________
  def end_of_cards(self):
    self.canvas.itemconfig(self.card_title, text="")
    self.canvas.itemconfig(self.word_text, text="Good job! You have gone through all the cards", font=("Arial", 24, "normal"))

  def click_right(self):
    rank = self.shuffled_rank[self.i]
    self.new_dict.pop(rank)
    self.i += 1
    if self.i == len(self.shuffled_rank):
      self.end_of_cards()
    else:
      self.front_card()

  def click_wrong(self):
    self.i += 1
    if self.i == len(self.shuffled_rank):
      self.end_of_cards()
    else:
      self.front_card()

  def click_info(self):
      messagebox.showinfo(
        message="You have 4 seconds to look at the Nepali word then the English translation will be displayed.\n Click 'Need to review' if you don't remember the word. Click 'I know this!' if you have memorized the "
                "word; it will be removed from the 'stack of cards'.")

