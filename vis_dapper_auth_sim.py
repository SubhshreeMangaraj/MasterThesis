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
import dash_cytoscape as cyto
import glob
import os
import dash_cytoscape as cyto
from gensim.matutils import hellinger
from scipy import spatial
from gensim import matutils
import dash
import dash_table
import pandas as pd
# import dash_design_kit as ddk
import time
import json
#import file of persona evolution
dfw = pd.read_csv (r'DAPPER_auth_sim\persona_topic.csv')
drop_optnw = ['Persona0', 'Persona1', 'Persona2', 'Persona3']

df_auth_perw = pd.read_csv (r'DAPPER_auth_sim\author_persona.csv')
authors_listw = df_auth_perw['author']

# df_sim = pd.DataFrame( columns=['Source_Author', 'Target_Author', 'Similarity'])
auth_id_doc_mapw = pd.read_csv (r'DAPPER_auth_sim\auth_id_doc_map.csv')

auth_id_doc_mapw = auth_id_doc_mapw.sort_values(by=['Size'],ascending=False)
authors_dictw=dict([(i,s) for i,s in zip(auth_id_doc_mapw.Id, auth_id_doc_mapw.Name)])
df_sim = pd.DataFrame( columns=['Source_Author', 'Target_Author', 'Similarity'])

default_stylesheet = [
    {
        'selector': 'node',
        'style': {
            'label': 'data(label)',
            "width": "mapData(size, 0, 170, 10,200)",
            "height": "mapData(size, 0, 170,10,200)",
            'background-color': '#2722AF',
            'background-opacity': '0.4'
        }
    },
    {
        'selector': 'edge',
        'style': {
            'line-color': '#A3C4BC',
            'width':'data(width)',
            'curve-style':'unbundled-bezier'
        }
    }
]
new_styles = [

    {
        'selector': '[weight >= 0]',
        'style': {
            'line-color': 'red'
        }
    },
    {
        'selector': '[weight >= 3 ]',
        'style': {
            'line-color': 'blue'
        }
    }
    ,
    {
        'selector': '[weight >= 15]',
        'style': {
            'line-color': 'green'
        }
    }
]
styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}


def layout():
    return html.Div(children=[
        html.Div([
            html.H3('Dapper-Variant - I : Analysis and visualizations for 2000-2020',style={'textAlign': 'center'}),
        ], className = 'row',style={'backgroundColor': '#d2e4f7'}
        ),

        html.Div([
            dcc.Markdown('''
                * **Author Persona Distribution plot**: This plot shows the distibution of a selected author over the personas for a selected time period.     
                * **Author Similarity Network**: This plot depicts the similarity network of the authors in the selected time period.                 
                ''')
        ], className='row',),
        html.Div([

            dcc.Dropdown(
                id='demo-dropdown-authorsw',
                # value=1103,
                options=[{'label': authors_dictw[i], 'value': i} for i in authors_dictw]
            ),

        ],  className='row',
            style={
                'borderBottom': 'thin lightgrey solid',
                'backgroundColor': 'rgb(250, 250, 250)',
                'padding': '10px 5px'}),

        html.Div(children=[
            html.Div(children=[
                dcc.Graph(id='donut_simw',
                          style={'width':650, 'height':650})
            ],style={'width': '40%', 'display': 'inline-block'},
                className= 'three columns'),
            html.Div(children=[

                cyto.Cytoscape(
                    id='cytoscape-dap-nodesw',
                    stylesheet=default_stylesheet + new_styles,
                    layout={'name': 'concentric'},
                    style={'width': '1000px','height':'700px'}
                )
            ],className='three columns',
                style={'width': '60%', 'display': 'inline-block'}),
        ],
            className='row'),

        html.Div(children=[

        ],className='row'),
        html.Div(children=[
            html.Iframe(src=app.get_asset_url('collapsible_tree_vis.html'),
                        style=dict(position="absolute",  width="100%", height="70%"))
        ],className='row')

    ])


