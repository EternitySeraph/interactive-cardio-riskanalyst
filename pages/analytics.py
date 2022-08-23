import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

import plotly.express as px

from dash import html, dcc, dash_table, callback
import dash

# all records in the csv file
from dash.dcc import Input
from dash.html import Output

heart_data = pd.read_csv('heart_failure_clinical_records_dataset.csv')

# dash register pages by its name, override path
dash.register_page(__name__, path='/analytics')

# web page design
layout = html.Div([
    # generates scrolling table of all csv data points
    html.H4(children='Patient Data of Cardiac Patients'),
    dash_table.DataTable(
        data=heart_data.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in heart_data.columns],
        page_action='none',
        fixed_rows={'headers': True},
        style_table={'height': '300px', 'overflowY': 'auto'}
    ),
    # graph (heatmap) depicts all columns and their correlations
    px.imshow(heart_data.corr(), title="Correlation Heat Map of Heart Failure", text_auto=True,
              aspect="auto"),
    # dropdown changes graph to depict data points corresponding to death event
    html.H4(children='Relation of Diabetes and Smoking to Survival Rate'),
    dcc.Dropdown(id='u_drop',
                 options=['Diabetes', 'Smoking'],
                 value='Diabetes',
                 multi=False,
                 style={'width': '50%'}),
    # graph will be updated with corresponding figure according to dropdown
    dcc.Graph(id='u_graph', figure={})
])


@callback(
    Output(component_id='u_graph', component_property='figure'),
    Input(component_id='u_drop', component_property='value')
)
def update_graph(dropdown_value):
    u_graph_figure = px.violin(heart_data, y="age", x=dropdown_value, color="DEATH_EVENT", box=True, points="all",
                               hover_data=heart_data.columns)
    return u_graph_figure
