import dash
import dash_core_components
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components
import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go
import random
from scipy import spatial
from datetime import datetime
from dash.dependencies import Input, Output
from app import app
import glob
import os
import time
import json
import dash_cytoscape as cyto
#import file of persona evolution
df_06_10 = pd.read_csv (r'DAPPER_06_10\persona_topic.csv')
drop_optn_06_10 = ['Persona0', 'Persona1', 'Persona2', 'Persona3']

df_auth_per_06_10 = pd.read_csv (r'DAPPER_06_10\author_persona.csv')
authors_list_06_10 = df_auth_per_06_10['author']

# df_sim = pd.DataFrame( columns=['Source_Author', 'Target_Author', 'Similarity'])
auth_id_doc_map_06_10 = pd.read_csv (r'DAPPER_06_10\auth_id_doc_map.csv')

auth_id_doc_map_06_10 = auth_id_doc_map_06_10.sort_values(by=['Size'],ascending=False)
authors_dict_06_10=dict([(i,s) for i,s in zip(auth_id_doc_map_06_10.Id, auth_id_doc_map_06_10.Name)])
#----------------------------------------------------------------------------------------------------------
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


    return html.Div([
        html.Div([
            html.H3('Dapper-Variant - II : Analysis and visualizations for 2006-2010',style={'textAlign': 'center'}),
        ], className = 'row',style={'backgroundColor': '#d2e4f7'}
        ),

        html.Div([
            dcc.Markdown('''
                * **Persona Evolution plot**: This plot shows the evolution of a selected persona in the selected time period for all the topics.
                * **Author Similarity Network**: This plot depicts the similarity network of the authors in the selected time period.
                * **Author Persona Distribution plot**: This plot shows the distibution of a selected author over the personas for a selected time period.                      
                ''')
        ], className='row',),

        html.Div([

            dcc.Dropdown(
                id='demo-dropdown_06_10',
                value='Persona0',
                options=[{'label': i, 'value': i} for i in drop_optn_06_10]
            ),

        ],className='row',
            style={
                'borderBottom': 'thin lightgrey solid',
                'backgroundColor': 'rgb(250, 250, 250)',
                'padding': '10px 5px'}),

        html.Div([
            dcc.Graph(
                id='persona-topic-06-10'
            )
        ],className='row'),


        html.Div([

            dcc.Dropdown(
                id='demo-dropdown-authors-06-10',
                value=243,
                options=[{'label': authors_dict_06_10[i], 'value': i} for i in authors_dict_06_10]
            ),

        ],  className='row',
            style={
                'borderBottom': 'thin lightgrey solid',
                'backgroundColor': 'rgb(250, 250, 250)',
                'padding': '10px 5px'}),

        html.Div(children=[
            html.Div(children=[
                dcc.Graph(id='donut_sim-06-10',
                          style={'width':650, 'height':650})
            ],style={'width': '40%', 'display': 'inline-block'},
                className= 'three columns'),
            html.Div(children=[

                cyto.Cytoscape(
                    id='cytoscape-dap-nodes-06-10',
                    stylesheet=default_stylesheet+new_styles,
                    layout={'name': 'concentric'},
                    style={'width': '1000px','height':'700px'}
                )
            ],className='three columns',
                style={'width': '60%', 'display': 'inline-block'}),
        ],
            className='row'),

        html.Div(children=[
            html.Iframe(src=app.get_asset_url('collapsible_tree_vis_06_10.html'),
                        style=dict(position="absolute",  width="100%", height="70%"))
        ],className='row')



        # html.Div([
        #     html.Pre(id='cytoscape-tapNodeData-json', style=styles['pre'])
        # ],className='row')


    ])

@app.callback(
    dash.dependencies.Output('persona-topic-06-10', 'figure'),
    [dash.dependencies.Input('demo-dropdown_06_10', 'value')])
