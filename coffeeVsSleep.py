import plotly.express as px
import csv

with open("./data/cups of coffee vs hours of sleep.csv") as csv_file:
      df = csv.DictReader(csv_file)
      fig = px.scatter(df,x="Coffee in ml", y="sleep in hours", color="week")
      fig.show()

#A correlation of 1 means the two data sets are closely correlated. This will be a rising graph where the data points are close to a central line.

#A correlation of 0 means that the two data sets are not correlated at all! The data points will be scattered on the graph.

#A correlation of -1 means that the two data sets are inversely correlated. This will be a falling graph where the data points are close to a central line.

#correlation lies in between -1 and 1
