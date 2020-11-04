import plotly.graph_objects as go

#interatividades internas
fig = go.Figure()

#barras do gráfico, motivos x quantidade, CÃES
fig.add_trace(go.Bar(name="até 5 salarios", x=['segurança/guarda','companhia', 'diversão/afetividade', 'outros'], y=[144,429,416,17]))
fig.add_trace(go.Bar(name="mais de 5 a 10 salarios", x=['segurança/guarda','companhia', 'diversão/afetividade', 'outros'], y=[140,647,724,99]))
fig.add_trace(go.Bar(name="mais de 10 salarios", x=['segurança/guarda','companhia', 'diversão/afetividade', 'outros'], y=[163,429,617,94]))
fig.add_trace(go.Bar(name="sem declaração", x=['segurança/guarda','companhia', 'diversão/afetividade', 'outros'], y=[57,206,209,24]))

fig . update_layout ( 
    #configurações do nome, espaçamento das barras
    title = { 
        'text' :  "Principal motivo de aquisição de cachorros por domicilios particulares subdividos por classes de rendimento nominal domiciliar" , 
        'y' : 0.93 , 
        'x' : 0.45 , 
        'xanchor' :  'center' , 
        'yanchor' :  'top' })
fig.show()

fig = go.Figure()

#barras do gráfico, motivos x quantidade, GATOS
fig.add_trace(go.Bar(name="até 5 salarios", x=['segurança/guarda','companhia', 'diversão/afetividade', 'outros'], y=[0,97,194,22]))
fig.add_trace(go.Bar(name="mais de 5 a 10 salarios", x=['segurança/guarda','companhia', 'diversão/afetividade', 'outros'], y=[8,66,208,9]))
fig.add_trace(go.Bar(name="mais de 10 salarios", x=['segurança/guarda','companhia', 'diversão/afetividade', 'outros'], y=[22,92,210,8]))
fig.add_trace(go.Bar(name="sem declaração", x=['segurança/guarda','companhia', 'diversão/afetividade', 'outros'], y=[0,2,57,0]))

fig . update_layout ( 
    #configurações do nome, espaçamento das barras
title = { 
        'text' :  "Principal motivo de aquisição de gatos por domicilios particulares subdividos por classes de rendimento nominal domiciliar" , 
        'y' : 0.93 , 
        'x' : 0.45 , 
        'xanchor' :  'center' , 
        'yanchor' :  'top' })
fig.show()