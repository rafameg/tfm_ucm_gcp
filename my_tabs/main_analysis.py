import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output



tab_1_layout = dbc.Container([
					dcc.Tabs(id="tabs-analysis", value='AnalisisChalets', children=[
				        dcc.Tab(label='Condos and Townhomes', value='AnalisisPisos'),
				        dcc.Tab(label='Single Family Homes', value='AnalisisChalets'),
				    ], style={'fontSize' : 18}),
				    dbc.Row([
						html.Div([
									html.Br(),
									html.P("Through state-of-the-art big data technologies, ProSelling is now capable of determining the optimal price range and Suggested Sale Price for any residential property in Miami-Dade, Broward or Palm Beach counties. By employing multiple sophisticated machine learning algorithms, you will have access to the most precise estimated values for any condo, townhome or single-family home. Simply, complete the form with the description of the required property’s features and generate your prediction. Should you have any doubts about the meaning of any of the variables found on the form, be sure to click on the question-mark icon on the left size of the screen.")
								])
					]),
					html.Hr(),
					html.Div(id='tabs-content-analysis')

				], fluid = True)







