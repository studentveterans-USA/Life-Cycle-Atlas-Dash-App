import dash
import dash_core_components as dcc
import dash_html_components as html


################################ Banner ##################################

def Header(app):
    return html.Div([get_header(app), html.Br([]),html.Br([]),html.Br([]),html.Br([]), get_menu()])

def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        #src="https://cdn.mmaweekly.com/wp-content/uploads/2017/10/UFC-black-logo-on-gradient.jpg",
                        #src="https://www.stripes.com/polopoly_fs/1.175627.1335454273!/image/3107706660.jpg_gen/derivatives/landscape_900/3107706660.jpg",
                        src = "Visualization/SVA.png",
                        
                        className='SVA_img'
                    ),
                    #html.Img(
                        #src="https://www.usveteransmagazine.com/wp-content/uploads/2017/04/pwc_charitablefoundation_logo.png",
                        #src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTjEFX1cPTepX0y5gq6csK8JFC-z2Xk-v8lkXuGSyG1EwLJsUdm&s',
                        #className='PWC_img'
                    #),
                ],
                className='row',
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Student Veterans of America Life Cycle Atlas")],
                        className="seven columns main-title",
                        style={'font-weight': 'bold'},
                    ),
                    html.Div(
                        [
                            html.A(
                                html.Button("Learn More", id="learn-more-button"),
                                href="https://atlas.studentveterans.org/"
                            )

                        ],
                        className='five columns',
                    ),
                ],
                className="twelve columns",
                style={"padding-left":"0"},
            ),
        ],
        className='row',
    )
    return header


################################ Banner Menu ##################################
def get_menu():
    menu = html.Div(
        [
           dcc.Link(
               'Overview',
               href="/Heroku_Deployment_v2/Visualization/Overview",
               className='tab first'
           ),
            dcc.Link(
                "Data Visualization",
                href="/Heroku_Deployment_v2/Visualization/Sankey",
                className='tab'
            ),
            dcc.Link(
                "SVA Research",
                href="/Heroku_Deployment_v2/Visualization/SVA_Research",
                className='tab'
            ),
        ],
        className='row all-tabs',
    )
    return menu

def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
