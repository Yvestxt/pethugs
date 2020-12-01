import pandas as pd     
import plotly           
import plotly.express as px

import dash
import http.client
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output







app = dash.Dash(__name__)

df1 = pd.read_csv("C:/Users/Paulo V.DESKTOP-060HC8T/Desktop/APC/Pets Code/Project Nexz - Pets/Data - Pets/abandono.csv")
df2 = pd.read_csv("C:/Users/Paulo V.DESKTOP-060HC8T/Desktop/APC/Pets Code/Project Nexz - Pets/Data - Pets/Pets por Estado.csv")
df3 = pd.read_csv("C:/Users/Paulo V.DESKTOP-060HC8T/Desktop/APC/Pets Code/Project Nexz - Pets/Data - Pets/Louyse_Raio_de_Sol.csv")
df4 = pd.read_csv("C:/Users/Paulo V.DESKTOP-060HC8T/Desktop/APC/Pets Code/Project Nexz - Pets/BarGraph - Learning/Code/Dropdown Teste/Urban_Park_Ranger_Animal_Condition.csv")

#-------------------------------------------------------------------------------------
# Deletar linhas vazias e linhas com mais de um valor de idade
df4 = df4[(df4['# of Animals']>0) & (df4['Age']!='Multiple')]
# Extract month from time call made to Ranger
df4['Month of Initial Call'] = pd.to_datetime(df4['Date and Time of initial call'])
df4['Month of Initial Call'] = df4['Month of Initial Call'].dt.strftime('%m')
# Copy columns to new columns with clearer names
df4['Quantidade de animais'] = df4['# of Animals']
df4['Tempo gasto em resgate (horas)'] = df4['Duration of Response']
#-------------------------------------------------------------------------------------

#Fazendo Layout do gráfico com HTML
app.layout = html.Div([
#Recebendo a figura do callback
    html.Div([
        dcc.Graph(id='our_graph1', figure={})
    ],className='nine columns'),

    html.Div([

        html.Br(),
        html.Div(id='output_data'),
        html.Br(),

        html.Label(['Choose column:'],style={'font-weight': 'bold', "text-align": "center"}),

        dcc.RadioItems(id='my_dropdown1',
            options=[
                     {'label': 'Cats', 'value': 'media gatos'},
                     {'label': 'Dogs', 'value': 'media cachorros'}
                     
            ],
                              
            value='media gatos',                   
                   
            ),                                  
                                                
                                                
    ],className='three columns'),

    html.Div([
        dcc.Graph(id='our_graph2', figure={})
    ],className='nine columns'),

    html.Div([

    

        html.Label(['Choose column:'],style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='my_dropdown2',
            options=[
                     #{'label': 'Cats', 'value': 'media gatos'},
                     #{'label': 'Dogs', 'value': 'media cachorros'}
                     {'label': x, 'value': x} for x in sorted(df2.Tipo.unique())
                    
            ],
            optionHeight=35,                    
            value='Gato',                    
            #disabled=False,                    
            multi=False,                             
            clearable=False,                     
            style={'width':"40%"},             
                  
            ),                                  
                                                
    ],className='three columns'),

    html.Div([
        dcc.Graph(id='our_graph3', figure={})
    ],className='nine columns'),

    html.Div([

    

        html.Label(['Escolha seu amigo:'],style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='my_dropdown3',
            options=[
                     {'label': 'Cats', 'value': 'v2'},
                     {'label': 'Dogs', 'value': 'v3'}
                     #{'label': x, 'value': x} for x in sorted(df.Tipo.unique())
                    
            ],
            optionHeight=35,                    
            value='v2',                    
            #disabled=False,                    
            multi=False,                             
            clearable=False,                     
            style={'width':"40%"},             
                  
            ),                                  
                                                
    ],className='three columns'),

    html.Div([
            html.Pre(children= "Chamadas para agentes de resgate em New York",
            style={"text-align": "center", "font-size":"100%", "color":"black"})
        ]),

        html.Div([
            html.Label(['Número de cahamados e Estado de Sáude do animal encontrado:'],style={'font-weight': 'bold'}),
            dcc.RadioItems(
                id='xaxis_raditem',
                options=[
                         {'label': 'Quantidade de ligações mensais', 'value': 'Month of Initial Call'},
                         {'label': 'Saúde dos animais', 'value': 'Animal Condition'},
                ],
                value='Animal Condition',
                style={"width": "50%"}
            ),
        ]),

        html.Div([
            html.Br(),
            html.Label(['Tempo investido em resgate e Quantitade de animais resgatados:'], style={'font-weight': 'bold'}),
            dcc.RadioItems(
                id='yaxis_raditem',
                options=[
                         {'label': 'Tempo investido (horas)', 'value': 'Tempo gasto em resgate (horas)'},
                         {'label': 'Quantidade de animais', 'value': 'Quantidade de animais'},
                ],
                value='Tempo gasto em resgate (horas)',
                style={"width": "50%"}
            ),
        
        html.Div([
        dcc.Graph(id='the_graph')
        ]),
    ]),
])

