import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Exemple de graphique scatter
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

layout = html.Div([
    html.H1('Page 2'),
    html.Div("Cette page montre un autre exemple de graphique."),
    dcc.Graph(
        id='iris-graph',
        figure=fig
    )
])
