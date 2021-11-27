import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
graph=px.scatter(df, x="Population", y="Per capita", size="Percentage", color="Country")
graph.show()