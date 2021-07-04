import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from app import app
from io import BytesIO
import pandas as pd
from wordcloud import WordCloud
import base64
import json

# function to make wordcoud from word frequency dataframe
def plot_wordcloud(data):
    d = {a: x for a, x in data.values}
    wc = WordCloud(background_color='white', width=480, height=360)
    wc.fit_words(d)
    return wc.to_image()

san = pd.read_csv (r'sankey\inputtopicevoldata.csv')
san_s = san['source'].tolist()
san_t = san['target'].tolist()
san_v = san['value'].tolist()
san_l = san['label'].tolist()

fig = go.Figure(go.Sankey(
    arrangement = "freeform",
    node = {
        "label": san_l,
        "x": [0.1, 0.1, 0.1, 0.1,0.1, 0.1, 0.1, 0.1,0.1,0.1,0.1,
              0.3,0.3,0.3, 0.3,0.3, 0.3, 0.3,0.3,0.3,0.3,0.3,
              0.6,0.6,0.6, 0.6,0.6, 0.6, 0.6,0.6,0.6,0.6,0.6,
              0.9,0.9,0.9, 0.9,0.9, 0.9, 0.9,0.9,0.9,0.9,0.9],
        "y": [0.1,0.2, 0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,
              0.1,0.2, 0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,
              0.1,0.2, 0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,
              0.1,0.2, 0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1],
        'thickness':50, 'pad':0},

    link = {
        "source": san_s,
        "target": san_t,
        "value": san_v

    }
    ))
fig.update_layout(
    title="Topic Evolution Plot",
    font=dict(size=15,color ='black'),
    hovermode='x',
    paper_bgcolor='#F2F4F4',
    height=700,
    clickmode='event+select'
    )
def layout():
    divBorder={
        "border": "2px solid black"
    }
    return html.Div([
        html.Div([
            html.H3('Dapper-Variant - II : Analysis and visualizations for different time periods',style={'textAlign': 'center'}),
        ], className = 'row',style={'backgroundColor': '#d2e4f7'}
        ),

        html.Div([
            dcc.Markdown('''
                * **Topic Evolution plot**: This plot depicts evolution of topics over time (2000-2020).
                * **Topic Content**: This plot gives the distribution of words in the selected topic for a selected time period.    
                ''')
        ], className='row',),

        html.Div([

            html.Div([
                # html.H3('Topic Evolution plot'),
                dcc.Graph(id = 'topic_evol',figure=fig)
            ])

        ], className = 'row',
        ),

        html.Div([
            dcc.RangeSlider(
                min=2000,
                max=2020,
                value=[2000,2005,2010,2015,2020],
                marks={
                    2000: {'label': '2000'},
                    2005: {'label': '2005'},
                    2010: {'label': '2010'},
                    2015: {'label': '2015'},
                    2020: {'label': '2020'}
                },
                included=False
            )
        ], className = 'row'),

        html.Div(children=[

            html.Div(children=[
            html.Img(id = 'image_wc1')
            ],className='four columns',
            style={'width': '40%', 'display': 'inline-block'}),

            html.Div(children=[
                dcc.Graph(id='freq_words')
            ],className='six columns',
                style={'width': '60%', 'display': 'inline-block'})
        ],className='row')
    ])

@app.callback(
    Output('image_wc1', 'src'),
    [Input('image_wc1', 'id'),
    Input('topic_evol', 'hoverData')])
def display_click_data(b,selectedData):
    x = json.dumps(selectedData)
    y = json.loads(x)
    m=y['points']
    n=json.dumps(m)
    j = json.loads(n)
    pnt_num=j[0]['pointNumber']
    filename = r"sankey\t"+str(pnt_num)+".csv"
    ff = pd.read_csv (filename)
    ff_df = pd.DataFrame(ff)
    words = ff_df['word'].tolist()
    freq = ff_df['score'].tolist()
    dfm = pd.DataFrame({'word': words, 'freq': freq})
    img = BytesIO()
    plot_wordcloud(data=dfm).save(img, format='PNG')
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())

@app.callback(
    Output('freq_words', 'figure'),
    [Input('topic_evol', 'hoverData')])
def display_click_data(selectedData):
    x = json.dumps(selectedData)
    y = json.loads(x)
    m=y['points']
    n=json.dumps(m)
    j = json.loads(n)
    pnt_num=j[0]['pointNumber']
    filename = r"sankey\t"+str(pnt_num)+".csv"
    ff = pd.read_csv (filename)
    ff_df = pd.DataFrame(ff)
    words = ff_df['word'].tolist()
    freq = ff_df['score'].tolist()
    data = go.Bar(x=words,
                  y=freq)
    layout = go.Layout(title='Word-Distribution')
    fig = go.Figure(data=data, layout=layout)

    return fig
