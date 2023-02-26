# References: Inspired by Angela Yu's 100 Day Python Class (flash card project).
# References: 1000 most frequently used Nepali words from https://1000mostcommonwords.com/1000-most-common-nepali-words/?_ga=2.230450588.1648665285.1641086668-45386293.1641086668&_gl=1%2A1nafr1s%2A_ga%2ANDUzODYyOTMuMTY0MTA4NjY2OA..%2A_ga_8KVRFXKPM6%2AMTY0MTA4NjY2Ny4xLjAuMTY0MTA4NjY2Ny4w
import pandas
from make_card_stacks import CardStacks
from go_thru_stack import GoThruStack

all_words_df = pandas.read_csv("data/original_100_common_words.csv")
# card_stacks = CardStacks(all_words_df) # This line only need to be run once unless new words are added to the original list.
go_thru_stack = GoThruStack("stack_1")

# TODO: add a word count. show it somewhere (total words, words remembered, words went through, words not remembered). save this in a separate cvs file (save review progress)
# TODO: what is a better way of doing click_right() other than breaking up the loop to several functions?
# TODO: update readme to add features.

