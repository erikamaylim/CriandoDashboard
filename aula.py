from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


df = pd.read_excel("Vendas.xlsx")

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append("Todas as Lojas")

app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráfico com a quantidade de produtos vendidos separados por loja.'),

    html.Div(children='''
        OBS: Este gráfico não exibe o faturamento.
    '''),

    dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista-lojas'),

    dcc.Graph(
        id='grafico-quantidade-vendas',
        figure=fig
    )
])


@app.callback(
    Output('grafico-quantidade-vendas', 'figure'),
    Input('lista-lojas', 'value')
)
def update_output(value):
    if value == "Todas as Lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja'] == value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
