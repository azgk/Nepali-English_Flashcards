# References:
#  1.Inspired by Angela Yu's 100 Day Python Class (flash card project).
#  2.1000 most frequently used Nepali words from
#    https://1000mostcommonwords.com/1000-most-common-nepali-words/?_ga=2.230450588.1648665285.1641086668-45386293.1641086668&_gl=1%2A1nafr1s%2A_ga%2ANDUzODYyOTMuMTY0MTA4NjY2OA..%2A_ga_8KVRFXKPM6%2AMTY0MTA4NjY2Ny4xLjAuMTY0MTA4NjY2Ny4w

import pandas
from make_card_stacks import CardStacks
from card_brain import CardBrain

all_words_df = pandas.read_csv("data/original_100_common_words.csv")
# Line 12 only need to be run once unless new words are added to the original list or if you want to reset card stacks.
# card_stacks = CardStacks(all_words_df)
card_brain = CardBrain()


