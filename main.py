# References: Inspired by Angela Yu's 100 Day Python Class (flash card project).
# 1000 most frequently used Nepali words from https://1000mostcommonwords.com/1000-most-common-nepali-words/?_ga=2.230450588.1648665285.1641086668-45386293.1641086668&_gl=1%2A1nafr1s%2A_ga%2ANDUzODYyOTMuMTY0MTA4NjY2OA..%2A_ga_8KVRFXKPM6%2AMTY0MTA4NjY2Ny4xLjAuMTY0MTA4NjY2Ny4w
# Only for initial launch or if needed to revert to original stacks, run make_card_stacks.py to create stacks of cards (20 cards per stack).
import pandas
from make_card_stacks import CardStacks
from go_thru_stack import GoThruStack

all_words_df = pandas.read_csv("data/original_100_common_words.csv")
card_stacks = CardStacks(all_words_df)
go_thru_stack = GoThruStack("stack_1")

# TODO: begin the game w this. allow user to choose 1--20 words, 21-40 words etc. Choose stack of cards. in each card, remember the progress.
# TODO: make a home button.
# TODO: change style of UI look. color, shape etc.
# TODO: add a word count. show it somewhere (total words, words remembered, words went through, words not remembered)
# TODO: what is a better way of doing click_right() other than breaking up the loop to several functions?

