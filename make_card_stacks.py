# Create card stacks (20 cards per stack).
import pandas

class CardStacks:

  def __init__(self, df):
    self.stack_i = 1
    self.new_dict = {}
    self.df = df
    self.make_stacks()

  def make_stacks(self):
    for index, row in self.df.iterrows():
      self.new_dict[row["Rank of Frequency"]] = [row["Rank of Frequency"], row["Nepali"], row["English"]]

      if (index + 1) % 20 == 0:
        new_df = pandas.DataFrame.from_dict(self.new_dict, orient='index', columns=["Rank of Frequency", "Nepali", "English"])
        new_df.to_csv(f"data/stack_{self.stack_i}.csv")
        self.new_dict = {}
        self.stack_i += 1
