from dash import Dash, html, dcc
import dash

from flask import Flask

import os

server = Flask(__name__)
server.secret_key = os.environ.get('secret_key', 'secret')

app = Dash(__name__, server, use_pages=True)
app.config.suppress_callback_exceptions = True

app.layout = html.Div([
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
])

if __name__ == '__main__':
    app.run_server(debug=True)
