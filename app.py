import dash
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.SPACELAB]

app = dash.Dash(__name__,external_stylesheets=external_stylesheets,title="ProSelling")
server = app.server

app.config['suppress_callback_exceptions'] = True

