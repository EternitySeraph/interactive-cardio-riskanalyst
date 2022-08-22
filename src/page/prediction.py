import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

import os

import dash_core_components as dcc
import dash_html_components as html

from dash import dash, callback

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# %matplotlib inline

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# all records in the csv file
heart_data = pd.read_csv('/kaggle/input/heart-failure-clinical-data/heart_failure_clinical_records_dataset.csv')

# training and testing data sets from targeted features to predict death event
Features = ['anaemia', 'high_blood_pressure', 'age']
x = heart_data[Features]
y = heart_data["DEATH_EVENT"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)

# logistic regression fit, train, tested
log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)
log_reg_pred = log_reg.predict(x_test)

# web page design
layout = html.Div([
    # form to make prediction
    html.H4(children='Input Patient Data for Prediction'),

    # age text input
    html.Label('Age:'),
    dcc.Input(value='40', type='number', id='age'),

    # sex radio selection
    html.Label('Sex:'),
    dcc.RadioItems(['Male', 'Female'], 'Female', inline=True, id='sex'),

    # anaemia radio selection
    html.Label('Anaemia:'),
    dcc.RadioItems(['Yes', 'No'], 'No', inline=True, id='anaemia'),

    # high blood pressure radio selection
    html.Label('Hypertension:'),
    dcc.RadioItems(['Yes', 'No'], 'No', inline=True, id='hypertension'),

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
        step=500
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


@callback(
    dash.dependencies.Output('graph-prediction', 'prediction'),
    [dash.dependencies.Input('age', 'value')], [dash.dependencies.Input('anaemia', 'value')],
    [dash.dependencies.Input('creatine-phos', 'value')],
    [dash.dependencies.State('input-box', 'value')])
def update_prediction(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )
