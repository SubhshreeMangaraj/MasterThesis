
import dash_core_components as dcc

import dash_html_components as html

from dash.dependencies import Input, Output
from app import app
import timeperiod_00_05,timeperiod_06_10,timeperiod_11_15,timeperiod_16_20


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
        dcc.Tabs(id='vis_tabs_dap1', value='tab-1', children=[
            dcc.Tab(label='2000-2005', value='tab-dap-11', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='2006-2010', value='tab-dap-21', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='2011-2015', value='tab-dap-31', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='2016-2020', value='tab-dap-41', style=tab_style, selected_style=tab_selected_style)
        ]),
        html.Div(id='tabs-example-content11')
    ])
@app.callback(Output('tabs-example-content11', 'children'),
              Input('vis_tabs_dap1', 'value'))
def render_content(tab):
    if tab == 'tab-dap-11':
        return timeperiod_00_05.layout()
    elif tab == 'tab-dap-21':
        return timeperiod_06_10.layout()
    elif tab == 'tab-dap-31':
        return timeperiod_11_15.layout()
    elif tab == 'tab-dap-41':
        return timeperiod_16_20.layout()