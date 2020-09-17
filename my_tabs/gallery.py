import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
from resources import data_load

df_chalets = data_load.data_load_images_chalets()

tab_1_layout = dbc.Container([
    html.Br(),
    # Se Crea la PRIMERA FILA:
    dbc.Row([
        # La primera fila solo incluye UNA COLUMNA, esta columna
        # contiene el titulo de esta seccion:
        
        html.Div([
            html.H2('Featured Virtual Tours'),
        ],style = {'text-align' : 'left'} )
            
    ]),
    html.Hr(),  # Añade un linea horizontal

    # Se Crea la SEGUNDA FILA:
    dbc.Row([
        # Solo contiene un columna que incluye un elemento
        # MARKDOWN, que sera una pequeña descripcion de la seccion:
        dbc.Col(
            html.Div([
                dcc.Markdown(
                    id = 'markdown',
                    children = '''
                        Immerse yourself in the city of your dreams. Click on any of the following virtual tours of properties currently available for sale in the most emblematic areas of Miami. Find the house or condo right for you and contact us to coordinate an appointment.
                    '''
                )
            ]),
            
            ),
        ]),
    dbc.Row([
        dbc.Col(
            html.Div([
                html.Iframe(src = 'https://player.vimeo.com/video/254172349?autoplay=1',  style={'width': 525, 'height' : 300, 'horizontal-align': 'center'})
            ],style = {'text-align' : 'left'} ),
            ),
        dbc.Col(
            html.Div([
                html.Iframe(src = 'https://player.vimeo.com/video/245191755?autoplay=1',  style={'width': 525, 'height' : 300, 'horizontal-align': 'center'})
            ],style = {'text-align' : 'left'} ),
            )

    ]),

    
    html.Hr(),  # Añade un linea horizontal
    html.H2("Featured Properties"),
    html.Hr(),
    dbc.Row([
        html.P("Get yourself a little tour of your own through some of the most exclusive neighborhoods in Miami. Choose the key attributes of your ideal home or condo and get acquainted with the best buying opportunities available today.")
    ]),
    html.Hr(),
    # Se Crea la TERCERA FILA:
    dbc.Row([
        # PRIMERA COLUMNA de la tercera fila, esta columna contiene el elemento de alarma
        # que lo usamos para resaltar el texto de encabezado del RadioItem de ciudades: 
        dbc.Col(
            html.Div([
                dbc.Alert([
                    "Select city:", 
                ], color = 'dark')
            ]), width = {'size':2, 'offset':2}, align = 'center'
           
        ),
        # SEGUNDA COLUMNA de la tercera fila, esta columna contiene el elemento de alarma
        # que lo usamos para resaltar el texto de encabezado del RadioItem de caracteristicas: 
        dbc.Col(
            html.Div([
                dbc.Alert([
                    "Select features:", 
                ], color = 'dark')
            ]), width = {'size':2, 'offset':4}, align = 'center'
        )
    ]),


    # Se Crea la CUARTA FILA:
    dbc.Row([
        # PRIMERA COLUMNA de la cuarta fila, esta columna contiene
        # el elemento RadioItem para seleccionar una ciudad: 
        dbc.Col(
            html.Div([
                dcc.RadioItems(
                    id='city',
                    options=[{'label': i, 'value': i} for i in df_chalets['city'].unique()],
                    value='Coconut Grove',
                    labelStyle = {'display': 'block'}
                ),

            ], style={'fontFamily':'arial', 'fontSize':20,}), 
            width = {'size':2, 'offset':2}
        ),
        # SEGUNDA COLUMNA de la cuarta fila, esta columna contiene
        # el elemento RadioItem para seleccionar una caracterisca: 
        dbc.Col(
            html.Div([
                dcc.RadioItems(
                    id='characteristics',
                    options=[{'label': i, 'value': i} for i in df_chalets['characteristics'].unique()],
                    value='Garden',
                    labelStyle = {'display': 'block'}
                ),
               
            ], style={'fontFamily':'arial', 'fontSize':20}), 
            width = {'size':2, 'offset':4}
        )
    ], justify = 'start'),
    
    html.Hr(),  # Añade un linea horizontal
    html.Br(),

    # Se Crea la QUINTA FILA:
    dbc.Row([
        # Solo tiene una columna que va a incluir la imagen:
        dbc.Col(
            html.Div([
                html.Img(id='display-image', src='children', height=300, style = {'align' : 'center'} )
            ], style = {'text-align' : 'left'}),
        width={'offset' : 3}
        )
    ]),
])




