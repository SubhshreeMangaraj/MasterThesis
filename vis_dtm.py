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
from dash.dependencies import Input, Output,State
from app import app
from gensim.models import ldaseqmodel
import glob
import os
import plotly.express as px
from gensim.test.utils import datapath
import time
import json
from wordcloud import WordCloud
import base64
from io import BytesIO


rest1 = pd.read_csv (r'DTM\rest1.csv')
rest2 = pd.read_csv (r'DTM\rest2.csv')
rest3 = pd.read_csv (r'DTM\rest3.csv')
rest4 = pd.read_csv (r'DTM\rest4.csv')
traces=[]

model = ldaseqmodel.LdaSeqModel.load("dtm_model")

colors=['#C62828', '#AD1457', '#6A1B9A','#4527A0','#283593','#1565C0','#0277BD','#00838F','#00695C','#2E7D32','#558B2F']
for i in range(0,11):

    traces.append(go.Scatter(
    # f.add_trace(go.Scatter(
    x=[1,2,3,4],
    y=[rest1['score'][i],rest2['score'][i],rest3['score'][i],rest4['score'][i]],
    type='scatter',
    mode='lines',
    line=dict(width=5,shape = 'spline'),
    # stackgroup='one',
    fill='tonexty',
    name= 'Topic '+str(i),
    opacity=1,
    line_color=colors[i],
    marker=dict(size = 15),
    ))
# print(traces)
lay1 = go.Layout(
    xaxis={
        'title': 'Time slice in years',
        'type': 'linear'

    },
    yaxis={
        'title': 'Strength of Topics',
        'type': 'linear'

    },
    title='Visualization of Topics Evolution ( The strength of a topic over the time slices are to be inferred only by the coloured area of the topic respectively )',
    hovermode='closest',
    clickmode='event+select'
)


def layout():
    return html.Div(children=[
        html.Div([
            html.H3('Dynamic Topic Model: Analysis and visualizations for different time periods',style={'textAlign': 'center'}),
        ], className = 'row',style={'backgroundColor': '#d2e4f7'}
        ),

        html.Div([
            dcc.Markdown('''
                * **Topic Evolution plot**: This plot depicts evolution of topics over time (2000-2020).
                * **Word Distribution Chart**: Shows how the content of a topic has changed over the time
                * **Topic Content**: This plot gives the distribution of words in the selected topic for a selected time period.    
                ''')
        ], className='row',),

        html.Div(children=[
            dcc.Graph(id='dtm_topic_evol',
                      figure={
                          'data':traces,
                          'layout':lay1
                      })
        ],className='row'),

        html.Div(children=[

            html.Div(children=[
                dcc.Graph(id='word_dist')
            ],className='four columns',
              style={'display': 'inline-block', 'width': '40%'}),

            html.Div(children=[
                    dcc.Graph(id='keyword_line')
            ],className='four columns',
                style={'display': 'inline-block', 'width': '58%'})

            ],className='row'),

        html.Div(children=[
            dcc.RadioItems(id='radio_dtm',
                           labelStyle={'display': 'inline-block'}
                           )
        ],className='row'),


    ])


@app.callback(
    Output('word_dist', 'figure'),
    [Input('dtm_topic_evol', 'clickData')])
def display_click_data(clickData):
    selected_topic = json.loads(json.dumps(json.loads(json.dumps(clickData))['points']))[0]['curveNumber']
    tt=model.print_topic_times(topic= selected_topic)
    #
    traces=[]

    t0 = pd.DataFrame(tt[0],columns=['word','score'])
    t1 = pd.DataFrame(tt[1],columns=['word','score'])
    t2 = pd.DataFrame(tt[2],columns=['word','score'])
    t3 = pd.DataFrame(tt[3],columns=['word','score'])

    t0['time']='2000-2005'
    t1['time']='2006-2010'
    t2['time']='2011-2015'
    t3['time']='2016-2020'

    t4 = t0.append(t1)
    t5 = t4.append(t2)
    t6 = t5.append(t3)

    fig = px.bar(t6, x="time", y="score", color="word", title="Visualisation of Keywords Distribution",
                 color_discrete_sequence=['#C62828', '#AD1457', '#6A1B9A','#4527A0','#283593','#1565C0','#0277BD','#00838F','#00695C','#2E7D32','#558B2F','#9E9D24','#F9A825','#FF8F00','#EF6C00','#D84315','#4E342E','#424242','#37474F','#000000']
                 ,opacity =0.7)
    return fig

