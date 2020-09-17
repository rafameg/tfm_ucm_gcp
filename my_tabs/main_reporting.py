import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output



tab_1_layout = dbc.Container([
					dcc.Tabs(id="tabs-reporting", value='ReportingChalets', children=[
				        dcc.Tab(label='Condos and Townhomes', value='ReportingPisos'),
				        dcc.Tab(label='Single Family Homes', value='ReportingChalets'),
				    ], style={'fontSize' : 18}),
				    dbc.Row([
						html.Div([
									html.Br(),
									html.P("Take advantage of ProSelling’s cutting-edge business intelligence tools to analyze a wide array of properties recently sold in the tri-county area. Choose between Condos and Townhomes or Single-Family Homes and customize your search by selecting one or multiple cities and your desired maximum price range. Review the resulting table with matching properties and key features and locate each one of them on the integrated fully dynamic map. Do want to learn more about these properties? Scroll down and get access to additional statistical data about the county and city where these condos or homes are located.")
								])
					]),
					html.Hr(),
					html.Div(id='tabs-content-reporting')

				], fluid = True)







