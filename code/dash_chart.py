# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("data/filtered_dataset.csv")
df = df.sort_values("date")

fig = px.line(
    df,
    x="date",
    y="sales",
    color='price',
    title="Pink Morsel Sales Before and After Price Increase (15 Jan 2021)",
    labels={
        "date": "Date",
        "sales": "Total Sales ($)"
    }
)

app.layout = html.Div(
    style={
        "backgroundColor": "grey",
        "fontFamily": "Arial, sans-serif",
        "padding": "30px"
    },

    children=[
    html.H1(children='Soul Foods company data',
            id="header"),

    html.Div(children='''
        This dashboard reveals Pink Morsel sales.
    '''),

    html.Div([
            dcc.RadioItems(
                options = [
                {'label' : 'North', "value" : "north"}, 
                 {'label' : 'East', "value" : "east"}, 
                 {'label' : 'South', "value" : "south"},
                 {'label' : 'West', "value" : "west"},
                 {'label' : 'All Regions', "value" : "all"},
                ],
                value = 'all',
                id='region-filter',
                inline=True
            )
        ]),
        
    dcc.Graph(
        id='data-graph',
        figure=fig,
    )
])


@callback(
    Output('data-graph', 'figure'),
    Input('region-filter', 'value'))
def update_graph(selected_region):
    
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df.region == selected_region]
    
    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color='price',
        title="Sales Before and After Price Increase (15 Jan 2021) in " + str(selected_region) + " region",
        labels={
            "date": "Date",
            "sales": "Total Sales ($)"
        }
    )

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 50, 'r': 0}, hovermode='closest',  paper_bgcolor="#DED7DD",)

    return fig


@callback(
    Output('container-no-ctx', 'children'),
    Input('region-filter', 'value'))
def update(selected):
    return f'selected: {selected}'

if __name__ == '__main__':
    app.run(debug=True)
