import dash

import dash_core_components as dcc

import dash_html_components as html
import pandas as pd
import plotly.graph_objects as go

from dash.dependencies import Input, Output
from app import app

import json
#import file of persona evolution
df = pd.read_csv (r'DAPPER_per_evol\persona_topic.csv')
drop_optn = ['Persona0', 'Persona1', 'Persona2', 'Persona3']
coloroptn=['#C62828', '#AD1457', '#6A1B9A','#4527A0','#283593','#1565C0','#0277BD','#00838F','#00695C','#2E7D32','#558B2F']
def layout():
    return html.Div(children=[
        html.Div([
            html.H3('Dapper-Variant - I : Analysis and visualizations for time period 2000-2020 (static topics)',style={'textAlign': 'center'}),
        ], className = 'row',style={'backgroundColor': '#d2e4f7'}
        ),
        html.Div([
            dcc.Markdown('''
                * **Persona Evolution Plot**: This plot shows the evolution of the selected persona for all the topics over the time period.                     
                ''')
        ], className='row',),
        html.Div([

            html.Div([

                dcc.Dropdown(
                    id='demo-dropdown',
                    value='Persona0',
                    options=[{'label': i, 'value': i} for i in drop_optn]
                ),

            ],style={'width': '30%', 'height':'30%', 'display': 'inline-block'})

        ],style={
            'borderBottom': 'thin lightgrey solid',
            'backgroundColor': 'rgb(250, 250, 250)',
            'padding': '10px 5px'
        }),
        html.Div([
            dcc.Graph(
                id='persona-evol-scatter'
            )
        ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),

        html.Div(children=[
            dcc.Graph(id='topic_dist_bar')
        ]),
    ])

@app.callback(
    Output('topic_dist_bar', 'figure'),
    [Input('demo-dropdown', 'value')])
def dist_dap_topic(value):
    if( value == 'Persona0'):
        df_persona=df[df.persona == 0]
    elif( value == 'Persona1'):
        df_persona=df[df.persona == 1]
    elif( value == 'Persona2'):
        df_persona=df[df.persona == 2]
    elif( value == 'Persona3'):
        df_persona=df[df.persona == 3]
    traces=[]
    df_persona.sort_values(by=['time'])
    for i in range(0,11):
        ld_str = 'topic'+ str(i)
        traces.append(
            go.Bar(
                x=df_persona['time'],
                y=df_persona[ld_str],
                name=ld_str,
                opacity=0.7,
                marker_line_color='rgb(8,48,107)',
                marker_line_width=2
            ))
    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={
                'title': 'Time slice in years',
                'type': 'linear'

            },
            yaxis={
                'title': 'Distribution over topics',
                'type': 'linear'

            },
            title='Visualisation of Topics Distribution',
            barmode='stack',
            colorway=['#C62828', '#AD1457', '#6A1B9A','#4527A0','#283593','#1565C0','#0277BD','#00838F','#00695C','#2E7D32','#558B2F']#,'#9E9D24','#F9A825','#FF8F00','#EF6C00','#D84315','#4E342E','#424242','#37474F','#000000']

        )
    }

