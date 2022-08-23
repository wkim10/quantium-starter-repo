from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

data = pd.read_csv("./final_data.csv")
data = data.sort_values(by="date")

app = Dash(__name__)

line_chart = px.line(data, x="date", y="sales", title="Sales of Pink Morsels")

app.layout = html.Div(
    [
        html.H1("Pink Morsel Visualizer"),
        dcc.Graph(figure=line_chart)
    ]
)

if __name__ == "__main__":
    app.run_server()