@app.callback(
    dash.dependencies.Output('donut_simw', 'figure'),
    [dash.dependencies.Input('demo-dropdown-authorsw', 'value')])
def persona_dist(value):
    traces=[]
    auth_dist = df_auth_perw.loc[df_auth_perw.author == value, ['persona0','persona1','persona2','persona3']].values.flatten().tolist()
    # per_dist = [auth_dist['persona0'],auth_dist['persona1'],auth_dist['persona2'],auth_dist['persona3']]
    traces.append(
        go.Pie(
            labels=['Persona0','Persona1','Persona2','Persona3'],
            marker={'colors':['darkblue','orange','green','red']},
            values=auth_dist,
            name=value,
            hole=.4,
            hoverinfo="label+percent"
        )
    )
    return {
        'data':traces,
        'layout':go.Layout(
            title_text="Author distribution over personas",
            annotations=[dict(text=authors_dictw[value], x=0.18, y=0.5, font_size=13, showarrow=False)]
        )
    }

@app.callback(Output('cytoscape-dap-nodesw', 'elements'),
              Input('demo-dropdown-authorsw', 'value'))
def update_elements(value):
    datas=[]
    s=[]
    src_vec = df_auth_perw.loc[df_auth_perw.author == value, ['persona0','persona1','persona2','persona3']].values.flatten().tolist()
    s=src_vec
    for index,i in df_auth_perw.iterrows():
        tar_vec = [i['persona0'],i['persona1'],i['persona2'],i['persona3']]
        sim = 1 - spatial.distance.cosine(s, tar_vec)

        doc_source=auth_id_doc_mapw.loc[auth_id_doc_mapw['Id'] == value, 'Docs'].tolist()
        doc_target=auth_id_doc_mapw.loc[auth_id_doc_mapw['Id'] == i['author'], 'Docs'].tolist()

        doc_source_l = doc_source[0][1:-1]
        doc_target_l = doc_target[0][1:-1]

        doc_src_set = set(doc_source_l.split(", "))
        doc_tar_set = set(doc_target_l.split(", "))

        intersection = doc_src_set.intersection(doc_tar_set)

        datas.append([value,i['author'],sim,len(intersection),len(doc_tar_set)])
    df_sim1 = pd.DataFrame(datas, columns=['Source_Author', 'Id', 'Similarity','Common','Size_target'])
    df_sim1 = df_sim1.sort_values(by=['Similarity'],ascending=False)
    df_sim2 = df_sim1.loc[df_sim1['Similarity'] >= 0.85]
    df_sim2 = df_sim2.sort_values(by=['Common'],ascending=False)
    df_sim2 = df_sim2.head(20)
    merged_tab=pd.merge(df_sim2, auth_id_doc_mapw, on='Id', how='inner')
    Result = pd.DataFrame(merged_tab)
    # Result.to_csv("C:/Users/Subhashree/Documents/KMD_Thesis/Complete Code Collection/DAPPER/Results of DAPPER/whole data/Result.csv")
    degrees= dict([(i,s) for i,s in zip(merged_tab.Id, merged_tab.Size)])
    degrees1= dict([(i,n) for i,n in zip(merged_tab.Id, merged_tab.Name)])
    ele = set()
    merged_tab = merged_tab.iloc[1:]

    for i in merged_tab.iterrows():
        ele.add((i[1]['Source_Author'],i[1]['Id'],i[1]['Similarity'],i[1]['Common']))
    nodes = [
        {
            'data': {'id': s, 'label': degrees1[s], 'size':degrees[s]},
            'position': {'x': 20, 'y': -20}
        }
        for s in (degrees)
    ]

    edges = [
        {'data': {'source': source, 'target': target,'width':score*2,'weight':common}}
        for source, target,score,common in (ele)
    ]

    elements = nodes + edges

    return elements
