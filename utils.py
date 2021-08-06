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
                        src="data:image/jpeg;base64,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",
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
               href="/Visualization/Overview",
               className='tab first'
           ),
            dcc.Link(
                "Data Visualization",
                href="/Visualization/Sankey",
                className='tab'
            ),
            dcc.Link(
                "SVA Research",
                href="/Visualization/SVA_Research",
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
