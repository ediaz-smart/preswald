from preswald import text, plotly, connect, get_df, table, query, slider
import pandas as pd
import plotly.express as px

# Load the CSV
connect()
df = get_df('sample')

sql = "SELECT * FROM sample WHERE Age < 30"
filtered_df = query(sql, "sample")

text("# My Data Analysis App")
table(filtered_df, title="Filtered Data")

threshold = slider("Threshold", min_val = 0, max_val = 60, default = 30)
dynamic_view = df[df["Age"] < threshold]
table(dynamic_view, title = "Dynamic Data View")

# Create a scatter plot
fig = px.scatter(df, x="Occupation", y="Age", color="Sleep Duration", title="Interactive Scatter Plot")

# Show the plot
plotly(fig)