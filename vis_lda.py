
import dash_core_components as dcc

import dash_html_components as html

from app import app



def layout():
    return html.Div(children=[
        html.Div([
            html.H3('Latent Dirichlet Allocation',style={'textAlign': 'center'}),
        ], className = 'row',style={'backgroundColor': '#d2e4f7'}
        ),
        html.Div([
            dcc.Markdown('''
                * **Visualizaton**: The plot here consists of topics depicted by circular nodes and on clicking on a node, the corresponding determinant words can be seen in the right side part in the plot..                     
                ''')
        ], className='row',),

        html.Iframe(src=app.get_asset_url('lda.html'),
                    style=dict(position="absolute",  width="90%", height="100%"))
        ])