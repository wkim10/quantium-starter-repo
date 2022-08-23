from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

data = pd.read_csv("./final_data.csv")
data = data.sort_values(by="date")

app = Dash(__name__)

title_background = "#E8A0BF"
paper_background = "#FCC5C0"
plot_background = "#E8A0BF"
font_color = "#554994"

header = html.H1(
    "Pink Morsel Visualizer",
    id="header",
    style={
        "background-color": title_background,
        "border-radius": "20px",
        "color": font_color,
        "text-align": "center"
    }
)

def create_figure(graph_data):
    line_chart = px.line(graph_data, x="date", y="sales", title="Sales of Pink Morsels")
    line_chart.update_layout(
        paper_bgcolor=paper_background,
        plot_bgcolor=plot_background,
        font_color=font_color
    )
    return line_chart

graph = dcc.Graph(figure=create_figure(data), id="graph")

region_picker = dcc.RadioItems(
        ["north", "east", "south", "west", "all"],
        "all",
        inline=True,
        id="region_picker"
    )

region_container = html.Div(
    [
        region_picker
    ],
    style={
        "background-color": title_background,
        "border-radius": "20px",
        "color": font_color,
        "margin-top": "20px",
        "text-align": "center",
    }
)

@app.callback(
    Output(graph, "figure"),
    Input(region_picker, "value")
)
def update_graph(region):
    if region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["region"] == region]
    
    figure = create_figure(filtered_data)
    return figure


app.layout = html.Div(
    [
        header,
        graph,
        region_container
    ]
)

if __name__ == "__main__":
    app.run_server()