import dash
import dash_core_components as dcc

import plotly.graph_objects as go

from dash.dependencies import Input, Output,State
from app import app
import numpy as np

import json
from io import BytesIO
import pandas as pd
from wordcloud import WordCloud
import base64
import dash_cytoscape as cyto
import dash_html_components as html
from sklearn.manifold import TSNE
from gensim.models import AuthorTopicModel


# temp_file = datapath("C:/Users/Subhashree/Documents/KMD_Thesis/Data Final/ATM/model")
#temp_file = datapath("C:/Users/Subhashree/Documents/KMD_Thesis/Complete Code Collection/Author Topic Model/model")
# Load a potentially pretrained model from disk.
model = AuthorTopicModel.load("model")

tsne = TSNE(n_components=2, random_state=0)
smallest_author = 5  # Ignore authors with documents less than this.
authors = [model.author2id[a] for a in model.author2id.keys() if len(model.author2doc[a]) >= smallest_author]
_ = tsne.fit_transform(model.state.gamma[authors, :])  # Result stored in tsne.embedding_

author_names = [model.id2author[a] for a in authors]
author_sizes = [len(model.author2doc[a]) for a in author_names]
author_top_names = pd.DataFrame()
author_top_names['Names'] = author_names
author_top_names['sizes'] = author_sizes
author_top_names=author_top_names.sort_values(by='sizes', ascending=False)
author_top_names = author_top_names.head(100)
topic_labels = ['Topic 0', 'Topic 1', 'Topic 2', 'Topic 3',
                'Topic 4', 'Topic 5', 'Topic 6',
                'Topic 7', 'Topic 8', 'Topic 9', 'Topic 10']

def show_author(name):
    print('\n%s' % name)
    print('Docs:', model.author2doc[name])
    print('Topics:')
    print([(topic_labels[topic[0]], topic[1]) for topic in model[name]])

mark_r=['0','5','10','15','20']
mark_y=['0','5','10','15','20','25','30','35','40']
mark_g=['0','5','10','15','20','25','30','35','40','45','50','55','60']

def plot_wordcloud(data):
    d = {a: x for a, x in data.values}
    wc = WordCloud(background_color='white', width=500, height=350)
    wc.fit_words(d)
    return wc.to_image()
# Element of network
# -------------------------------------------
# df = pd.read_csv (r'C:\Users\Subhashree\Documents\KMD_Thesis\Data Final\ATM\ATMv2_filtered_data\top500similar\Result_Atm.csv')
df = pd.read_csv (r'ATM\Result_Atm.csv')
# source = df['Source_auth'].unique()
# target = df['Target_auth'].unique()
# arr = np.concatenate((source, target))
# arr = set(arr)
degrees= dict([(i,s) for i,s in zip(df.Target_auth, df.Size)])

ele = set()
for i in df.iterrows():
    ele.add((i[1]['Source_auth'],i[1]['Target_auth'],i[1]['Score'],i[1]['Common']))

nodes = [
    {
        'data': {'id': s, 'label': s, 'size':degrees[s]},
        'position': {'x': 20, 'y': -20}
    }
    for s in (degrees)
]

edges = [
    {'data': {'source': source, 'target': target,'width':score*2,'weight':common}}
    for source, target,score,common in (ele)
]

default_stylesheet = [
    {
        'selector': 'node',
        'style': {
            # 'background-color': '#BFD7B5',

            'label': 'data(label)',
            "width": "mapData(size, 0, 170, 10,200)",
            "height": "mapData(size, 0, 170,10,200)",
            'background-color':'F7DC6F', #'#5D6D7E', #F7DC6F,#2722AF',
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

elements = nodes + edges
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
# -------------------------------------------
def layout():
    return html.Div(children=[
        html.Div([
            html.H3('Author Topic Model : Analysis and visualizations for author similarity, co-authorship links etc.',style={'textAlign': 'center'}),
        ], className = 'row',style={'backgroundColor': '#d2e4f7'}
        ),
        html.Div([
            dcc.Markdown('''
                * **Cytoscape Network Graph**: This is a author similarity network plot. The nodes are the authors, 
                the edges from a node connect to the similar authors. The size of the node is proportional to the number of publications by the author.
                * Co-authorship Links: This is depicted by the color of the egde between two nodes.
                * Red: Co-aothored very few ( 0-2 )
                * Blue: Co-authored moderartely ( 3-15 )
                * Green: Co-authored largly ( >15 )
                * **Topic Distribution Donut Chart:** On clicking on a node, the donut chart shows the interest distribution of the selected author.
                * **Topic Content Word Cloud**: On clicking a topic on the donut chart, the top words consisting the topic is displayed in the form of a word cloud                      
                ''')
        ], className='row',),

        html.Div(children=[

            html.Div(children=[

                html.Div([
                    html.H4('Select the network layout'),
                    dcc.Dropdown(
                        id='dropdown-update-layout',
                        value='cose',
                        clearable=False,
                        options=[
                            {'label': name.capitalize(), 'value': name}
                            for name in ['grid', 'random', 'circle', 'cose', 'concentric']
                        ]
                    )
                ],className='two columns',
                    style={'width': '25%', 'display': 'inline-block'}),


        ],className='row',
          style={'borderBottom': 'thin lightgrey solid',
                 'backgroundColor': 'rgb(250, 250, 250)'}),

        html.Div(children=[
            cyto.Cytoscape(
                id='cytoscape-atm-nodes',
                stylesheet=default_stylesheet +new_styles,
                layout={'name': 'cose'},
                style={'width': '1500px','height':'1000px'},
                elements=elements
            )
        ],className='row',
          style={'borderBottom': 'thin lightgrey solid'}),

        ],className='row'),

        html.Div(children=[
            html.Div(children=[
                dcc.Graph(id='donut')
            ],style={'width': '30%', 'display': 'inline-block'},
                className= 'three columns'),

            html.Div(children=[
                html.Img(id="image_wc"),
                html.Div(id='dd-output-container')
            ],className='three columns',
                style={'width': '60%', 'display': 'inline-block'})

        ],className='row')


    ])

@app.callback(Output('cytoscape-atm-nodes', 'layout'),
              Input('dropdown-update-layout', 'value'))
def update_layout(layout):
    return {
        'name': layout,
        'animate': True
    }

@app.callback(
    dash.dependencies.Output('donut', 'figure'),
    [Input('cytoscape-atm-nodes', 'tapNodeData')])
def update_output(data):
    value=data['id']
    # print(value)
    df2 = pd.DataFrame(np.array([(topic_labels[topic[0]], topic[1]) for topic in model[value]]),
                       columns=['Topic_Name', 'Distribution'])
    res=[]
    for i in range(0,11):
        name = 'Topic '+ str(i)
        if name not in df2.values:
            res.append([name,''])
        else:
            res.append([name,float(df2.loc[df2['Topic_Name'] == name]['Distribution'].values[0])])
    resdf = pd.DataFrame(res, columns = ['Topic_Name', 'Distribution'])
    labels=resdf['Topic_Name']
    traces=[]
    traces.append(
        go.Pie(
            labels=labels,
            # values=df2['Distribution'],
            values=resdf['Distribution'],
            name=value,hole=.4,
            marker={'colors':['#C0392B', '#E74C3C', '#9B59B6', '#2980B9', '#16A085', '#F1C40F', '#E59866', '#0B5345', '#D2B4DE', '#F39C12','#5D6D7E']},
            hoverinfo="label+percent"
    )
                  )
    return {
        'data':traces,
        'layout':go.Layout(
            title_text="Interest distribution of author over topics",
            annotations=[dict(text=value, x=0.18, y=0.5, font_size=13, showarrow=False)]
        )
    }

@app.callback(dash.dependencies.Output('image_wc', 'src'),
              [dash.dependencies.Input('image_wc', 'id'),
               dash.dependencies.Input('donut','clickData')])
def make_image(b,clk_data):
    print(clk_data)
    x = json.dumps(clk_data)
    y = json.loads(x)
    m=y['points']
    n=json.dumps(m)
    j = json.loads(n)
    topic_lbl=j[0]['label']
    print(topic_lbl)
    # topic_wc = datapath("C:/Users/Subhashree/Documents/KMD_Thesis/Data Final/ATM/ATMv2_filtered_data/"+topic_lbl+".csv")
    #topic_wc = datapath(topic_lbl+".csv")
    ff = pd.read_csv ("ATM\\"+topic_lbl+".csv")
    ff_df = pd.DataFrame(ff)
    words = ff_df['word'].tolist()
    freq = ff_df['score'].tolist()
    dfm = pd.DataFrame({'word': words, 'freq': freq})
    img = BytesIO()
    plot_wordcloud(data=dfm).save(img, format='PNG')
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())