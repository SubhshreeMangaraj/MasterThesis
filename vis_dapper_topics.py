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
from wordcloud import WordCloud
import base64
from io import BytesIO
import glob
import os
import time
import json
#upload all topic files
topic0 = pd.read_csv (r'DAPPER_topics\topic_0.csv')
topic1 = pd.read_csv (r'DAPPER_topics\topic_1.csv')
topic2 = pd.read_csv (r'DAPPER_topics\topic_2.csv')
topic3 = pd.read_csv (r'DAPPER_topics\topic_3.csv')
topic4 = pd.read_csv (r'DAPPER_topics\topic_4.csv')
topic5 = pd.read_csv (r'DAPPER_topics\topic_5.csv')
topic6 = pd.read_csv (r'DAPPER_topics\topic_6.csv')
topic7 = pd.read_csv (r'DAPPER_topics\topic_7.csv')
topic8 = pd.read_csv (r'DAPPER_topics\topic_8.csv')
topic9 = pd.read_csv (r'DAPPER_topics\topic_9.csv')
topic10 = pd.read_csv (r'DAPPER_topics\topic_10.csv')

# function to make wordcoud from word frequency dataframe
def plot_wordcloud(data):
    d = {a: x for a, x in data.values}
    wc = WordCloud(background_color='white', width=450, height=350)
    wc.fit_words(d)
    return wc.to_image()

bar_1 = go.Figure([go.Bar(x= topic0['word'].tolist(), y=topic0['score'].tolist(),type='bar')])
bar_1.update_layout(title_text='Top 20 words for Topic 0',
                    xaxis=dict(title='Words'),
                    yaxis=dict(title='Distribution score'))
df_1 = pd.DataFrame({'word': topic0['word'].tolist(), 'freq': topic0['score'].tolist()})
img1 = BytesIO()
plot_wordcloud(data=df_1).save(img1, format='PNG')
img_1 = 'data:image/png;base64,{}'.format(base64.b64encode(img1.getvalue()).decode())

bar_2 = go.Figure([go.Bar(x= topic1['word'].tolist(), y=topic1['score'].tolist(),type='bar')])
bar_2.update_layout(title_text='Top 20 words for Topic 1',
                    xaxis=dict(title='Words'),
                    yaxis=dict(title='Distribution score'))
df_2 = pd.DataFrame({'word': topic1['word'].tolist(), 'freq': topic1['score'].tolist()})
img2 = BytesIO()
plot_wordcloud(data=df_2).save(img2, format='PNG')
img_2 = 'data:image/png;base64,{}'.format(base64.b64encode(img2.getvalue()).decode())

bar_3 = go.Figure([go.Bar(x= topic2['word'].tolist(), y=topic2['score'].tolist(),type='bar')])
bar_3.update_layout(title_text='Top 20 words for Topic 2',
                    xaxis=dict(title='Words'),
                    yaxis=dict(title='Distribution score'))
df_3 = pd.DataFrame({'word': topic2['word'].tolist(), 'freq': topic2['score'].tolist()})
img3 = BytesIO()
plot_wordcloud(data=df_3).save(img3, format='PNG')
img_3 = 'data:image/png;base64,{}'.format(base64.b64encode(img3.getvalue()).decode())

bar_4 = go.Figure([go.Bar(x= topic3['word'].tolist(), y=topic3['score'].tolist(),type='bar')])
bar_4.update_layout(title_text='Top 20 words for Topic 3',
                    xaxis=dict(title='Words'),
                    yaxis=dict(title='Distribution score'))
df_4 = pd.DataFrame({'word': topic3['word'].tolist(), 'freq': topic3['score'].tolist()})
img4 = BytesIO()
plot_wordcloud(data=df_4).save(img4, format='PNG')
img_4 = 'data:image/png;base64,{}'.format(base64.b64encode(img4.getvalue()).decode())

bar_5 = go.Figure([go.Bar(x= topic4['word'].tolist(), y=topic4['score'].tolist(),type='bar')])
bar_5.update_layout(title_text='Top 20 words for Topic 4',
                    xaxis=dict(title='Words'),
                    yaxis=dict(title='Distribution score'))
