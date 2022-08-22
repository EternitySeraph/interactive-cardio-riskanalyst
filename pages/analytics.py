import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

import plotly.express as px

from dash import html, dash
import dash

# all records in the csv file
heart_data = pd.read_csv('heart_failure_clinical_records_dataset.csv')


# reusable table gen component (first 10 rows)
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


# graph depicts data points as age and smoking as chance of death event
fig1 = px.violin(heart_data, y="age", x="smoking", color="DEATH_EVENT", box=True, points="all",
                 hover_data=heart_data.columns)
fig1.update_layout(title_text="Analysis in Age and Smoking on Survival Status")

# graph depicts data points as age and diabetes as chance of death event
fig2 = px.violin(heart_data, y="age", x="diabetes", color="DEATH_EVENT", box=True, points="all",
                 hover_data=heart_data.columns)
fig2.update_layout(title_text="Analysis in Age and Diabetes on Survival Status")

# dash register pages by its name, override path
dash.register_page(__name__, path='/analytics')

layout = html.Div([
    # generates table of first ten rows from csv data points
    html.H4(children='Patient Data of Cardiac Patients'),
    generate_table(heart_data),
    # graph (heatmap) depicts all columns and their correlations
    px.imshow(heart_data.corr(), title="Correlation Heat Map of Heart Failure", text_auto=True,
              aspect="auto"),
    # graph depicts data points as age and smoking as chance of death event
    fig1.show(),
    # graph depicts data points as age and diabetes as chance of death event
    fig2.show()
])
