import pandas as pd #(version 0.24.2)
import datetime as dt
import dash         #(version 1.0.0)
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly       #(version 4.4.1)
import plotly.express as px

df = pd.read_csv("C:/Users/Paulo V.DESKTOP-060HC8T/Desktop/APC/Pets Code/Project Nexz - Pets/BarGraph - Learning/Code/Dropdown Teste/Urban_Park_Ranger_Animal_Condition.csv")

#-------------------------------------------------------------------------------------
# Deletar linhas vazias e linhas com mais de um valor de idade
df = df[(df['# of Animals']>0) & (df['Age']!='Multiple')]

# Extract month from time call made to Ranger
df['Month of Initial Call'] = pd.to_datetime(df['Date and Time of initial call'])
df['Month of Initial Call'] = df['Month of Initial Call'].dt.strftime('%m')

# Copy columns to new columns with clearer names
df['Quantidade de animais'] = df['# of Animals']
df['Tempo gasto em resgate (horas)'] = df['Duration of Response']
#-------------------------------------------------------------------------------------

app = dash.Dash(__name__)

#-------------------------------------------------------------------------------------
app.layout = html.Div([

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
        ]),

    html.Div([
        dcc.Graph(id='the_graph')
    ]),

])

#-------------------------------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='xaxis_raditem', component_property='value'),
     Input(component_id='yaxis_raditem', component_property='value')]
)

def update_graph5(x_axis, y_axis):

    dff = df
    # print(dff[[x_axis,y_axis]][:1])

    barchart=px.histogram(
            data_frame=dff,
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