@app.callback(
    Output('radio_dtm', 'options'),
    [Input('dtm_topic_evol', 'clickData')]
)
def radio_options5(clickData):
    selected_topic = json.loads(json.dumps(json.loads(json.dumps(clickData))['points']))[0]['curveNumber']
    tt=model.print_topic_times(topic= selected_topic)
    #
    traces=[]

    t0 = pd.DataFrame(tt[0],columns=['word','score'])
    t1 = pd.DataFrame(tt[1],columns=['word','score'])
    t2 = pd.DataFrame(tt[2],columns=['word','score'])
    t3 = pd.DataFrame(tt[3],columns=['word','score'])

    word_list=t0['word'].tolist() + t1['word'].tolist() +t2['word'].tolist() + t3['word'].tolist()
    word_set = set(word_list)
    return [{'label': opt, 'value': opt} for opt in word_set]

@app.callback(
    Output('keyword_line', 'figure'),
    [Input('dtm_topic_evol', 'clickData'),
     Input('radio_dtm', 'value')]
)

def keyline(clickdata,value):
    selected_topic = json.loads(json.dumps(json.loads(json.dumps(clickdata))['points']))[0]['curveNumber']
    tt=model.print_topic_times(topic= selected_topic)

    t0 = pd.DataFrame(tt[0],columns=['word','score'])
    t1 = pd.DataFrame(tt[1],columns=['word','score'])
    t2 = pd.DataFrame(tt[2],columns=['word','score'])
    t3 = pd.DataFrame(tt[3],columns=['word','score'])

    t0['time']='2000-2005'
    t1['time']='2006-2010'
    t2['time']='2011-2015'
    t3['time']='2016-2020'

    t4 = t0.append(t1)
    t5 = t4.append(t2)
    t6 = t5.append(t3)

    df_key=t6[t6.word == value]

    fig = px.line(df_key, x="time", y="score", title='Visualization of Individual Keyword Distribution')

    return  fig

@app.callback(
    dash.dependencies.Output("dtm_topic_evol", "figure"),
    [dash.dependencies.Input("dtm_topic_evol", "clickData")]
)
def highlight_trace(clickData):
    traces=[]
    selected_topic = json.loads(json.dumps(json.loads(json.dumps(clickData))['points']))[0]['curveNumber']
    colors=['#C62828', '#AD1457', '#6A1B9A','#4527A0','#283593','#1565C0','#0277BD','#00838F','#00695C','#2E7D32','#558B2F']
    for i in range(0,11):
        if i == selected_topic:
            traces.append(go.Scatter(
                # f.add_trace(go.Scatter(
                x=[1,2,3,4],
                y=[rest1['score'][i],rest2['score'][i],rest3['score'][i],rest4['score'][i]],
                type='scatter',
                mode='lines',
                line=dict(width=8,shape = 'spline'),
                # stackgroup='one',
                fill='tonexty',
                name= 'Topic '+str(i),
                opacity=1,
                line_color=colors[i],
                marker=dict(size = 15),
            ))
        else:
            traces.append(go.Scatter(
                # f.add_trace(go.Scatter(
                x=[1,2,3,4],
                y=[rest1['score'][i],rest2['score'][i],rest3['score'][i],rest4['score'][i]],
                type='scatter',
                mode='lines',
                line=dict(width=0.1,shape = 'spline'),
                # stackgroup='one',
                fill='tonexty',
                name= 'Topic '+str(i),
                opacity=0.001,
                line_color=colors[i],
                marker=dict(size = 15),
            ))


    return {
        'data': traces,
        'layout':lay1
    }