import pandas
from sklearn.model_selection import train_test_split

df = pandas.read_csv("games.csv")

df = df.drop_duplicates()

train_df, test_df = train_test_split(
    df, 
    test_size=0.2, 
    random_state=4
    )

train_df.to_csv(f"train_games.csv", index=False)
test_df.to_csv(f"test_games.csv", index=False)

