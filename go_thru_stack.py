import random
import pandas
from card_brain import CardBrain


class GoThruStack:

  def __init__(self, stack):
    self.stack = stack
    self.card_num = 0

    df = pandas.read_csv(f"data/{self.stack}.csv")
    shuffled_rank = df["Rank of Frequency"].tolist()
    random.shuffle(shuffled_rank) # shuffled_rank is a list of indice (aka rank of usage frequency from original list).

    # use new_dict to save words NOT remembered (without messing with the stack of cards during the loop).
    new_dict = {}
    for index, row in df.iterrows():
        new_dict[row["Rank of Frequency"]] = [row["Rank of Frequency"], row["Nepali"], row["English"]]

    card_brain = CardBrain(shuffled_rank, new_dict)

    # after the stack of cards have been reviewed (after creating/running card_brain)
    self.card_num = len(new_dict)
    new_df = pandas.DataFrame.from_dict(card_brain.new_dict, orient='index', columns=["Rank of Frequency", "Nepali", "English"])
    new_df.to_csv(f"data/{stack}.csv")
    q_df = pandas.DataFrame.from_dict(card_brain.words_in_question, orient='index', columns=["Rank of Frequency", "Nepali", "English"])
    q_df.to_csv("data/words_in_question.csv", mode="a")