import pandas as pd
import numpy as np

df=pd.read_csv("002_dataset_transformation/day02_usage.csv")

chat=df["Chat"].to_numpy()
study=df["Study"].to_numpy()
video=df["Video"].to_numpy()
games=df["Games"].to_numpy()


print("Length of chat : ",len(chat))
print("Length of study : ",len(study))
print("Length of video : ",len(video))
print("Length of games : ",len(games))

print("Chat total time : ",chat.sum())
print("Study total time : ",study.sum())
print("Video total time : ",video.sum())
print("Games total time : ",games.sum())

print("Average of chat : ",round(chat.mean(),1))
print("Average of study : ",round(study.mean(),1))
print("Average of video : ",round(video.mean(),1))
print("Average of games : ",round(games.mean(),1))

diff=study-games

print("Index of max differece : ",diff.argmax())
print("Index of min differece : ",diff.argmin())


                                            