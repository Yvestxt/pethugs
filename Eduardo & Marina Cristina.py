#http://127.0.0.1:8050/
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#distribuição de dados
df = pd.DataFrame({
    "Pet": ["Cães", "Gatos", "Roedores", "Peixes", "Répteis", "Aves"],
    "Gasto mensal": [302.1,121.39,55.50,66.50,14.90,7.80],
})

#processamento de dados
fig = px.bar(df, x="Pet", y="Gasto mensal", barmode="group")

#layout
app.layout = html.Div(children=[
    html.H1(children='Pet Hugs',
    style={
        'textAlign': 'center',
    }
),
    html.Div(children='Média de gasto mensal por pet',
    style={
        'textAlign': 'center',
    }
),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

#player
if __name__ == '__main__':
    app.run_server(debug=True)