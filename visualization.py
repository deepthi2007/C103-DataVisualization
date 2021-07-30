import pandas as pd
import plotly.express as px

df = pd.read_csv("D:/deepthi projects/C103/data.csv")
print(df)
fig = px.scatter(df,x=df["date"],y=df["cases"],color=df["country"])
fig.show()