@app.callback(
    dash.dependencies.Output('persona-evol-scatter', 'figure'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_persona_evol_scatter(value):
    traces=[]
    topics=['topic0','topic1','topic2','topic3','topic4','topic5','topic6','topic7','topic8','topic9','topic10']
    colors=['#C62828', '#AD1457', '#6A1B9A','#4527A0','#283593','#1565C0','#0277BD','#00838F','#00695C','#2E7D32','#558B2F']
    if(value == 'Persona0'):
        df_0 = df[df['persona']==0]
        for i,j in zip(topics,colors):

                traces.append(
                    go.Scatter(
                        fill= 'tonexty',
                        # line = dict(shape = 'spline',
                        #             width = 0),
                        line=dict(width=3,shape = 'spline'),
                        name= i,
                        type= 'scatter',
                        x= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'],
                        y= df_0[i],
                        # fillcolor= j,
                        opacity=1,
                        mode='lines',
                        line_color=j,
                        # stackgroup='one',
                        marker=dict(size = 15)

                        )
                     )
    elif (value == 'Persona1'):
        df_1 = df[df['persona']==1]
        for i,j in zip(topics,colors):
            traces.append(
                go.Scatter(
                    fill= 'tonexty',
                    # line = dict(shape = 'spline',
                    #             width = 0),
                    line=dict(width=3,shape = 'spline'),
                    name= i,
                    type= 'scatter',
                    x= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'],
                    y= df_1[i],
                    # fillcolor= j,
                    opacity=1,
                    mode='lines',
                    line_color=j,
                    # stackgroup='one',
                    marker=dict(size = 15)

                )
            )

    elif (value == 'Persona2'):

        df_2 = df[df['persona']==2]
        for i,j in zip(topics,colors):
            traces.append(
                go.Scatter(
                    fill= 'tonexty',
                    # line = dict(shape = 'spline',
                    #             width = 0),
                    line=dict(width=3,shape = 'spline'),
                    name= i,
                    type= 'scatter',
                    x= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'],
                    y= df_2[i],
                    # fillcolor= j,
                    opacity=1,
                    mode='lines',
                    line_color=j,
                    # stackgroup='one',
                    marker=dict(size = 15)

                )
            )

    elif (value == 'Persona3'):
        df_3 = df[df['persona']==3]
        for i,j in zip(topics,colors):
            traces.append(
                go.Scatter(
                    fill= 'tonexty',
                    # line = dict(shape = 'spline',
                    #             width = 0),
                    line=dict(width=3,shape = 'spline'),
                    name= i,
                    type= 'scatter',
                    x= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'],
                    y= df_3[i],
                    # fillcolor= j,
                    opacity=1,
                    mode='lines',
                    line_color=j,
                    # stackgroup='one',
                    marker=dict(size = 15)

                )
            )

    elif (value == 'Persona4'):

        df_4 = df[df['persona']==4]
        for i,j in zip(topics,colors):
            traces.append(
                go.Scatter(
                    fill= 'tonexty',
                    # line = dict(shape = 'spline',
                    #             width = 0),
                    line=dict(width=3,shape = 'spline'),
                    name= i,
                    type= 'scatter',
                    x= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'],
                    y= df_4[i],
                    # fillcolor= j,
                    opacity=1,
                    mode='lines',
                    line_color=j,
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
                                    'title': 'Distribution over Topics',
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
    dash.dependencies.Output("persona-evol-scatter", "data"),
    [dash.dependencies.Input("persona-evol-scatter", "clickData"),
     dash.dependencies.Input('demo-dropdown', 'value')]
)
def highlight_trace_persona(clickData,value):
    traces=[]
    selected_topic = json.loads(json.dumps(json.loads(json.dumps(clickData))['points']))[0]['curveNumber']
    topics=['topic0','topic1','topic2','topic3','topic4','topic5','topic6','topic7','topic8','topic9','topic10']
    indexx=[0,1,2,3,4,5,6,7,8,9,10]
    colors=['#C62828', '#AD1457', '#6A1B9A','#4527A0','#283593','#1565C0','#0277BD','#00838F','#00695C','#2E7D32','#558B2F']
    if(value == 'Persona0'):
        df_0 = df[df['persona']==0]
        for i,j,k in zip(topics,colors,indexx):
            if k == selected_topic:
                traces.append(
                    go.Scatter(
                        fill= 'tonexty',
                        # line = dict(shape = 'spline',
                        #             width = 0),
                        line=dict(width=15,shape = 'spline'),
                        name= i,
                        type= 'scatter',
                        x= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'],
                        y= df_0[i],
                        # fillcolor= j,
                        opacity=1,
                        mode='lines',
                        line_color=j,
                        # stackgroup='one',
                        marker=dict(size = 15)
                    )
                )
            else:
                traces.append(
                    go.Scatter(
                        fill= 'tonexty',
                        # line = dict(shape = 'spline',
                        #             width = 0),
                        line=dict(width=1,shape = 'spline'),
                        name= i,
                        type= 'scatter',
                        x= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'],
                        y= df_0[i],
                        # fillcolor= j,
                        opacity=0.001,
                        mode='lines',
                        line_color=j,
                        # stackgroup='one',
                        marker=dict(size = 15)
                    )
                )

    elif (value == 'Persona1'):
        df_1 = df[df['persona']==1]
        for i,j,k in zip(topics,colors,indexx):
            if k == selected_topic:
                traces.append(
                    go.Scatter(
                        fill= 'tonexty',
                        # line = dict(shape = 'spline',
                        #             width = 0),
                        line=dict(width=15,shape = 'spline'),
                        name= i,
                        type= 'scatter',
                        x= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'],
                        y= df_1[i],
                        # fillcolor= j,
                        opacity=1,
                        mode='lines',
                        line_color=j,
                        # stackgroup='one',
                        marker=dict(size = 15)
                    )
                )
            else:
                traces.append(
                    go.Scatter(
                        fill= 'tonexty',
                        # line = dict(shape = 'spline',
                        #             width = 0),
                        line=dict(width=1,shape = 'spline'),
                        name= i,
                        type= 'scatter',
                        x= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'],
                        y= df_1[i],
                        # fillcolor= j,
                        opacity=0.001,
                        mode='lines',
                        line_color=j,
                        # stackgroup='one',
                        marker=dict(size = 15)
                    )
                )

    elif (value == 'Persona2'):

        df_2 = df[df['persona']==2]
        for i,j,k in zip(topics,colors,indexx):
            if k == selected_topic:
                traces.append(
                    go.Scatter(
                        fill= 'tonexty',
                        # line = dict(shape = 'spline',
                        #             width = 0),
                        line=dict(width=15,shape = 'spline'),
                        name= i,
                        type= 'scatter',
                        x= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'],
                        y= df_2[i],
                        # fillcolor= j,
                        opacity=1,
                        mode='lines',
                        line_color=j,
                        # stackgroup='one',
                        marker=dict(size = 15)
                    )
                )
            else:
                traces.append(
                    go.Scatter(
                        fill= 'tonexty',
                        # line = dict(shape = 'spline',
                        #             width = 0),
                        line=dict(width=1,shape = 'spline'),
                        name= i,
                        type= 'scatter',
                        x= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'],
                        y= df_2[i],
                        # fillcolor= j,
                        opacity=0.001,
                        mode='lines',
                        line_color=j,
                        # stackgroup='one',
                        marker=dict(size = 15)
                    )
                )

    elif (value == 'Persona3'):
        df_3 = df[df['persona']==3]
        for i,j,k in zip(topics,colors,indexx):
            if k == selected_topic:
                traces.append(
                    go.Scatter(
                        fill= 'tonexty',
                        # line = dict(shape = 'spline',
                        #             width = 0),
                        line=dict(width=15,shape = 'spline'),
                        name= i,
                        type= 'scatter',
                        x= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'],
                        y= df_3[i],
                        # fillcolor= j,
                        opacity=1,
                        mode='lines',
                        line_color=j,
                        # stackgroup='one',
                        marker=dict(size = 15)
                    )
                )
            else:
                traces.append(
                    go.Scatter(
                        fill= 'tonexty',
                        # line = dict(shape = 'spline',
                        #             width = 0),
                        line=dict(width=1,shape = 'spline'),
                        name= i,
                        type= 'scatter',
                        x= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'],
                        y= df_3[i],
                        # fillcolor= j,
                        opacity=0.001,
                        mode='lines',
                        line_color=j,
                        # stackgroup='one',
                        marker=dict(size = 15)
                    )
                )

    elif (value == 'Persona4'):

        df_4 = df[df['persona']==4]
        for i,j,k in zip(topics,colors,indexx):
            if k == selected_topic:
                traces.append(
                    go.Scatter(
                        fill= 'tonexty',
                        # line = dict(shape = 'spline',
                        #             width = 0),
                        line=dict(width=15,shape = 'spline'),
                        name= i,
                        type= 'scatter',
                        x= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'],
                        y= df_4[i],
                        # fillcolor= j,
                        opacity=1,
                        mode='lines',
                        line_color=j,
                        # stackgroup='one',
                        marker=dict(size = 15)
                    )
                )
            else:
                traces.append(
                    go.Scatter(
                        fill= 'tonexty',
                        # line = dict(shape = 'spline',
                        #             width = 0),
                        line=dict(width=1,shape = 'spline'),
                        name= i,
                        type= 'scatter',
                        x= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020'],
                        y= df_4[i],
                        # fillcolor= j,
                        opacity=0.001,
                        mode='lines',
                        line_color=j,
                        # stackgroup='one',
                        marker=dict(size = 15)
                    )
                )
    return traces
    # return {
    #     'data': traces,
    #     'layout': go.Layout(
    #         font= {'family': 'Balto'},
    #         title= 'Streamgraph with ThemeRiver layout',
    #         width= 1400,
    #         xaxis= {
    #             'mirror': True,
    #             'ticklen': 4,
    #             'showgrid': False,
    #             'showline': True,
    #             'tickfont': {'size': 11},
    #             'zeroline': False,
    #             'showticklabels': True,
    #             'title': 'Time slice in years',
    #             'type': 'linear'
    #         },
    #         yaxis= {
    #             'mirror': True,
    #             'ticklen': 4,
    #             'showgrid': False,
    #             'showline': True,
    #             'tickfont': {'size': 11},
    #             'zeroline': False,
    #             'showticklabels': True,
    #             'title': 'Distribution over Topics',
    #             'type': 'linear'
    #         },
    #         height= 460,
    #         margin= {
    #             'b': 60,
    #             'l': 60,
    #             'r': 60,
    #             't': 80
    #         },
    #         hovermode='closest',
    #         clickmode='event+select'
    #
    #     )
    #
    # }
