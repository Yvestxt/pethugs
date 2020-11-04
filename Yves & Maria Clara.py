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
    "Causas": ["Sujeira", "Destrutivo fora de casa", "Agressivo a pessoas", "Vício em fugir de casa", "Ativo demais", "Requer atenção demais", "Late ou uiva demais", "Morde", "Destrutivo dentro de casa", "Teimoso", "Não se adapta com outros animais", "Eutanásia", "Não amistoso", "Sujeira", "Destrutivo fora de casa", "Agressivo a pessoas", "Vício em fugir de casa", "Ativo demais", "Requer atenção demais", "Late ou uiva demais", "Morde", "Destrutivo dentro de casa", "Teimoso", "Não se adapta com outros animais", "Eutanásia", "Não amistoso"],
    "Média": [18.5, 12.6, 12.1, 11.6, 11.4, 10.9, 10.7, 9.7, 9.7, 9, 0, 0, 0, 37.7, 11.4, 10.9, 8, 4.8, 6.9, 0, 8, 0, 0, 8, 4.6, 6.9],
    "Pets": ["Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos"]
})

#processamento de dados
fig = px.bar(df, x="Causas", y="Média", color="Pets", barmode="group")
    #color_discrete_map={"Cães":"goldenrod","Gatos":"magenta"})

#layout
app.layout = html.Div(children=[
    html.H1(children='Causas de Abandono:',
    style={
            'textAlign': 'center'
    }
),
    html.Div(children='Principais causas de abandono de cães e gatos:',
    style={
            'textAlign': 'center'
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
