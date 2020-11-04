import plotly.graph_objects as go
#interatividades internas
fig = go.Figure()
#barras do gráfico, quantidade de cães e gatos por região, Configuração de cor
fig.add_trace(go.Bar(x=['Centro Oeste','Norte','Nordeste','Sudeste', 'Sul', 'Brasil'], y=[710, 1043, 4014, 3860, 1886, 11513], name="Quantidade de Gatos", marker_color='darkred'))
fig.add_trace(go.Bar(x=['Centro Oeste','Norte','Nordeste','Sudeste', 'Sul', 'Brasil'], y=[2470, 2202, 5799, 12156, 5823, 28450], name="Quantidade de Cachorros", marker_color='darkslateblue'))

fig . update_layout ( 
    #configurações do nome, espaçamento das barras
    title = { 
        'text' :  "Principal motivo de aquisição de cachorros por domicilios particulares subdividos por classes de rendimento nominal domiciliar" , 
        'y' : 0.9 , 
        'x' : 0.45 , 
        'xanchor' :  'center' , 
        'yanchor' :  'top' })
fig.show()

