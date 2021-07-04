import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import urllib.parse as urlparse
from urllib.parse import parse_qs

from app import app
import vis_lda, vis_dtm, vis_detm, vis_atm, vis_tot, vis_dapper
import glob
import os
import sys
import subprocess

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

app.layout = html.Div([
    dcc.Tabs(id='vis_tabs', value='tab-1', children=[
        dcc.Tab(label='Latent Dirichlet Allocation', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Dynamic Topic Model', value='tab-2', style=tab_style, selected_style=tab_selected_style),
        # dcc.Tab(label='Dynamic Embedded Topic Model', value='tab-3', style=tab_style, selected_style=tab_selected_style),
        # dcc.Tab(label='Topics Over Time Model', value='tab-4', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Author Topic Model', value='tab-5', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='DAPPER Model', value='tab-6', style=tab_style, selected_style=tab_selected_style),
    ]),
    html.Div(id='tabs-example-content')
])

@app.callback(Output('tabs-example-content', 'children'),
              Input('vis_tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return vis_lda.layout()
        # return html.Div([
        # return vis_map.layout()
        # ])
    elif tab == 'tab-2':
        return vis_dtm.layout()
    # elif tab == 'tab-3':
    #     return vis_detm.layout()
    # elif tab == 'tab-4':
    #     return vis_tot.layout()
    elif tab == 'tab-5':
        return vis_atm.layout()
    elif tab == 'tab-6':
        return vis_dapper.layout()

if __name__ == '__main__':
    app.run_server(debug=True)