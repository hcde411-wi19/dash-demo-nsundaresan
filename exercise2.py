# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html


# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.

hours_of_day = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
"15", "16", "17", "18", "19", "20", "21", "22", "23"]
counts_in_order = [1059, 605, 471, 756, 3722, 12692, 36008, 62107, 77330, 78947, 84650,
87067, 87075, 86720, 88931, 95320, 108873, 110013, 81305, 45572, 21963, 8818, 3971, 2079]

# initialize Dash environment
app = dash.Dash(__name__)

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='Exercise #2'),

    # a div to put a short description
    html.Div(children='''
        Line graph for usage of BGT North per hours of the day. Hours are in military time.
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # set x to be weekday, and y to be the counts. We use bars to represent our data.
                {'x': hours_of_day, 'y': counts_in_order, 'type': 'line', 'name': 'Total'},

            ],
            # configure the layout of the visualization --
            # set the title to be "Usage of the BGT North of NE 70th per week day"
            'layout': {
                'title': 'Usage of the BGT North of NE 70th per hour of the day'
            }
        }
    )
])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)
