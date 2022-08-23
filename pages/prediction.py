import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State

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

# dash register pages by its name, override path
dash.register_page(__name__)

# web pages design
layout = html.Div([
    # form to make prediction
    html.H4(children='Input Patient Data for Prediction'),

    # age, default value = 40, only accepts numbers, text input
    html.Div([
        # age text input
        html.Label('Age:'),
        dcc.Input(value='40', type='number', id='age', required=True)
    ], style={'padding': 10, 'flex': 1}),

    # sex, default value = female (1), radio items (2)
    html.Div([
        # sex radio selection
        html.Label('Sex:'),
        dcc.RadioItems(
            options=[
                {'label': 'Male', 'value': 0},
                {'label': 'Female', 'value': 1}
            ], value=1, inline=True, id='sex')
    ], style={'padding': 10, 'flex': 1}),

    # anaemia, default value = no (0), radio items (2)
    html.Div([
        # anaemia radio selection
        html.Label('Anaemia:'),
        dcc.RadioItems(options=[
            {'label': 'No', 'value': 0},
            {'label': 'Yes', 'value': 1}
        ], value=0, inline=True, id='anaemia')
    ], style={'padding': 10, 'flex': 1}),

    # high blood pressure (hypertension), default value = no (0), radio items (2)
    html.Div([
        # high blood pressure radio selection
        html.Label('Hypertension:'),
        dcc.RadioItems(options=[
            {'label': 'No', 'value': 0},
            {'label': 'Yes', 'value': 1}
        ], value=0, inline=True, id='hypertension')
    ], style={'padding': 10, 'flex': 1}),

    # creatine phosphokinase, slider, no default value, range 0 to 1200, step 100
    html.Div([html.Label('Creatine Phosphokinase (mcg/L):'),
              dcc.Slider(
                  id='creatine_phos',
                  value=1000,
                  min=0,
                  max=1200,
                  step=100
              )], style={'padding': 10, 'flex': 1}),

    # platelets, default value = 1000, only accepts numbers, range 1000 to 850000, text input
    html.Div([html.Label('Platelet Count:'),
              dcc.Input(id='platelets', value='1000', type='number', min=1000, max=850000, step=100, required=True)
              ], style={'padding': 10, 'flex': 1}),

    # serum sodium, slider, no default value, range 100 to 200, step 10
    html.Div([html.Label('Serum Sodium (mEq/L):'),
              dcc.Slider(
                  id='sodium',
                  value=140,
                  min=100,
                  max=200,
                  step=10
              )], style={'padding': 10, 'flex': 1}),

    # add a button to update chart
    html.Div([html.Button('Submit', id='button-update')], style={'padding': 10, 'flex': 1}),

    # field to be updated by button-update with Low/High/Very High Risk
    html.Div([dcc.Input(value='Estimated Risk', type='text', id='u_pred', readOnly=True)], style={'padding': 10, 'flex': 1})
])


# OUTPUT = u_pred, read only text field, Low/High/Very High Risk
# INPUT = age, anaemia, hypertension,
@callback(
    Output(component_id='u_pred', component_property='value'),
    Input('button-update', 'n_clicks'),
    # main values
    State(component_id='anaemia', component_property='value'),
    State(component_id='hypertension', component_property='value'),
    State(component_id='age', component_property='value'),
    # add values
    State(component_id='creatine_phos', component_property='value'),
    State(component_id='sex', component_property='value'),
    State(component_id='platelets', component_property='value'),
    State(component_id='sodium', component_property='value')
)
# Features = ['anaemia', 'high_blood_pressure', 'age']
def update_pred(n_clicks, anaemia, hypertension, age, creatine_phos, sex, platelets, sodium):
    xnew = pd.DataFrame({'anaemia': [int(anaemia)],
                         'high_blood_pressure': [int(hypertension)],
                         'age': [int(age)]})
    ynew = log_reg.predict(xnew)

    if ynew == [0]:
        if sex == 'Male' or int(platelets) > 200000 or int(sodium) < 135:
            if int(creatine_phos) < 75:
                return 'Very High Risk'  # both risk for hypertension and anaemia
            else:
                return 'High Risk'  # only risk for hypertension
        else:
            if int(creatine_phos) < 75:
                return 'High Risk'  # only risk for anaemia
            else:
                return 'Low Risk'  # no risk
    else:
        return 'Very High Risk'  # prediction indicates high risk
