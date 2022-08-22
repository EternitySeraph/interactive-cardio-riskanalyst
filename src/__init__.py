import dash
import dash_core_components as dcc
import dash_html_components as html
from flask_login.utils import login_required
import plotly.express as px
import pandas as pd

def create_main_dash(flask_app):
	dash_app = dash.Dash(server=flask_app, name="MainPage", url_base_pathname="/")
	dash_app.layout = html.Div([
		html.H1('Interactive Cardio Risk Analysis'),
		html.Div(
			[
			html.Div(
				dcc.Link(
					f"{page['name']}", href=page["relative_path"]
				)
			)
			for page in dash.page_registry.values()
		]
		),
		dash.page_container
	]
	)
	)
	return dash_app
