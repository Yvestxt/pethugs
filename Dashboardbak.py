#Yves & Maria Clara & Marina Cristina & Eduardo
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

pets = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#distribuição de dados
#dados abandono
abandono = pd.DataFrame({
    "Causas": ["Sujeira", "Destrutivo fora de casa", "Agressivo a pessoas", "Vício em fugir de casa", "Ativo demais", "Requer atenção demais", "Late ou uiva demais", "Morde", "Destrutivo dentro de casa", "Teimoso", "Não se adapta com outros animais", "Eutanásia", "Não amistoso", "Sujeira", "Destrutivo fora de casa", "Agressivo a pessoas", "Vício em fugir de casa", "Ativo demais", "Requer atenção demais", "Late ou uiva demais", "Morde", "Destrutivo dentro de casa", "Teimoso", "Não se adapta com outros animais", "Eutanásia", "Não amistoso"],
    "Média": [18.5, 12.6, 12.1, 11.6, 11.4, 10.9, 10.7, 9.7, 9.7, 9, 0, 0, 0, 37.7, 11.4, 10.9, 8, 4.8, 6.9, 0, 8, 0, 0, 8, 4.6, 6.9],
    "Pets": ["Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Cães", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos", "Gatos"]
})
#dados média
media = pd.DataFrame({
    "Pet": ["Cães", "Gatos", "Roedores", "Peixes", "Répteis", "Aves"],
    "Gasto mensal": [302.1,121.39,55.50,66.50,14.90,7.80],
})
#dados total
total = pd.DataFrame({
    "Espécie dos PETs": [ "Peixes ornamentais", "Cães", "Gatos", "Aves ornamentais", "Répteis e pequenos mamíferos", "Total de PETs", "Peixes ornamentais", "Cães", "Gatos", "Aves ornamentais", "Répteis e pequenos mamíferos", "Total de PETs"],
    "Média": [655800000, 360800000, 271900000, 205200000, 70300000, 1500000000, 649793940, 483116188, 381050666, 220866000, 80628340, 1594810000],
    "Anos": ["Ano de 2013", "Ano de 2013", "Ano de 2013", "Ano de 2013", "Ano de 2013", "Ano de 2013","Ano de 2018" , "Ano de 2018" ,"Ano de 2018" ,"Ano de 2018" ,"Ano de 2018" ,"Ano de 2018"]
})
#dados Louyse & Pedro
pizzacaes =go.Figure(go.Sunburst(
    labels=["Segurança/Guarda", "Companhia", "Diversão/Afetividade", "Outros", "Até 5 salários", "Mais de 5 a 10 salários", "Mais de 10 salários", "Sem declaração", "Até 5 salários", "Mais de 5 a 10 salários", "Mais de 10 salários", "Sem declaração", "Até 5 salários", "Mais de 5 a 10 salários", "Mais de 10 salários", "Sem declaração", "Até 5 salários", "Mais de 5 a 10 salários", "Mais de 10 salários", "Sem declaração"],
    parents=["Cães", "Cães", "Cães", "Cães", "Segurança/Guarda", "Segurança/Guarda", "Segurança/Guarda", "Segurança/Guarda", "Companhia", "Companhia", "Companhia", "Companhia", "Diversão/Afetividade", "Diversão/Afetividade", "Diversão/Afetividade", "Diversão/Afetividade", "Outros", "Outros", "Outros", "Outros"],
    values=[144, 429, 416, 17, 140, 647, 724, 99, 163, 429, 617, 94, 57, 206, 209, 24],
))

#color_discrete_map={"Cães":"goldenrod","Gatos":"magenta"})
#processamento de dados

abandfig = px.bar(abandono, x="Causas", y="Média", color="Pets", barmode="group")
medfig = px.bar(media, x="Pet", y="Gasto mensal", barmode="group")
totalfig = px.bar(total, x="Espécie dos PETs", y="Média", color="Anos", barmode="group")
pizzacaes.update_layout(margin = dict(t=0, l=0, r=0, b=0))


#layout
pets.layout = html.Div(children=[
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
        id='abandfig',
        figure=abandfig
    ),

#fim do primeiro gráfico (Yves & Maria Clara)
    html.H1(children='Média de gasto mensal por pet',
    style={
        'textAlign': 'center'
    }
),
    dcc.Graph(
        id='medfig',
        figure=medfig
    ),
#fim do segundo gráfico (Marina Crist. & Eduardo)
    html.H1(children='Total de PETs internacionalmente',
    style={
            'textAlign': 'center'
    }
),
    dcc.Graph(
        id='total',
        figure=totalfig
    ),
#fim do terceiro gráfico (Renann & Hugo)
    html.H1(children='Cães x Gatos por salários mínimos',
    style={
            'textAlign': 'center'
    }
),
    dcc.Graph(
        id='pizzacaes',
        figure=pizzacaes
    ),
])

    
#player
if __name__ == '__main__':
    pets.run_server(debug=True)