df_5 = pd.DataFrame({'word': topic4['word'].tolist(), 'freq': topic4['score'].tolist()})
img5 = BytesIO()
plot_wordcloud(data=df_5).save(img5, format='PNG')
img_5 = 'data:image/png;base64,{}'.format(base64.b64encode(img5.getvalue()).decode())

bar_6 = go.Figure([go.Bar(x= topic5['word'].tolist(), y=topic5['score'].tolist(),type='bar')])
bar_6.update_layout(title_text='Top 20 words for Topic 5',
                    xaxis=dict(title='Words'),
                    yaxis=dict(title='Distribution score'))
df_6 = pd.DataFrame({'word': topic5['word'].tolist(), 'freq': topic5['score'].tolist()})
img6 = BytesIO()
plot_wordcloud(data=df_6).save(img6, format='PNG')
img_6 = 'data:image/png;base64,{}'.format(base64.b64encode(img6.getvalue()).decode())

bar_7 = go.Figure([go.Bar(x= topic6['word'].tolist(), y=topic6['score'].tolist(),type='bar')])
bar_7.update_layout(title_text='Top 20 words for Topic 6',
                    xaxis=dict(title='Words'),
                    yaxis=dict(title='Distribution score'))
df_7 = pd.DataFrame({'word': topic6['word'].tolist(), 'freq': topic6['score'].tolist()})
img7 = BytesIO()
plot_wordcloud(data=df_7).save(img7, format='PNG')
img_7 = 'data:image/png;base64,{}'.format(base64.b64encode(img7.getvalue()).decode())

bar_8 = go.Figure([go.Bar(x= topic7['word'].tolist(), y=topic7['score'].tolist(),type='bar')])
bar_8.update_layout(title_text='Top 20 words for Topic 7',
                    xaxis=dict(title='Words'),
                    yaxis=dict(title='Distribution score'))
df_8 = pd.DataFrame({'word': topic7['word'].tolist(), 'freq': topic7['score'].tolist()})
img8 = BytesIO()
plot_wordcloud(data=df_8).save(img8, format='PNG')
img_8 = 'data:image/png;base64,{}'.format(base64.b64encode(img8.getvalue()).decode())

bar_9 = go.Figure([go.Bar(x= topic8['word'].tolist(), y=topic8['score'].tolist(),type='bar')])
bar_9.update_layout(title_text='Top 20 words for Topic 8',
                    xaxis=dict(title='Words'),
                    yaxis=dict(title='Distribution score'))
df_9 = pd.DataFrame({'word': topic8['word'].tolist(), 'freq': topic8['score'].tolist()})
img9 = BytesIO()
plot_wordcloud(data=df_9).save(img9, format='PNG')
img_9 = 'data:image/png;base64,{}'.format(base64.b64encode(img9.getvalue()).decode())

bar_10 = go.Figure([go.Bar(x= topic9['word'].tolist(), y=topic9['score'].tolist(),type='bar')])
bar_10.update_layout(title_text='Top 20 words for Topic 9',
                    xaxis=dict(title='Words'),
                    yaxis=dict(title='Distribution score'))
df_10 = pd.DataFrame({'word': topic9['word'].tolist(), 'freq': topic9['score'].tolist()})
img10 = BytesIO()
plot_wordcloud(data=df_10).save(img10, format='PNG')
img_10 = 'data:image/png;base64,{}'.format(base64.b64encode(img10.getvalue()).decode())

bar_11 = go.Figure([go.Bar(x= topic10['word'].tolist(), y=topic10['score'].tolist(),type='bar')])
bar_11.update_layout(title_text='Top 20 words for Topic 10',
                    xaxis=dict(title='Words'),
                    yaxis=dict(title='Distribution score'))
df_11 = pd.DataFrame({'word': topic10['word'].tolist(), 'freq': topic10['score'].tolist()})
img11 = BytesIO()
plot_wordcloud(data=df_11).save(img11, format='PNG')
img_11 = 'data:image/png;base64,{}'.format(base64.b64encode(img11.getvalue()).decode())

