import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Importation des layouts des autres pages
from apps.home import layout as home_layout
from apps.page1 import layout as page1_layout
from apps.page2 import layout as page2_layout

app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Définition de la barre de navigation et du layout principal
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Accueil | ', href='/'),
        dcc.Link('Page 1 | ', href='/page1'),
        dcc.Link('Page 2', href='/page2')
    ], className="row"),
    html.Div(id='page-content')
])

# Mise à jour du contenu de la page en fonction de l'URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page1':
        return page1_layout
    elif pathname == '/page2':
        return page2_layout
    else:
        return home_layout

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
