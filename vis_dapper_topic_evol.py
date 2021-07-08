
import dash_core_components as dcc

import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

san = pd.read_csv (r'C:\Users\Subhashree\Documents\KMD_Thesis\Complete Code Collection\DAPPER\Results of DAPPER\inputtopicevoldata.csv')
san_s = san['source'].tolist()
san_t = san['target'].tolist()
san_v = san['value'].tolist()
san_l = san['label'].tolist()

fig = go.Figure(go.Sankey(
    arrangement = "freeform",
    node = {
        #         "label": ["0", "0", "0", "1", "2", "3","4","5","6","7","8","9","10","11","11","12","13","13","14","15","15","16","17","18","18","19","19","20","21","22","23","24","25","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43"],
        "label": san_l,
        "x": [0.1, 0.1, 0.1, 0.1,0.1, 0.1, 0.1, 0.1,0.1,0.1,0.1,
              0.3,0.3,0.3, 0.3,0.3, 0.3, 0.3,0.3,0.3,0.3,0.3,
              0.6,0.6,0.6, 0.6,0.6, 0.6, 0.6,0.6,0.6,0.6,0.6,
              0.9,0.9,0.9, 0.9,0.9, 0.9, 0.9,0.9,0.9,0.9,0.9],
        "y": [0.1,0.2, 0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,
              0.1,0.2, 0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,
              0.1,0.2, 0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,
              0.1,0.2, 0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,],
        'pad':2},  # 10 Pixels

    link = {
        "source": san_s,
        "target": san_t,
        "value": san_v

    } ))
def layout():
    return html.Div([
        html.H5('Dapper Topics Evolution'),
        html.Div([
            dcc.Graph(figure=fig)])
    ])