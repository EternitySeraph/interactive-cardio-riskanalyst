import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

import plotly.express as px

import plotly.figure_factory as ff

from dash import html, dcc, dash_table, callback
from dash.dependencies import Input, Output
import dash

# all records in the csv file
heart_data = pd.read_csv('heart_failure_clinical_records_dataset.csv')

# dash register pages by its name, override path
dash.register_page(__name__)

# graph (heatmap) depicts all columns and their correlations
fig_corr = px.imshow(heart_data.corr(), title="Correlation Heat Map of Heart Failure", text_auto=True,
                     aspect="auto")

fig_dist = ff.create_distplot(heart_data, 'age')
fig_dist.update_layout(title_text='Age Distribution plot')

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
    dcc.Graph(figure=fig_corr),

    dcc.Graph(figure=fig_dist),

    # dropdown changes graph to depict data points corresponding to death event
    html.H4(children='Relation of Diabetes and Smoking to Survival Rate'),
    dcc.Dropdown(id='u_drop',
                 options=[
                     {'label': 'Diabetes', 'value': 'diabetes'},
                     {'label': 'Smoking', 'value': 'smoking'}
                 ],
                 value='diabetes',
                 multi=False,
                 searchable=False,
                 style={'width': '50%'}),
    # graph will be updated with corresponding figure according to dropdown
    dcc.Graph(id='u_graph', figure={})
])


@callback(
    Output(component_id='u_graph', component_property='figure'),
    Input(component_id='u_drop', component_property='value')
)
def update_graph(dropdown_value):
    u_graph_figure = px.violin(heart_data, y="age", x=str(dropdown_value), color="DEATH_EVENT", box=True, points="all",
                               hover_data=heart_data.columns)
    return u_graph_figure
