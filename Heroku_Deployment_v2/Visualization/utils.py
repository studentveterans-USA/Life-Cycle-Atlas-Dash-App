import dash
import dash_core_components as dcc
import dash_html_components as html


################################ Banner ##################################

def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])

def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        #src="https://cdn.mmaweekly.com/wp-content/uploads/2017/10/UFC-black-logo-on-gradient.jpg",
                        #src="https://www.stripes.com/polopoly_fs/1.175627.1335454273!/image/3107706660.jpg_gen/derivatives/landscape_900/3107706660.jpg",
                        src = "data:image/png;base64,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"
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
                        [html.H5("Student Veterans of America -- Life Cycle Atlas")],
                        className="seven columns main-title",
                        style={'font-weight':'bold'},
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "MORE INFO",
                                href="https://atlas.studentveterans.org/",
                                className='full-view-link'
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
               'Home',
               href="/Heroku_Deployment_v2/Visualization/Home",
               className='tab first'
           ),
            dcc.Link(
                "Data Visualization",
                href="/Heroku_Deployment_v2/Visualization/Sankey",
                className='tab'
            ),
            dcc.Link(
                "About Me",
                href="/Capstone_Fall19/Visualization/About_Project",
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
