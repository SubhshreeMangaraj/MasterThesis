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
import vis_dapper_variant2,vis_timeperiod

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
        dcc.Tabs(id='vis_tabs_dap_dyn', value='tab-1', children=[
            dcc.Tab(label='Topic Evolution over 2000-2020', value='tab-dap-1', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Discrete Time Period Analysis', value='tab-dap-2', style=tab_style, selected_style=tab_selected_style)
        ]),
        html.Div(id='tabs-example-dynamic')
    ])
@app.callback(Output('tabs-example-dynamic', 'children'),
              Input('vis_tabs_dap_dyn', 'value'))
def render_content(tab):
    if tab == 'tab-dap-1':
        return vis_dapper_variant2.layout()
    elif tab == 'tab-dap-2':
        return vis_timeperiod.layout()
