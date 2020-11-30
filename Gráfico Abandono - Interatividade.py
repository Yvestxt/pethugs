import pandas as pd     
import plotly           
import plotly.express as px

import dash            
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)


#Importando Dataframe:
df = pd.read_csv("C:/Users/Paulo V.DESKTOP-060HC8T/Desktop/APC/Pets Code/Project Nexz - Pets/Data - Pets/abandono.csv")

#Fazendo Layout do gráfico com HTML
app.layout = html.Div([
#Recebendo a figura do callback
    html.Div([
        dcc.Graph(id='our_graph', figure={})
    ],className='nine columns'),

    html.Div([

        html.Br(),
        html.Div(id='output_data'),
        html.Br(),

        html.Label(['Choose column:'],style={'font-weight': 'bold', "text-align": "center"}),

        dcc.RadioItems(id='my_dropdown',
            options=[
                     {'label': 'Cats', 'value': 'media gatos'},
                     {'label': 'Dogs', 'value': 'media cachorros'}
                     #{'label': x, 'value': x} for x in
                     #     sorted(df.causas.unique())
                     #{'label': 'Animal Condition', 'value': 'Animal Condition'},
                     #{'label': 'Species Status', 'value': 'Species Status'}
            ],
            #optionHeight=35,                   
            value='media gatos',                   
                       
            #multi=False,                      
            #searchable=True,                    
            #search_value='',                    
            #placeholder='Please select...',    
            #clearable=False,                     
            #style={'width':"40%"},             
            # className='select_box',           
            # persistence=True,                 
            # persistence_type='memory'         
            ),                                  
                                                
                                                
    ],className='three columns'),

])

#---------------------------------------------------------------
# Connecting the Dropdown values to the graph
@app.callback(
    Output(component_id='our_graph', component_property='figure'),
    [Input(component_id='my_dropdown', component_property='value')]
)

def build_graph(causas_chosen):
    dff=df
    #dff = df['causas'].isin(['causas_chosen'])
    #dff = df[df['animais']=='gato']
    #dff = df[df['animais']==('causas_chosen')]
    #if causas_chosen is dff['media gatos']:
    fig = px.pie(dff, names= 'causas', values= causas_chosen)
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(title={'text':'Abandono Pets',
                      'font':{'size':28},'x':0.5,'xanchor':'center'})
    #else:
    #    print('Dog')
    #    fig = px.pie(dff, names= 'causas', values= 'media cachorros', hole=0.1)
    #    fig.update_traces(textinfo='percent+label')
    #    fig.update_layout(title={'text':'Abandono Pets',
    #                    'font':{'size':28},'x':0.5,'xanchor':'center'})
    print(causas_chosen)
    return fig


#@app.callback(
#    Output(component_id='output_data', component_property='children'),
#    [Input(component_id='my_dropdown', component_property='search_value')]
#)
#
#def build_graph(data_chosen):
#    return ('Search value was: " {} "'.format(data_chosen))
##---------------------------------------------------------------

if __name__ == '__main__':
    app.run_server(debug=True)
