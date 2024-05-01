import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Importation des sous-pages
from apps import home, page1, page2

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

# Layout principal de l'application
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Home | ', href='/home'),
        dcc.Link('Page 1 | ', href='/page1'),
        dcc.Link('Page 2', href='/page2'),
    ]),
    html.Div(id='page-content')
])

# Mise à jour du contenu en fonction de l'URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page1':
        return page1.layout
    elif pathname == '/page2':
        return page2.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)
