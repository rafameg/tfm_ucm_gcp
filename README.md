# Real Estate Prediction Platform

Dash Plotly dashboard used for reporting and predicting real state ownerships from Florida, USA.

Datasets are extracted directly from Real Estate agencies.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the requirements needed.

```bash
pip install -r requirements.txt
```

## Usage

Go to the folder using terminal and execute 
```python
python main.py
```
Then go to the browser and type: 0.0.0.0:8080

## Structure

The project is divided in several files and folders:

Dash_App/

	|-- app.py

	|-- main.py

	|-- my_callbacks.py

	|-- Tabs/

	|-- Resources/

	|-- Assets/

	|-- requirements.txt

	|-- Procfile

	|-- README.MD


#### main.py 

Contains the main programar that starts the execution of the project.

####  app.py

Initialize the app and the server properties

####  my_callbacks.py

Manage all the interactions between the data and the html views contained on the web

####  Tabs/... .py

Contains all the html views and programmatic to displays and capture the data and the behaviour from the user.

####  Resources

Contains all the extra files needed for the running of the application.
Most important file is:

####  	data_load.py

Contains all the calls to the several Machine Learning algorithmns implemented, XGBM models, recommendation model, data_loads, etc.

####  	resources/data_preparation folder

Contains all the scripts for preparing the data and models.

## Screenshots

#### Introduction

![Introduction](resources/readme_Screenshots/introduction.png?raw=true "Introduction view")

#### Gallery

![Gallery](resources/readme_Screenshots/gallery.png?raw=true "Gallery view")


#### Reporting

![Reporting](resources/readme_Screenshots/reporting.png?raw=true "Reporting view")



#### Analysis

![Analysis](resources/readme_Screenshots/analysis.png?raw=true "Analysis view")