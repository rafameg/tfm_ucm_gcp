import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from resources import data_load
import dash_table

df_input = data_load.data_load_chalets_predictions()


tab_1_layout = html.Div([
								dbc.Row([
									dbc.Col(
										html.P("Validate user for premium features: ")
									),
									dbc.Col(
										html.Div(
										    children=[dcc.Input(id='input-userEmail-chalets')],  # fill out your Input however you need
										    style=dict(display='flex', justifyContent='center')
										)
									),
									dbc.Col(
										html.Div(id='output-userEmail-chalets')
									),
									dcc.Store(id = 'output-userEmailStatus-chalets', storage_type = 'memory')
									
								]),
								html.Hr(),
								dbc.Row([
									dbc.Col(
										html.Img(
					                        id='button-help-chalets',
					                        src="assets/question-circle-solid-chalets.svg",
					                        n_clicks=0,
					                        className='info-icon',
					                        style={'width' : 25, 'height' : 25},
					                    ),
				                    )
								]),
								##### Explicacion de las variables dentro del Rmarkdown.
								dbc.Modal(
						            [
						                dbc.ModalHeader("Single Family home variable description"),
						                dbc.ModalBody(dcc.Markdown("""
						                * __Bedrooms__: indicate the property’s number of legal bedrooms.

						                * __Bathrooms__: indicate the property’s number of legal bathrooms.

						                * __Garage Spots__: indicate the property’s number of spots available inside a garage, whether it is attached, detached or underground.

						                * __Homeowners Association__: Is your property governed by homeowner’s association?

						                * __Pool__: Does your property have an inground pool inside your property’s lot? (community pools do not apply).

						                * __Waterfront__: Is your property located next to a body of water, such as an ocean, the Intracoastal Wterway, canal, lake, river or other similar body of water? 

						                * __Living Area (Sq Ft)__: type your property’s total living area in square feet. For best results, verify that you are not indicating either the Actual Area or the Adjusted Area. The Living Area is considered the area of the property under A/C and should only take into consideration ½ of the garage if applicable. The value most be within 400 and 15,000 sq ft. Please do not type units, only numbers.

						                * __Year Construction__: indicate the year when the property was built. Do not use this entry to include the year when it was purchased by its current owner or when a renovation was completed.

						                * __Zip Code__: type the 5-digit area code corresponding to the property.

						                * __Projected Days on the Market__: you may choose between the values of 30, 60 and 90 days depending on how aggressive you want to be price-wise when you are ready to put the property on the market. A higher number in this entry should render a higher price estimate.

								        """)),
						                dbc.ModalFooter(
						                    dbc.Button(
						                        "Got it!", id="close-modal-chalets", n_clicks = 0,className="ml-auto"
						                    ),style={'textAlign': 'center'}
						                ),
						            ],
						            id="modal-chalets",
						            centered=True,
						            size='xl'
						        ),
							    dbc.Row([
						        dbc.Col(html.P('Bedrooms'),
						                    width={'size': 1, 'offset':1},
						                    ),
						         dbc.Col(html.P('Bathrooms'),
						                    width={'size': 1, 'offset':0},
						                    ),
						         dbc.Col(html.P('Garage Spots'),
						                    width={'size': 1, 'offset':0},
						                    ),
						         dbc.Col(html.P('Homeowners Association'),
						                    width={'size': 2, 'offset':0},
						                    ),
						         dbc.Col(html.P('Pool'),
						                    width={'size': 2, 'offset':0},
						                    ),
						         dbc.Col(html.P('Waterfront'),
						                    width={'size': 2, 'offset':0},
						                    ),
						         ], no_gutters=False
						        ),
						    dbc.Row([
						        dbc.Col(dcc.Dropdown(
						            id='input-bed-chalets',
						            placeholder='Number',
						            options=[ 
						                {'label': '1', 'value': 1},
						                {'label': '2', 'value': 2},
						                {'label': '3', 'value': 3},
						                {'label': '4', 'value': 4},
						                {'label': '5', 'value': 5},
						                {'label': '6', 'value': 6},
						                {'label': '7', 'value': 7},
						                {'label': '8', 'value': 8},
						                {'label': '9', 'value': 9},
						                {'label': '10', 'value': 10},
						                {'label': '11', 'value': 11},
						                {'label': '12', 'value': 12},
						                {'label': '12+', 'value': 13}]),
						            width={'size':1,'offset':1}
						    ),
						        dbc.Col(dcc.Dropdown(
						            id='input-bath-chalets',
						            placeholder='Number',
						            options=[ 
						                {'label': '1', 'value': 1},
						                {'label': '2', 'value': 2},
						                {'label': '3', 'value': 3},
						                {'label': '4', 'value': 4},
						                {'label': '5', 'value': 5},
						                {'label': '6', 'value': 6},
						                {'label': '7', 'value': 7},
						                {'label': '8', 'value': 8},
						                {'label': '9', 'value': 9},
						                {'label': '10', 'value': 10},
						                {'label': '11', 'value': 11},
						                {'label': '12', 'value': 12},
						                {'label': '12+', 'value': 13}]),
						            width={'size':1,'offset':0}
						    ),
						        dbc.Col(dcc.Dropdown(
						            id='input-garage-chalets',
						            placeholder='Number',
						            options=[ 
						                {'label': 'None', 'value': 0},
						                {'label': '1', 'value': 1},
						                {'label': '2 or more', 'value': 2}]),
						            width={'size':1,'offset':0}
						    ),
						        dbc.Col(dcc.Dropdown(
						            id='input-hoa-chalets',
						            placeholder='Yes / No',
						            options=[ 
						                {'label': 'Yes', 'value': 1},
						                {'label': 'No', 'value': 0}]),
						            width={'size':2,'offset':0}
						    ),
						        dbc.Col(dcc.Dropdown(
						            id='input-pool-chalets',
						            placeholder='Yes/No',
						            options=[
						                {'label': 'Yes', 'value': 1},
						                {'label': 'No', 'value': 0}],
						            #value=[],
						            multi=False),
						            width={'size':2,'offset':0}
						    ),
						        dbc.Col(dcc.Dropdown(
						            id='input-waterfront-chalets',
						            placeholder='Yes/No',
						            options=[ 
						                {'label': 'Yes', 'value': 1},
						                {'label': 'No', 'value': 0}]),
						            width={'size':2,'offset':0,}
						    ),
						    ], no_gutters=False
						        ),
						    html.Br(),
						    html.Br(),
						     dbc.Row([
						         dbc.Col(html.P('Living Area (Sq Ft)'),
						                    width={'size': 3, 'offset':1},
						                    ),
						         dbc.Col(html.P('Year Construction'),
						                    width={'size': 2, 'offset':0},
						                    ),
						         dbc.Col(html.P('Zip Code'),
						                    width={'size': 2, 'offset':0},
						                    ),
						         dbc.Col(html.P('Projected Days on the Market'),
						                    width={'size': 2, 'offset':0},
						                    ),
						         ], no_gutters=False
						        ),
						    dbc.Row([
						        dbc.Col(
						            dbc.Input(id='input-living_area-chalets', type='number', 
						                      placeholder='From 400 to 15000', 
						                      min=400, max=15000, step=1, className='mb-3'),
						            width={'size':3, 'offset':1},
						             ),
						        dbc.Col(dcc.Dropdown(
						            id='input-built_year-chalets',
						            placeholder='Year',
						            options=[
						                {'label': '2021', 'value': 2021},
						                {'label': '2020', 'value': 2020},
						                {'label': '2019', 'value': 2019},
						                {'label': '2018', 'value': 2018},
						                {'label': '2017', 'value': 2017},
						                {'label': '2016', 'value': 2016},
						                {'label': '2015', 'value': 2015},
						                {'label': '2014', 'value': 2014},
						                {'label': '2013', 'value': 2013},
						                {'label': '2012', 'value': 2012},
						                {'label': '2011', 'value': 2011},
						                {'label': '2010', 'value': 2010},
						                {'label': '2009', 'value': 2009},
						                {'label': '2008', 'value': 2008},
						                {'label': '2007', 'value': 2007},
						                {'label': '2006', 'value': 2006},
						                {'label': '2005', 'value': 2005},
						                {'label': '2004', 'value': 2004},
						                {'label': '2003', 'value': 2003},
						                {'label': '2002', 'value': 2002},
						                {'label': '2001', 'value': 2001},
						                {'label': '2000', 'value': 2000},
						                {'label': '1999', 'value': 1999},
						                {'label': '1998', 'value': 1998},
						                {'label': '1997', 'value': 1997},
						                {'label': '1996', 'value': 1996},
						                {'label': '1995', 'value': 1995},
						                {'label': '1994', 'value': 1994},
						                {'label': '1993', 'value': 1993},
						                {'label': '1992', 'value': 1992},
						                {'label': '1991', 'value': 1991},
						                {'label': '1990', 'value': 1990},
						                {'label': '1989', 'value': 1989},
						                {'label': '1988', 'value': 1988},
						                {'label': '1987', 'value': 1987},
						                {'label': '1986', 'value': 1986},
						                {'label': '1985', 'value': 1985},
						                {'label': '1984', 'value': 1984},
						                {'label': '1983', 'value': 1983},
						                {'label': '1982', 'value': 1982},
						                {'label': '1981', 'value': 1981},
						                {'label': '1980', 'value': 1980},
						                {'label': '1979', 'value': 1979},
						                {'label': '1978', 'value': 1978},
						                {'label': '1977', 'value': 1977},
						                {'label': '1976', 'value': 1976},
						                {'label': '1975', 'value': 1975},
						                {'label': '1974', 'value': 1974},
						                {'label': '1973', 'value': 1973},
						                {'label': '1972', 'value': 1972},
						                {'label': '1971', 'value': 1971},
						                {'label': '1970', 'value': 1970},
						                {'label': '1969', 'value': 1969},
						                {'label': '1968', 'value': 1968},
						                {'label': '1967', 'value': 1967},
						                {'label': '1966', 'value': 1966},
						                {'label': '1965', 'value': 1965},
						                {'label': '1964', 'value': 1964},
						                {'label': '1963', 'value': 1963},
						                {'label': '1962', 'value': 1962},
						                {'label': '1961', 'value': 1961},
						                {'label': '1960', 'value': 1960},
						                {'label': '1959', 'value': 1959},
						                {'label': '1958', 'value': 1958},
						                {'label': '1957', 'value': 1957},
						                {'label': '1956', 'value': 1956},
						                {'label': '1955', 'value': 1955},
						                {'label': '1954', 'value': 1954},
						                {'label': '1953', 'value': 1953},
						                {'label': '1952', 'value': 1952},
						                {'label': '1951', 'value': 1951},
						                {'label': '1950', 'value': 1950},
						                {'label': '1949', 'value': 1949},
						                {'label': '1948', 'value': 1948},
						                {'label': '1947', 'value': 1947},
						                {'label': '1946', 'value': 1946},
						                {'label': '1945', 'value': 1945},
						                {'label': '1944', 'value': 1944},
						                {'label': '1943', 'value': 1943},
						                {'label': '1942', 'value': 1942},
						                {'label': '1941', 'value': 1941},
						                {'label': '1940', 'value': 1940},
						                {'label': '1939', 'value': 1939},
						                {'label': '1938', 'value': 1938},
						                {'label': '1937', 'value': 1937},
						                {'label': '1936', 'value': 1936},
						                {'label': '1935', 'value': 1935},
						                {'label': '1934', 'value': 1934},
						                {'label': '1933', 'value': 1933},
						                {'label': '1932', 'value': 1932},
						                {'label': '1931', 'value': 1931},
						                {'label': '1930', 'value': 1930},
						                {'label': '1929', 'value': 1929},
						                {'label': '1928', 'value': 1928},
						                {'label': '1927', 'value': 1927},
						                {'label': '1926', 'value': 1926},
						                {'label': '1925', 'value': 1925},
						                {'label': '1924', 'value': 1924},
						                {'label': '1923', 'value': 1923},
						                {'label': '1922', 'value': 1922},
						                {'label': '1921', 'value': 1921},
						                {'label': '1920', 'value': 1920},
						                {'label': '1919', 'value': 1919},
						                {'label': '1918', 'value': 1918},
						                {'label': '1917', 'value': 1917},
						                {'label': '1916', 'value': 1916},
						                {'label': '1915', 'value': 1915},
						                {'label': '1914', 'value': 1914},
						                {'label': '1913', 'value': 1913},
						                {'label': '1912', 'value': 1912},
						                {'label': '1911', 'value': 1911},
						                {'label': '1910', 'value': 1910},
						                {'label': '1909', 'value': 1909},
						                {'label': '1908', 'value': 1908},
						                {'label': '1907', 'value': 1907},
						                {'label': '1906', 'value': 1906},
						                {'label': '1905', 'value': 1905},
						                {'label': '1904', 'value': 1904},
						                {'label': '1903', 'value': 1903},
						                {'label': '1902', 'value': 1902},
						                {'label': '1901', 'value': 1901},
						                {'label': '1900', 'value': 1900}]),
						            width={'size':2,'offset':0}
						            ),
						        dbc.Col(dcc.Dropdown(
						            id='input-zip-code-chalets',
						            placeholder='33131',
						            options=[ 
						                {'label': '33498', 'value': 33498},
						                {'label': '33496', 'value': 33496},
						                {'label': '33493', 'value': 33493},
						                {'label': '33487', 'value': 33487},
						                {'label': '33486', 'value': 33486},
						                {'label': '33484', 'value': 33484},
						                {'label': '33483', 'value': 33483},
						                {'label': '33480', 'value': 33480},
						                {'label': '33478', 'value': 33478},
						                {'label': '33477', 'value': 33477},
						                {'label': '33476', 'value': 33476},
						                {'label': '33473', 'value': 33473},
						                {'label': '33472', 'value': 33472},
						                {'label': '33470', 'value': 33470},
						                {'label': '33469', 'value': 33469},
						                {'label': '33467', 'value': 33467},
						                {'label': '33463', 'value': 33463},
						                {'label': '33462', 'value': 33462},
						                {'label': '33461', 'value': 33461},
						                {'label': '33460', 'value': 33460},
						                {'label': '33458', 'value': 33458},
						                {'label': '33449', 'value': 33449},
						                {'label': '33446', 'value': 33446},
						                {'label': '33445', 'value': 33445},
						                {'label': '33444', 'value': 33444},
						                {'label': '33442', 'value': 33442},
						                {'label': '33441', 'value': 33441},
						                {'label': '33438', 'value': 33438},
						                {'label': '33437', 'value': 33437},
						                {'label': '33436', 'value': 33436},
						                {'label': '33435', 'value': 33435},
						                {'label': '33434', 'value': 33434},
						                {'label': '33433', 'value': 33433},
						                {'label': '33432', 'value': 33432},
						                {'label': '33431', 'value': 33431},
						                {'label': '33430', 'value': 33430},
						                {'label': '33428', 'value': 33428},
						                {'label': '33426', 'value': 33426},
						                {'label': '33418', 'value': 33418},
						                {'label': '33417', 'value': 33417},
						                {'label': '33415', 'value': 33415},
						                {'label': '33414', 'value': 33414},
						                {'label': '33413', 'value': 33413},
						                {'label': '33412', 'value': 33412},
						                {'label': '33411', 'value': 33411},
						                {'label': '33410', 'value': 33410},
						                {'label': '33409', 'value': 33409},
						                {'label': '33408', 'value': 33408},
						                {'label': '33407', 'value': 33407},
						                {'label': '33406', 'value': 33406},
						                {'label': '33405', 'value': 33405},
						                {'label': '33404', 'value': 33404},
						                {'label': '33403', 'value': 33403},
						                {'label': '33401', 'value': 33401},
						                {'label': '33351', 'value': 33351},
						                {'label': '33334', 'value': 33334},
						                {'label': '33332', 'value': 33332},
						                {'label': '33331', 'value': 33331},
						                {'label': '33330', 'value': 33330},
						                {'label': '33328', 'value': 33328},
						                {'label': '33327', 'value': 33327},
						                {'label': '33326', 'value': 33326},
						                {'label': '33325', 'value': 33325},
						                {'label': '33324', 'value': 33324},
						                {'label': '33323', 'value': 33323},
						                {'label': '33322', 'value': 33322},
						                {'label': '33321', 'value': 33321},
						                {'label': '33319', 'value': 33319},
						                {'label': '33317', 'value': 33317},
						                {'label': '33316', 'value': 33316},
						                {'label': '33315', 'value': 33315},
						                {'label': '33314', 'value': 33314},
						                {'label': '33313', 'value': 33313},
						                {'label': '33312', 'value': 33312},
						                {'label': '33311', 'value': 33311},
						                {'label': '33309', 'value': 33309},
						                {'label': '33308', 'value': 33308},
						                {'label': '33306', 'value': 33306},
						                {'label': '33305', 'value': 33305},
						                {'label': '33304', 'value': 33304},
						                {'label': '33301', 'value': 33301},
						                {'label': '33196', 'value': 33196},
						                {'label': '33194', 'value': 33194},
						                {'label': '33193', 'value': 33193},
						                {'label': '33190', 'value': 33190},
						                {'label': '33189', 'value': 33189},
						                {'label': '33187', 'value': 33187},
						                {'label': '33186', 'value': 33186},
						                {'label': '33185', 'value': 33185},
						                {'label': '33184', 'value': 33184},
						                {'label': '33183', 'value': 33183},
						                {'label': '33182', 'value': 33182},
						                {'label': '33181', 'value': 33181},
						                {'label': '33180', 'value': 33180},
						                {'label': '33179', 'value': 33179},
						                {'label': '33178', 'value': 33178},
						                {'label': '33177', 'value': 33177},
						                {'label': '33176', 'value': 33176},
						                {'label': '33175', 'value': 33175},
						                {'label': '33174', 'value': 33174},
						                {'label': '33173', 'value': 33173},
						                {'label': '33172', 'value': 33172},
						                {'label': '33170', 'value': 33170},
						                {'label': '33169', 'value': 33169},
						                {'label': '33168', 'value': 33168},
						                {'label': '33167', 'value': 33167},
						                {'label': '33166', 'value': 33166},
						                {'label': '33165', 'value': 33165},
						                {'label': '33162', 'value': 33162},
						                {'label': '33161', 'value': 33161},
						                {'label': '33160', 'value': 33160},
						                {'label': '33158', 'value': 33158},
						                {'label': '33157', 'value': 33157},
						                {'label': '33156', 'value': 33156},
						                {'label': '33155', 'value': 33155},
						                {'label': '33154', 'value': 33154},
						                {'label': '33150', 'value': 33150},
						                {'label': '33149', 'value': 33149},
						                {'label': '33147', 'value': 33147},
						                {'label': '33146', 'value': 33146},
						                {'label': '33145', 'value': 33145},
						                {'label': '33144', 'value': 33144},
						                {'label': '33143', 'value': 33143},
						                {'label': '33142', 'value': 33142},
						                {'label': '33141', 'value': 33141},
						                {'label': '33140', 'value': 33140},
						                {'label': '33139', 'value': 33139},
						                {'label': '33138', 'value': 33138},
						                {'label': '33137', 'value': 33137},
						                {'label': '33136', 'value': 33136},
						                {'label': '33135', 'value': 33135},
						                {'label': '33134', 'value': 33134},
						                {'label': '33133', 'value': 33133},
						                {'label': '33132', 'value': 33132},
						                {'label': '33131', 'value': 33131},
						                {'label': '33130', 'value': 33130},
						                {'label': '33129', 'value': 33129},
						                {'label': '33128', 'value': 33128},
						                {'label': '33127', 'value': 33127},
						                {'label': '33126', 'value': 33126},
						                {'label': '33125', 'value': 33125},
						                {'label': '33122', 'value': 33122},
						                {'label': '33109', 'value': 33109},
						                {'label': '33101', 'value': 33101},
						                {'label': '33076', 'value': 33076},
						                {'label': '33073', 'value': 33073},
						                {'label': '33071', 'value': 33071},
						                {'label': '33069', 'value': 33069},
						                {'label': '33068', 'value': 33068},
						                {'label': '33067', 'value': 33067},
						                {'label': '33066', 'value': 33066},
						                {'label': '33065', 'value': 33065},
						                {'label': '33064', 'value': 33064},
						                {'label': '33063', 'value': 33063},
						                {'label': '33062', 'value': 33062},
						                {'label': '33060', 'value': 33060},
						                {'label': '33056', 'value': 33056},
						                {'label': '33055', 'value': 33055},
						                {'label': '33054', 'value': 33054},
						                {'label': '33039', 'value': 33039},
						                {'label': '33035', 'value': 33035},
						                {'label': '33034', 'value': 33034},
						                {'label': '33033', 'value': 33033},
						                {'label': '33032', 'value': 33032},
						                {'label': '33031', 'value': 33031},
						                {'label': '33030', 'value': 33030},
						                {'label': '33029', 'value': 33029},
						                {'label': '33028', 'value': 33028},
						                {'label': '33027', 'value': 33027},
						                {'label': '33026', 'value': 33026},
						                {'label': '33025', 'value': 33025},
						                {'label': '33024', 'value': 33024},
						                {'label': '33023', 'value': 33023},
						                {'label': '33021', 'value': 33021},
						                {'label': '33020', 'value': 33020},
						                {'label': '33019', 'value': 33019},
						                {'label': '33018', 'value': 33018},
						                {'label': '33016', 'value': 33016},
						                {'label': '33015', 'value': 33015},
						                {'label': '33014', 'value': 33014},
						                {'label': '33013', 'value': 33013},
						                {'label': '33012', 'value': 33012},
						                {'label': '33010', 'value': 33010},
						                {'label': '33009', 'value': 33009},
						                {'label': '33004', 'value': 33004}]),
						            width={'size':2,'offset':0}
						            ),
						        dbc.Col(dcc.Dropdown(
						            id='input-dom-chalets',
						            placeholder='Select between 30, 60 and 90',
						            options=[ 
						                {'label': '30', 'value': 30},
						                {'label': '60', 'value': 60},
						                {'label': '90', 'value': 90}]),
						            width={'size':2,'offset':0}
						    ),
						        
						    ], no_gutters=False
						        ),
						    dbc.Row([
									dbc.Col(
										html.Div([
											dbc.Button("Generate Prediction", id="input-predi_button-chalets", color='primary',className="mr-2")
										],style={'textAlign':'center'})
									)
								]),
						    html.Br(),
						    dcc.Loading(
						    	html.Div([
							    	dbc.Row([
							    		dbc.Col(
							        	 	html.P(id='result-prediction-chalets')
							        	)
							        ]),
							        dbc.Row([
							        	dbc.Col(
							        		html.Div(id='output-data-recomenacion-chalets')
							        	)
							        ])
							    ])
						    ),
						    html.Hr(),
					        html.P("The following table includes all the recently performed searches using ProSelling’s Price Estimator Tool. You may review this table to gauge where the market is heading (buyers or sellers markets) and what type of properties and areas may become popular in the near future. "),
					        dash_table.DataTable(
											        id='tabla-analisis-chalets',
											        columns=[{'name':i, 'id':i} for i in df_input.columns],
											        data=df_input.to_dict('records'),
											        editable=True,                  # allow user to edit data inside tabel
											        row_deletable=True,             # allow user to delete rows
											        sort_action="native",           # give user capability to sort columns
											        sort_mode="single",             # sort across 'multi' or 'single' columns
											        filter_action="native",         # allow filtering of columns
											        page_action='none',             # render all of the data at once. No paging.
											        style_table={'height': '300px', 'overflowY': 'auto'},
											        #style_cell={'textAlign': 'left', 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px'},
											        style_cell={'padding': '5px'},
												    style_header={
												        'backgroundColor': 'white',
												        'fontWeight': 'bold'
												    }
											    )

							
					])


