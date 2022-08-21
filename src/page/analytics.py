import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import matplotlib.pyplot as plt
import warnings
import seaborn as sns
from colorama import Fore, Back, Style 
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from mlxtend.plotting import plot_confusion_matrix
from plotly.offline import plot, iplot, init_notebook_mode
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.express as px
from statsmodels.formula.api import ols
import plotly.graph_objs as gobj

# all records in the csv file
heart_data = pd.read_csv('/kaggle/input/heart-failure-clinical-data/heart_failure_clinical_records_dataset.csv')

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
fig1 = px.violin(heart_data, y="age", x="smoking", color="DEATH_EVENT", box=True, points="all", hover_data=heart_data.columns)
fig1.update_layout(title_text="Analysis in Age and Smoking on Survival Status")

# graph depicts data points as age and diabetes as chance of death event
fig2 = px.violin(heart_data, y="age", x="diabetes", color="DEATH_EVENT", box=True, points="all", hover_data=heart_data.columns)
fig2.update_layout(title_text="Analysis in Age and Diabetes on Survival Status")


app.layout = html.Div([
  # generates table of first ten rows from csv data points
  html.H4(children='Patient Data of Cardiac Patients'),
  generate_table(df),
  # graph (heatmap) depicts all columns and their correlations
  px.imshow(heart_data.corr(), title="Correlation Heat Map of Heart Failure", text_auto=True, 
  aspect="auto"),
  # graph depicts data points as age and smoking as chance of death event
  fig1.show(),
  # graph depicts data points as age and diabetes as chance of death event
  fig2.show()
])
