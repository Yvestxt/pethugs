import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

pets = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#cores
colors = {
    'background': '#bbf6f6',
}

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
#dados estado
estados = pd.DataFrame({
    "ESTADOS": ['Acre', 'Alagoas','Amapá','Amazonas','Bahia','Ceará','Distrito Federal','Espírito Santo','Goiás','Maranhão','Mato Grosso','Mato Grosso Sul','Minas Gerais','Pará','Paraíba','Paraná','Pernambuco','Piauí','Rio de Janeiro','Rio Grande do Norte','Rio Grande do Sul','Rondônia','Roraima','Santa Catarina','São Paulo','Sergipe','Tocantins','Acre', 'Alagoas','Amapá','Amazonas','Bahia','Ceará','Distrito Federal','Espírito Santo','Goiás','Maranhão','Mato Grosso','Mato Grosso Sul','Minas Gerais','Pará','Paraíba','Paraná','Pernambuco','Piauí','Rio de Janeiro','Rio Grande do Norte','Rio Grande do Sul','Rondônia','Roraima','Santa Catarina','São Paulo','Sergipe','Tocantins'],
    "VALORES": [120, 323, 81, 404, 1691, 944, 293, 494, 1115, 794, 605, 457, 3256, 1045, 450, 2183, 947, 445, 2117, 375, 2384, 305, 64, 1256, 6289, 240, 183, 53, 216, 42, 171, 1016, 752, 62, 143, 268, 577, 212, 168, 1019, 493, 262, 597, 537, 323, 748, 194, 920, 149, 29, 369, 1950, 137, 106],
    "RAÇA": ["Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Cães","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos","Gatos"]
})
#dados pizza/motivos(Cães)
pizzacaes = go.Figure(go.Sunburst(
    labels=["Segurança/Guarda", "Companhia", "Diversão/Afetividade", "Outros", "Até 5 salários", "Mais de 5 a 10 salários", "Mais de 10 salários", "Sem declaração", "Até 5 salários", "Mais de 5 a 10 salários", "Mais de 10 salários", "Sem declaração", "Até 5 salários", "Mais de 5 a 10 salários", "Mais de 10 salários", "Sem declaração", "Até 5 salários", "Mais de 5 a 10 salários", "Mais de 10 salários", "Sem declaração"],
    parents=["Cães", "Cães", "Cães", "Cães", "Segurança/Guarda", "Segurança/Guarda", "Segurança/Guarda", "Segurança/Guarda", "Companhia", "Companhia", "Companhia", "Companhia", "Diversão/Afetividade", "Diversão/Afetividade", "Diversão/Afetividade", "Diversão/Afetividade", "Outros", "Outros", "Outros", "Outros"],
    values=[1006, 1610, 1303, 496, 144, 429, 416, 17, 140, 647, 724, 99, 163, 429, 617, 94, 57, 206, 209, 24],
    branchvalues = "total",
))
#dados pizza/motivos(Gatos)
pizzagatos = go.Figure(go.Sunburst(
    labels=["Segurança/Guarda", "Companhia", "Diversão/Afetividade", "Outros", "Até 5 salários", "Mais de 5 a 10 salários", "Mais de 10 salários", "Sem declaração", "Até 5 salários", "Mais de 5 a 10 salários", "Mais de 10 salários", "Sem declaração", "Até 5 salários", "Mais de 5 a 10 salários", "Mais de 10 salários", "Sem declaração", "Até 5 salários", "Mais de 5 a 10 salários", "Mais de 10 salários", "Sem declaração"],
    parents=["Gatos", "Gatos", "Gatos", "Gatos", "Segurança/Guarda", "Segurança/Guarda", "Segurança/Guarda", "Segurança/Guarda", "Companhia", "Companhia", "Companhia", "Companhia", "Diversão/Afetividade", "Diversão/Afetividade", "Diversão/Afetividade", "Diversão/Afetividade", "Outros", "Outros", "Outros", "Outros"],
    values=[313, 291, 332, 59, 0, 97, 194, 22, 8, 66, 208, 9, 22, 92, 210, 8, 0, 2, 57, 0],
    branchvalues = "total",
))
#color_discrete_map={"Cães":"goldenrod","Gatos":"magenta"})

#processamento de dados
abandfig = px.bar(abandono, x="Causas", y="Média", color="Pets", barmode="group")
medfig = px.bar(media, x="Pet", y="Gasto mensal", barmode="group")
totalfig = px.bar(total, x="Espécie dos PETs", y="Média", color="Anos", barmode="group")
pizzacaes.update_layout(margin = dict(t=0, l=0, r=0, b=0))
pizzagatos.update_layout(margin = dict(t=0, l=0, r=0, b=0))
estadofig = px.bar(estados, x="ESTADOS", y="VALORES", color="RAÇA", barmode="group")

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
    html.H1(children='Relação gatos e cães a cada mil domicilios',
    style={
        'textAlign': 'center'
    }
),
    dcc.Graph(
        id='estadofig',
        figure=estadofig
    ),
#fim do quarto gráfico (Mayara & Maria Cláudia)
    html.H1(children='Cães x Gatos por salários mínimos',
    style={
            'textAlign': 'center'
    }
),
    dcc.Graph(
        id='pizzacaes',
        figure=pizzacaes
    ),
    dcc.Graph(
        id='pizzagatos',
        figure=pizzagatos
    
    ),
])

#player
if __name__ == '__main__':
    pets.run_server(debug=True)