#---------------------------------------------------------------
# Connecting the Dropdown values to the graph
@app.callback(
    Output(component_id='our_graph1', component_property='figure'),
    Input(component_id='my_dropdown1', component_property='value')
    
)

def build_graph1(causas_chosen):
    
    dff1=df1
   
    fig1 = px.pie(dff1, names= 'causas', values= causas_chosen)
    fig1.update_traces(textinfo='percent+label')
    fig1.update_layout(title={'text':'Abandono Pets',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    

    print(causas_chosen)
    return fig1

@app.callback(
    Output(component_id='our_graph2', component_property='figure'),
    Input(component_id='my_dropdown2', component_property='value')
)

def build_graph2(causas_chosen2):
    
 
    dff2 = df2.copy()
    dff2.set_index('UF', inplace=True)
    print()
    dff2 = df2[df2['Tipo']==causas_chosen2]
    fig2 = px.bar(dff2, color= 'UF',x = 'Tipo', y= 'Total', barmode='group', range_y=[0, 7000])
    
    print(causas_chosen2)
    return fig2

@app.callback(
    Output(component_id='our_graph3', component_property='figure'),
    Input(component_id='my_dropdown3', component_property='value')
)

def build_graph3(causas_chosen3):
  
    #dff = df[df['animais']=='gato']
    #dff = df[df['animais']==('causas_chosen')]
    #if causas_chosen is dff['media gatos']:
    dff3 = df3.copy()
    #dff.set_index('UF', inplace=True)
    #print()
    #dff = df[df['Tipo']==causas_chosen]
    if causas_chosen3 == 'v2':
        fig3 = px.sunburst(dff3, names= 'v1', parents ='v2' , values= 'Valores_G', branchvalues="total", width=750, height=750)
    
    else:
        fig3 = px.sunburst(dff3, names= 'v1', parents ='v3' , values= 'Valores_C', branchvalues="total", width=750, height=750)
    
    print(causas_chosen3)
    
    return fig3

#-------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='xaxis_raditem', component_property='value'),
     Input(component_id='yaxis_raditem', component_property='value')]
)

def update_graph4(x_axis, y_axis):

    dff4 = df4
    # print(dff[[x_axis,y_axis]][:1])

    barchart=px.histogram(
            data_frame=dff4,
            x=x_axis,
            y=y_axis,
            title=y_axis+': by '+x_axis,
            #facet_col='Borough',
            color='Borough',
            barmode='group',
            orientation='v'
            )

    barchart.update_layout(xaxis={'categoryorder':'total ascending'},
                           title={'xanchor':'center', 'yanchor': 'top', 'y':0.9,'x':0.5,})

    return (barchart)

if __name__ == '__main__':
    app.run_server(debug=True)
