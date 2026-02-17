# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
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

app.layout = html.Div(children=[
    html.H1(children='Soul Foods company data'),

    html.Div(children='''
        This dashboard reveals Pink Morsel sales.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig,
    )
])

if __name__ == '__main__':
    app.run(debug=True)
