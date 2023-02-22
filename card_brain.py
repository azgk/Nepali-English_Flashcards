from tkinter import *
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"


class CardBrain:

  def __init__(self, shuffled_rank, new_dict):
    #TODO: flag--move the arg to a function. this class would not need initial arg.
    #TODO: change names. card_brain to ui. go_thru_stack to card_brain.
    #TODO: add UI for welcome msg and selection of stacks (list? or something SIMPLE)
    #TODO: pass user choice (stack) to go_thru_stack (change names) to generate shuffle and something.
    #TODO: in go_thru, also take out initialization arg and then pass the obj to ui. (see quizzler brain)


    # input
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
    self.card_front_img = PhotoImage(file="images/card_front.png")
    self.card_back_img = PhotoImage(file="images/card_back.png")
    self.canvas_image = self.canvas.create_image(450, 280, image=self.card_front_img)
    self.card_title = self.canvas.create_text(435, 120, text="", fill="Black", font=("Arial", 30, "italic"))
    self.word_text = self.canvas.create_text(440, 280, text="", fill="Black", font=("Arial", 60, "normal"))
    self.canvas.grid(column=0, row=0, columnspan=3)

    wrong_img = PhotoImage(file="images/wrong.png")
    button_wrong = Button(image=wrong_img, highlightthickness=0, command=self.click_wrong, bd=0)
    button_wrong.grid(column=0, row=1)
    question_img = PhotoImage(file="images/question.png")
    button_question = Button(image=question_img, command=self.click_question, highlightthickness=0, bd=0)
    button_question.grid(column=1, row=1)
    right_img = PhotoImage(file="images/right.png")
    button_right = Button(image=right_img, highlightthickness=0, command=self.click_right, bd=0)
    button_right.grid(column=2, row=1)
    info_img = PhotoImage(file="images/info.png")
    info_button = Button(image=info_img, command=self.click_info, highlightthickness=0, bd=0)
    info_button.grid(column=1, row=2, pady=20)

    self.front_card()
    self.window.mainloop()

  # showing cards ___________________________________________________________________
  def front_card(self):
    rank = self.shuffled_rank[self.i]
    self.window.after_cancel(self.flip_timer)
    self.canvas.itemconfig(self.canvas_image, image=self.card_front_img)
    self.canvas.itemconfig(self.card_title, text="Nepali", fill="Black")
    self.canvas.itemconfig(self.word_text, text=self.new_dict[rank][1], fill="Black")
    self.flip_timer = self.window.after(4000, self.back_card)

  def back_card(self):
    rank = self.shuffled_rank[self.i]
    self.canvas.itemconfig(self.canvas_image, image=self.card_back_img)
    self.canvas.itemconfig(self.card_title, text="English", fill="White")
    self.canvas.itemconfig(self.word_text, text=self.new_dict[rank][2], fill="White")

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

  def click_question(self):
    rank = self.shuffled_rank[self.i]
    new_word = self.new_dict[rank]
    self.words_in_question[rank] = [new_word[0], new_word[1], new_word[2]]
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
        message="You have 4 seconds to look at the Nepali word then the English translation will be displayed.\n Click 'cross' if you don't remember the word. Click 'check' if you memorized the "
                "word; it will be removed from the 'stack of cards'. Click 'question' if you want to save"
                " the word to look up later.")

