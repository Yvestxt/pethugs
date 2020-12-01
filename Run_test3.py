import pandas as pd     
import plotly           
import plotly.express as px

import dash             
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)


#Taken from https://opendata.cityofnewyork.us/
df = pd.read_csv("C:/Users/Paulo V.DESKTOP-060HC8T/Desktop/APC/Pets Code/Project Nexz - Pets/Data - Pets/Pets por Estado.csv")


app.layout = html.Div([

    html.Div([
        dcc.Graph(id='our_graph', figure={})
    ],className='nine columns'),

    html.Div([

    

        html.Label(['Choose column:'],style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(id='my_dropdown',
            options=[
                     #{'label': 'Cats', 'value': 'media gatos'},
                     #{'label': 'Dogs', 'value': 'media cachorros'}
                     {'label': x, 'value': x} for x in sorted(df.Tipo.unique())
                    
            ],
            optionHeight=35,                    
            value='Gato',                    
            #disabled=False,                    
            multi=False,                             
            clearable=False,                     
            style={'width':"40%"},             
                  
            ),                                  
                                                
    ],className='three columns'),

])

#---------------------------------------------------------------

@app.callback(
    Output(component_id='our_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def build_graph3(causas_chosen):
    
    #dff = df[df['animais']=='gato']
    #dff = df[df['animais']==('causas_chosen')]
    #if causas_chosen is dff['media gatos']:
    dff = df.copy()
    dff.set_index('UF', inplace=True)
    print()
    dff = df[df['Tipo']==causas_chosen]
    fig = px.bar(dff, color= 'UF',x = 'Tipo', y= 'Total', barmode='group', range_y=[0, 7000])
    
    print(causas_chosen)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
