import data_df
import pandas as pd
df = preprocessor.preprocess(df)
new_df = pd.DataFrame(df, columns=["date", "user", "message"])
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sentiments = SentimentIntensityAnalyzer()
new_df["sentiment"] = new_df["message"].apply(lambda message: sentiments.polarity_scores(message))
new_df["positive"] = new_df["sentiment"].apply(lambda score: score["pos"])
new_df["negative"] = new_df["sentiment"].apply(lambda score: score["neg"])
new_df["neutral"] = new_df["sentiment"].apply(lambda score: score["neu"])
new_df = new_df.drop("sentiment", axis=1)
new_df.head(10)