def update_persona_evol(value):
    traces=[]
    topics=['topic0','topic1','topic2','topic3','topic4','topic5','topic6','topic7','topic8','topic9','topic10']
    colors=['#C62828', '#AD1457', '#6A1B9A','#4527A0','#283593','#1565C0','#0277BD','#00838F','#00695C','#2E7D32','#558B2F']
    print(value)
    if(value == 'Persona0'):
        df_0 = df_06_10[df_06_10['persona']==0]
        for i,j in zip(topics,colors):
            traces.append(
                go.Scatter(
                    fill= 'tonexty',
                    line=dict(width=5,shape = 'spline'),
                    name= i,
                    type= 'scatter',
                    x= ['2006','2007','2008','2009','2010'],
                    y= df_0[i],
                    # fillcolor= j,
                    opacity=1,
                    mode='lines',
                    # stackgroup='one',
                    marker=dict(size = 15)

                )
            )
    elif (value == 'Persona1'):
        df_1 = df_06_10[df_06_10['persona']==1]
        for i,j in zip(topics,colors):
            traces.append(
                go.Scatter(
                    fill= 'tonexty',
                    # line = dict(shape = 'spline',
                    #             width = 0),
                    line=dict(width=5,shape = 'spline'),
                    name= i,
                    type= 'scatter',
                    x= ['2006','2007','2008','2009','2010'],
                    y= df_1[i],
                    # fillcolor= j,
                    opacity=1,
                    mode='lines',
                    # stackgroup='one',
                    marker=dict(size = 15)

                )
            )

    elif (value == 'Persona2'):

        df_2 = df_06_10[df_06_10['persona']==2]
        for i,j in zip(topics,colors):
            traces.append(
                go.Scatter(
                    fill= 'tonexty',
                    # line = dict(shape = 'spline',
                    #             width = 0),
                    line=dict(width=5,shape = 'spline'),
                    name= i,
                    type= 'scatter',
                    x= ['2006','2007','2008','2009','2010'],
                    y= df_2[i],
                    # fillcolor= j,
                    opacity=1,
                    mode='lines',
                    # stackgroup='one',
                    marker=dict(size = 15)

                )
            )

    elif (value == 'Persona3'):
        df_3 = df_06_10[df_06_10['persona']==3]
        for i,j in zip(topics,colors):
            traces.append(
                go.Scatter(
                    fill= 'tonexty',
                    # line = dict(shape = 'spline',
                    #             width = 0),
                    line=dict(width=5,shape = 'spline'),
                    name= i,
                    type= 'scatter',
                    x= ['2006','2007','2008','2009','2010'],
                    y= df_3[i],
                    # fillcolor= j,
                    opacity=1,
                    mode='lines',
                    # stackgroup='one',
                    marker=dict(size = 15)

                )
            )

    elif (value == 'Persona4'):

        df_4 = df_06_10[df_06_10['persona']==4]
        for i,j in zip(topics,colors):
            traces.append(
                go.Scatter(
                    fill= 'tonexty',
                    # line = dict(shape = 'spline',
                    #             width = 0),
                    line=dict(width=5,shape = 'spline'),
                    name= i,
                    type= 'scatter',
                    x= ['2006','2007','2008','2009','2010'],
                    y= df_4[i],
                    # fillcolor= j,
                    opacity=1,
                    mode='lines',
                    # stackgroup='one',
                    marker=dict(size = 15)

                )
            )

    return {
        'data': traces,
        'layout': go.Layout(
            font= {'family': 'Balto'},
            title= 'Streamgraph with ThemeRiver layout',
            width= 1400,
            xaxis= {
                'mirror': True,
                'ticklen': 4,
                'showgrid': False,
                'showline': True,
                'tickfont': {'size': 11},
                'zeroline': False,
                'showticklabels': True,
                'title': 'Time slice in years',
                'type': 'linear'
            },
            yaxis= {
                'mirror': True,
                'ticklen': 4,
                'showgrid': False,
                'showline': True,
                'tickfont': {'size': 11},
                'zeroline': False,
                'showticklabels': True,
                'title': 'Distribution over topics',
                'type': 'linear'
            },
            height= 460,
            margin= {
                'b': 60,
                'l': 60,
                'r': 60,
                't': 80
            },
            hovermode='closest',
            clickmode='event+select'

        )

    }

@app.callback(
    dash.dependencies.Output('donut_sim-06-10', 'figure'),
    [dash.dependencies.Input('demo-dropdown-authors-06-10', 'value')])
def persona_dist(value):
    traces=[]
    auth_dist = df_auth_per_06_10.loc[df_auth_per_06_10.author == value, ['persona0','persona1','persona2','persona3']].values.flatten().tolist()
    # per_dist = [auth_dist['persona0'],auth_dist['persona1'],auth_dist['persona2'],auth_dist['persona3']]
    traces.append(
        go.Pie(
            labels=['persona0','persona1','persona2','persoan3'],
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
            annotations=[dict(text=authors_dict_06_10[value], x=0.18, y=0.5, font_size=13, showarrow=False)]
        )
    }

@app.callback(Output('cytoscape-dap-nodes-06-10', 'elements'),
              Input('demo-dropdown-authors-06-10', 'value'))
def update_elements(value):
    datas=[]
    s=[]
    src_vec = df_auth_per_06_10.loc[df_auth_per_06_10.author == value, ['persona0','persona1','persona2','persona3']].values.flatten().tolist()
    s=src_vec
    for index,i in df_auth_per_06_10.iterrows():
        tar_vec = [i['persona0'],i['persona1'],i['persona2'],i['persona3']]
        sim = 1 - spatial.distance.cosine(s, tar_vec)

        doc_source=auth_id_doc_map_06_10.loc[auth_id_doc_map_06_10['Id'] == value, 'Docs'].tolist()
        doc_target=auth_id_doc_map_06_10.loc[auth_id_doc_map_06_10['Id'] == i['author'], 'Docs'].tolist()

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
    merged_tab=pd.merge(df_sim2, auth_id_doc_map_06_10, on='Id', how='inner')

    degrees= dict([(i,s) for i,s in zip(merged_tab.Id, merged_tab.Size)])
    degrees1= dict([(i,n) for i,n in zip(merged_tab.Id, merged_tab.Name)])
    ele = set()
    merged_tab = merged_tab.iloc[1:]
    Result = pd.DataFrame(merged_tab)
    # Result.to_csv("C:/Users/Subhashree/Documents/KMD_Thesis/Complete Code Collection/DAPPER/Results of DAPPER/2006_2010/AUTH/Result.csv")
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