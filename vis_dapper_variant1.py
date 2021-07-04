import dash
import dash_core_components
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components
import dash
import dash_core_components
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import random
from datetime import datetime
from dash.dependencies import Input, Output
from app import app
import vis_dapper_topics,vis_dapper_persona_evol,vis_dapper_auth_sim
import glob
import os

import time
import json

def layout():
    tab_style = {
        'borderBottom': '1px solid #d6d6d6',
        'padding': '6px',
        'fontWeight': ''
    }

    tab_selected_style = {
        'borderTop': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'backgroundColor': '#808782',
        'color': 'white',
        'padding': '6px'
    }
    return html.Div([
        dcc.Tabs(id='vis_var1_dap1', value='tab-1', children=[
            dcc.Tab(label='Topic Content', value='tab-var1-1', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Persona Evolution', value='tab-var1-2', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Authors Similarity', value='tab-var1-3', style=tab_style, selected_style=tab_selected_style)
        ]),
        html.Div(id='tabs-var1-content')
    ])
@app.callback(Output('tabs-var1-content', 'children'),
              Input('vis_var1_dap1', 'value'))
def render_content(tab):
    if tab == 'tab-var1-1':
        return vis_dapper_topics.layout()
    elif tab == 'tab-var1-2':
        return vis_dapper_persona_evol.layout()
    elif tab == 'tab-var1-3':
        return vis_dapper_auth_sim.layout()