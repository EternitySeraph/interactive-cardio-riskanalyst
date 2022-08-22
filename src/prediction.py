import dash
import dash_html_components as html
from dash import Dash

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

import os

import warnings

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

from plotly.offline import init_notebook_mode
import plotly.express as px

init_notebook_mode(connected=True)
warnings.filterwarnings("ignore")

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
log_reg_acc = accuracy_score(y_test, log_reg_pred)
