from app import app
import dash_html_components as html
import dash_core_components as dcc
import my_callbacks
from app import server

app.layout = html.Div([
							    html.H1('ProSelling - Real Estate Prediction Platform'),
							    dcc.Tabs(id="tabs-master", value='Introduction', 
							    	children=[
								        dcc.Tab(label='About ProSelling', value='Introduction'),
								        dcc.Tab(label='Explore your city', value='gallery'),
								        dcc.Tab(label='Neighborhood Analyzer', value='Reporting'),
								        dcc.Tab(label='Price Estimator Tool', value='Analysis')
							    ], style={'fontSize' : 18}),
							    html.Div(id='tabs-content-master')
							])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',port='8080',debug=True)