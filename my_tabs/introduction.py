import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import base64


test_png_rafa = 'resources/team_images/image_rafa.png'
test_base64_rafa = base64.b64encode(open(test_png_rafa, 'rb').read()).decode('ascii')

test_png_jorge = 'resources/team_images/image_jorge.jpeg'
test_base64_jorge = base64.b64encode(open(test_png_jorge, 'rb').read()).decode('ascii')

test_png_ruben = 'resources/team_images/image_ruben.png'
test_base64_ruben = base64.b64encode(open(test_png_ruben, 'rb').read()).decode('ascii')

test_png_miguel = 'resources/team_images/image_miguel.jpeg'
test_base64_miguel = base64.b64encode(open(test_png_miguel, 'rb').read()).decode('ascii')

test_png_arturo = 'resources/team_images/image_arturo.jpeg'
test_base64_arturo = base64.b64encode(open(test_png_arturo, 'rb').read()).decode('ascii')

test_png_javier = 'resources/team_images/image_javier.jpeg'
test_base64_javier = base64.b64encode(open(test_png_javier, 'rb').read()).decode('ascii')

tab_1_layout = html.Div([
			    	
			    	
					dbc.Container([
						html.Br(),
						dbc.Row([
								html.Br(),
								html.Br(),
								html.H2('Welcome'),
								html.Div([
										html.P(dcc.Markdown("""

												The ProSelling web application has been developed to predict residential real estate property values for the South Florida region of the U.S. By means of advanced machine learning techniques, it is now possible to calculate the market price of a condo or a single-family home with a level of precision never before seen in the industry. The goal was to improve upon similar tools currently available to realtors and homeowners and concentrate exclusively on properties located in the Miami-Dade, Broward and Palm Beach counties. In fact, the primary focus lies on forecasting values for properties between the $150,000 and the $3.5-million range. The results obtained from the appplication’s initial launch evaluation process have surpassed all expectations, indicating that the *ProSelling* solution is considerably more accurate than any of its counterparts.
												\n
												This project has been led by a team of six graduate students pursuing a Master’s degree in Big Data and Business Analytics from the University Complutense Madrid. In addition, it has covered areas involving machine learning, feature engineering, business intelligence and web application development. The machine learning models were initially created and tested using R, while the web application was developed using Python and Plotly’s Dash library.

												"""))
									]),
						]),
						dbc.Row([
							dcc.Markdown("""
								## Project Structure

								                                

								#### Data Extraction

								A considerable amount of data had to be obtained and properly curated before developing any prediction model. To ensure reliable information for this analysis, all data was retrieved from the Multiple Listing Service (MLS), an exclusive database of all brokered real estate transactions available only to licensed real estate agents. In all, 41,102 single family homes and 29,801 condo closed sales were analyzed and incorporated in the design of the final machine learning models.

								#### Data Cleaning 

								Once the data was gathered, the curation process began. Data imputation techniques and feature engineering concepts were implemented to properly cleanse and transform every single variable. Out of the more than 180 variables available in the MLS, ultimately only about 50 were carefully selected and included in the dataset.

								#### Data Analysis

								In this part of the development, feature transformation and variable selection processes were applied once the dataset was properly curated. Variables were compared and evaluated to gauge their overall influence in the creation of future machine learning predictive models.

								#### Data Modeling

								This part of the development required testing multiple algorithms, such as linear regressions, Random Forest, Gradient Boosting, XGBoosting and Support Vector Machines. In the end XGBoost provided the most reliable results, in part due to its robustness and ability to deliver and exceptional accuracy when compared to other tested algorithms. 
								Furthermore, XGBoost offered the following additional advantages:
								
								*	**Regularization**: prevents overfitting by means of using L1 (Lasso Regression) and L2 (Ridge Regression) regularization, which can be controlled by changing the hyperparameters *alpha* and *lambda* respectively.
								*	**Parallel Processing**: by using multiple CPU cores, it allows the algorithm to process much faster than its older sibling, the Gradient Boosting Machine algorithm or GBM.
								*	**Handling Missing Values**: this is a positive aspect of this algorithm, yet, not an issue for the dataset employed in this project since it lacks any missing values.
								*	**Cross Validation**: allows the user to determine the exact number of boosting iterations in a single run for optimal results.
								*	**Effective Tree Pruning**: the algorithm creates splits up to the specified max_depth value, pruning trees backwards and removing splits once there are no positive gains.

								#### Reporting

								Once a dependable model is developed, the next challenge is to put it into production. A formidable way to do so is to create a dashboard where the user is free to enter values for the different variables required to execute the model. One of the best currently available solutions that incorporates BI tools with Python is Plotly’s Dash library. By creating a dashboard using Dash, it is possible to design a user-friendly web app that provides a highly reliable value assessment of any residential property in South Florida, up to $3.5 millions. The ProSelling app is without question an elegant and effective solution, unlike anything else in today’s market.

								#### Web

								As noted before, **ProSelling** is a web-based app, meaning it can be accessed locally on any computer if properly installed, and also remotely anywhere in the world where there is an internet connection. We have employed Heroku’s well-known cloud application platform to deploy the app on the internet, providing the same user interface and level of performance as the locally installed version. 
								""")
						]),
						
						html.Hr(),
						dbc.Row([
							html.H2("Team Profiles"),
						]),
						html.Br(),
						dbc.Row([
							
							dbc.Col(
								dbc.Card(
									    	[	
										        dbc.CardImg(src='data:image/png;base64,{}'.format(test_base64_ruben), top=False),
										        dbc.CardBody(
										            [
										                html.H5("Rubén Basadre", className="card-title"),
										                dbc.Button("Learn more", href="https://www.linkedin.com/in/rubén-basadre-423255169" , color="primary"),
										            ]
										        ),
									    	],
									    style={"width": "18rem"},
										)
								),
							dbc.Col(
								dbc.Card(
									    	[	
										        dbc.CardImg(src='data:image/png;base64,{}'.format(test_base64_rafa), top=False),
										        dbc.CardBody(
										            [
										                html.H5("Rafael Megales", className="card-title"),
										                dbc.Button("Learn more", href="https://www.linkedin.com/in/rmegales" , color="primary"),
										            ]
										        ),
									    	],
									    style={"width": "18rem"},
										)
								),
							dbc.Col(
								dbc.Card(
									    	[	
										        dbc.CardImg(src='data:image/png;base64,{}'.format(test_base64_jorge), top=False),
										        dbc.CardBody(
										            [
										                html.H5("Jorge Muñoz", className="card-title"),
										                dbc.Button("Learn more", href="https://www.linkedin.com/in/jmunozmendoza" , color="primary"),
										            ]
										        ),
									    	],
									    style={"width": "18rem"},
										)
								)

						]),
						dbc.Row([

							dbc.Col(
								dbc.Card(
									    	[	
										        dbc.CardImg(src='data:image/png;base64,{}'.format(test_base64_javier), top=False,style={"height" : 260}),
										        dbc.CardBody(
										            [
										                html.H5("Javier Alonso", className="card-title"),
										                dbc.Button("Learn more", href="https://www.linkedin.com/in/javier-alonso-4b85383a" , color="primary"),
										            ]
										        ),
									    	],
									    style={"width": "18rem"},
										)
								),
							dbc.Col(
								dbc.Card(
									    	[	
										        dbc.CardImg(src='data:image/png;base64,{}'.format(test_base64_arturo), top=False),
										        dbc.CardBody(
										            [
										                html.H5("Arturo Lopez", className="card-title"),
										                dbc.Button("Learn more", href="https://www.linkedin.com/in/arturo-lópez-iglesias-0b9b991b4" , color="primary"),
										            ]
										        ),
									    	],
									    style={"width": "18rem"},
										)
								),
							dbc.Col(
								dbc.Card(
									    	[	
										        dbc.CardImg(src='data:image/png;base64,{}'.format(test_base64_miguel), top=False, style={"height" : 260}),
										        dbc.CardBody(
										            [
										                html.H5("Miguel Molina", className="card-title"),
										                dbc.Button("Learn more", href="https://www.linkedin.com/in/miguel-ángel-molina-2354b3192" , color="primary"),
										            ]
										        ),
									    	],
									    style={"width": "18rem"},
										)
								)

						]),
						html.Br(),
						html.Br()


					])
			       
			   		
])

