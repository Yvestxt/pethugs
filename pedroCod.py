import plotly.graph_objects as go
#interatividades internas
fig = go.Figure()
#barras do gráfico, como adotou x quantidade, cães
fig.add_trace(go.Bar(name="até 5 salarios", x=['compra','doaçao', 'adoçao', 'outros'], y=[275,622,124,88]))
fig.add_trace(go.Bar(name="mais de 5 a 10 salarios", x=['compra','doaçao', 'adoçao', 'outros'], y=[650,740,271,97]))
fig.add_trace(go.Bar(name="mais de 10 salarios", x=['compra','doaçao', 'adoçao', 'outros'], y=[653,514,112,93]))
fig.add_trace(go.Bar(name="sem declaração", x=['compra','doaçao', 'adoçao', 'outros'], y=[204,187,70,81]))
fig . update_layout ( 
    #configurações do nome, espaçamento das barras
    title = { 
        'text' :  "Principal modo de aquisição de cachorros por domicilios particulares subdividos por classes de rendimento nominal domiciliar" , 
        'y' : 0.9 , 
        'x' : 0.45 , 
        'xanchor' :  'center' , 
        'yanchor' :  'top' })
fig.show()

fig = go.Figure()
#barras do gráfico, como adotou x quantidade, gatos
fig.add_trace(go.Bar(name="até 5 salarios", x=['compra','doaçao', 'adoçao', 'outros'], y=[46,83,123,94]))
fig.add_trace(go.Bar(name="mais de 5 a 10 salarios", x=['compra','doaçao', 'adoçao', 'outros'], y=[27,159,125,50]))
fig.add_trace(go.Bar(name="mais de 10 salarios", x=['compra','doaçao', 'adoçao', 'outros'], y=[64,168,108,23]))
fig.add_trace(go.Bar(name="sem declaração", x=['compra','doaçao', 'adoçao', 'outros'], y=[0,31,32,24]))
fig . update_layout ( 
    #configurações do nome, espaçamento das barras
title = { 
        'text' :  "Principal modo de aquisição de gatos por domicilios particulares subdividos por classes de rendimento nominal domiciliar" , 
        'y' : 0.9 , 
        'x' : 0.45 , 
        'xanchor' :  'center' , 
        'yanchor' :  'top' })


fig.show()
