#http://127.0.0.1:8050/
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#cores
colors = {
    'background': '#bbf6f6',
}

#distribuição de dados
df = pd.DataFrame({
    "ESTADOS": ['ACRE', 'ALAGOAS','AMAPÁ','AMAZONAS','BAHIA','CEARÁ','DISTRITO FEDEERAL','ESPIRITO SANTO','GOIÁS','MARANHÃO','MATO GROSSO','MATO GROSSO SUL','MINAS GERAIS','PARÁ','PARAIBA','PARANÁ','PERNAMBUCO','PIAUÍ','RIO DE JANEIRO','RIO GRANDE DO NORTE','RIO GRANDE DO SUL','RONDÔNIA','RORAIMA','SANTA CATARINA','SÃO PAULO','SERGIPE','TOCANTINS','ACRE', 'ALAGOAS','AMAPÁ','AMAZONAS','BAHIA','CEARÁ','DISTRITO FEDEERAL','ESPIRITO SANTO','GOIÁS','MARANHÃO','MATO GROSSO','MATO GROSSO SUL','MINAS GERAIS','PARÁ','PARAIBA','PARANÁ','PERNAMBUCO','PIAUÍ','RIO DE JANEIRO','RIO GRANDE DO NORTE','RIO GRANDE DO SUL','RONDÔNIA','RORAIMA','SANTA CATARINA','SÃO PAULO','SERGIPE','TOCANTINS'],
    "VALORES": [120, 323, 81, 404, 1691, 944, 293, 494, 1115, 794, 605, 457, 3256, 1045, 450, 2183, 947, 445, 2117, 375, 2384, 305, 64, 1256, 6289, 240, 183, 53, 216, 42, 171, 1016, 752, 62, 143, 268, 577, 212, 168, 1019, 493, 262, 597, 537, 323, 748, 194, 920, 149, 29, 369, 1950, 137, 106],
    "RAÇA": ["cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","cães","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos","gatos"]
})

#processamento de dados
fig = px.bar(df, x="ESTADOS", y="VALORES", color="RAÇA", barmode="group")

#layout
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
)
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Animais por domicilio',
    style={
        'textAlign': 'center',
    }
),
    html.Div(children='Relação gatos e cães a cada mil domicilios',
    style={
        'textAlign': 'center',
    }
),
    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

#player
if __name__ == '__main__':
    app.run_server(debug=True)