import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

from dash import dcc, html, callback
import dash

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# all records in the csv file
heart_data = pd.read_csv('heart_failure_clinical_records_dataset.csv')

# training and testing data sets from targeted features to predict death event
Features = ['anaemia', 'high_blood_pressure', 'age']
x = heart_data[Features]
y = heart_data["DEATH_EVENT"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)

# logistic regression fit, train, tested
log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)
log_reg_pred = log_reg.predict(x_test)

# dash register pages by its name, override path
dash.register_page(__name__, path='/predictions')

# web pages design
layout = html.Div([
    # form to make prediction
    html.H4(children='Input Patient Data for Prediction'),

    html.Div(children=[
        # age text input
        html.Label('Age:'),
        dcc.Input(value='40', type='number', id='age')
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        # sex radio selection
        html.Label('Sex:'),
        dcc.RadioItems(['Male', 'Female'], 'Female', inline=True, id='sex')
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        # anaemia radio selection
        html.Label('Anaemia:'),
        dcc.RadioItems(['Yes', 'No'], 'No', inline=True, id='anaemia')
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        # high blood pressure radio selection
        html.Label('Hypertension:'),
        dcc.RadioItems(['Yes', 'No'], 'No', inline=True, id='hypertension')
    ], style={'padding': 10, 'flex': 1}),

    # creatine phosphokinase text input or slider?
    html.Label('Creatine Phosphokinase (mcg/L):'),
    dcc.Slider(
        id='creatine-phos',
        min=0,
        max=1200,
        step=100
    ),

    # platelets text input or slider?
    html.Label('Platelet Count:'),
    dcc.Slider(
        id='platelets',
        min=20000,
        max=850000,
        step=1000
    ),

    # serum sodium text input or slider?
    html.Label('Serum Sodium (mEq/L):'),
    dcc.Slider(
        id='sodium',
        min=100,
        max=200,
        step=10
    ),

    # add a button to update chart
    html.Button('Submit', id='button-update')
])
