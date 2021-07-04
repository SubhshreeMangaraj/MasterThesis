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

import glob
import os

import time
import json

from app import app
import vis_dapper_home,vis_dapper_variant1, Dapper_dynamic,vis_timeperiod

def layout():
    tabs_styles = {
        'height': '44px'
    }
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
        dcc.Tabs(id='vis_tabs_dap', value='tab-1', children=[
            dcc.Tab(label='Variant 1', value='tab-dap-1', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Variant 2', value='tab-dap-2', style=tab_style, selected_style=tab_selected_style),
        ]),
        html.Div(id='tabs-example-content1')
    ])
@app.callback(Output('tabs-example-content1', 'children'),
              Input('vis_tabs_dap', 'value'))
def render_content(tab):
    if tab == 'tab-dap-2':
        return Dapper_dynamic.layout()
    elif tab == 'tab-dap-1':
        return vis_dapper_variant1.layout()