def layout():
    return html.Div(children=[
        html.Div([
            html.H3('Dapper-Variant - I : Visualizations for Topic Content over 2000-2020',style={'textAlign': 'center'}),
        ], className = 'row',style={'backgroundColor': '#d2e4f7'}
        ),
        html.Div([
            dcc.Markdown('''
                * **Topic Contents**: The plots here show the topic contents of all the topics discovered over 2000-2020 in the form of frequency chart and word cloud.                     
                ''')
        ], className='row',),

    html.Div(children=[
        html.Div(children=[
            dcc.Graph(figure=bar_1)
        ],className='four columns',
            style={'width': '60%', 'display': 'inline-block'}),
        html.Div(children=[
            html.Img(src=img_1)
        ],className='four columns',
            style={'width': '40%', 'display': 'inline-block'}),
    ],className='row'),

        html.Div(children=[
            html.Div(children=[
                dcc.Graph(figure=bar_2)
            ],className='four columns',
                style={'width': '60%', 'display': 'inline-block'}),
            html.Div(children=[
                html.Img(src=img_2)
            ],className='four columns',
                style={'width': '40%', 'display': 'inline-block'}),
        ],className='row'),

        html.Div(children=[
            html.Div(children=[
                dcc.Graph(figure=bar_3)
            ],className='four columns',
                style={'width': '60%', 'display': 'inline-block'}),
            html.Div(children=[
                html.Img(src=img_3)
            ],className='four columns',
                style={'width': '40%', 'display': 'inline-block'}),
        ],className='row'),

        html.Div(children=[
            html.Div(children=[
                dcc.Graph(figure=bar_4)
            ],className='four columns',
                style={'width': '60%', 'display': 'inline-block'}),
            html.Div(children=[
                html.Img(src=img_4)
            ],className='four columns',
                style={'width': '40%', 'display': 'inline-block'}),
        ],className='row'),

        html.Div(children=[
            html.Div(children=[
                dcc.Graph(figure=bar_5)
            ],className='four columns',
                style={'width': '60%', 'display': 'inline-block'}),
            html.Div(children=[
                html.Img(src=img_5)
            ],className='four columns',
                style={'width': '40%', 'display': 'inline-block'}),
        ],className='row'),

        html.Div(children=[
            html.Div(children=[
                dcc.Graph(figure=bar_6)
            ],className='four columns',
                style={'width': '60%', 'display': 'inline-block'}),
            html.Div(children=[
                html.Img(src=img_6)
            ],className='four columns',
                style={'width': '40%', 'display': 'inline-block'}),
        ],className='row'),

        html.Div(children=[
            html.Div(children=[
                dcc.Graph(figure=bar_7)
            ],className='four columns',
                style={'width': '60%', 'display': 'inline-block'}),
            html.Div(children=[
                html.Img(src=img_7)
            ],className='four columns',
                style={'width': '40%', 'display': 'inline-block'}),
        ],className='row'),

        html.Div(children=[
            html.Div(children=[
                dcc.Graph(figure=bar_8)
            ],className='four columns',
                style={'width': '60%', 'display': 'inline-block'}),
            html.Div(children=[
                html.Img(src=img_8)
            ],className='four columns',
                style={'width': '40%', 'display': 'inline-block'}),
        ],className='row'),

        html.Div(children=[
            html.Div(children=[
                dcc.Graph(figure=bar_9)
            ],className='four columns',
                style={'width': '60%', 'display': 'inline-block'}),
            html.Div(children=[
                html.Img(src=img_9)
            ],className='four columns',
                style={'width': '40%', 'display': 'inline-block'}),
        ],className='row'),

        html.Div(children=[
            html.Div(children=[
                dcc.Graph(figure=bar_10)
            ],className='four columns',
                style={'width': '60%', 'display': 'inline-block'}),
            html.Div(children=[
                html.Img(src=img_10)
            ],className='four columns',
                style={'width': '40%', 'display': 'inline-block'}),
        ],className='row'),

        html.Div(children=[
            html.Div(children=[
                dcc.Graph(figure=bar_11)
            ],className='four columns',
                style={'width': '60%', 'display': 'inline-block'}),
            html.Div(children=[
                html.Img(src=img_11)
            ],className='four columns',
                style={'width': '40%', 'display': 'inline-block'}),
        ],className='row'),

    ])