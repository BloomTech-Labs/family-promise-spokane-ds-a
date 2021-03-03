import pandas as pd
import plotly.graph_objects as go
from datetime import date, timedelta
from sqlalchemy.orm import Session

from .crud import exit_date_subset, count_exits, today

def pie_exits(db: Session, time_range: int):
    date_subset = exit_date_subset(db=db, start_range=time_range)
    query = db.query(date_subset.c.exit_destination)
    df = pd.read_sql(query.statement, query.session.bind)
    exits = ['Unkown/Other', 'Permanent Exit', 'Emergency Shelter', 'Temporary Exit', 'Transitional Housing']
    # Make the plot of exit type to count of people to show how they are exiting
    fig = go.Figure([go.Pie(labels=exits, values=df['exit_destination'].value_counts())])
    fig.update_layout(
        title={
            'text': "Exit Destinations",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
            xaxis_title="Exit Type",
            yaxis_title='Number of People')

    return fig.to_json()


def moving_average(db: Session, time_range: int):
    exits = ["Unknown/Other", "Permanent Exit", "Emergency Shelter", "Temporary Exit", "Transitional Housing"]
    daterange = pd.date_range(today - timedelta(days = time_range), today)
    averages_dict = {"Permanent Exit" : [], "Emergency Shelter" : [], "Temporary Exit" : [], "Transitional Housing" : [], "Unknown/Other" : []}
    a = [5,|6,7,8,8,1,2|,3,4,5]
    for exit_type in exits:
        for day in daterange:
            avg = count_exits(db= db, exit_type= exit_type, time_range= 90, stop= day)
            averages_dict[exit_type].append(avg)

    # all_
    # for exit_type in exits:

    averages_dict.update({"Days" : daterange})
    avg_df = pd.DataFrame(averages_dict)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=avg_df["Days"],
        y=avg_df["Permanent Exit"],
        mode = "lines",
        name="Permanent Exit",
        marker_color="#EF553B"
    ))
    fig.add_trace(go.Scatter(
        x=avg_df["Days"],
        y=avg_df["Emergency Shelter"],
        mode = "lines",
        name="Emergency Shelter",
        marker_color="#00CC96"
    ))
    fig.add_trace(go.Scatter(
        x=avg_df["Days"],
        y=avg_df["Temporary Exit"],
        mode = "lines",
        name="Temporary Exit",
        marker_color="#AB63FA"
    ))
    fig.add_trace(go.Scatter(
        x=avg_df["Days"],
        y=avg_df["Transitional Housing"],
        mode = "lines",
        name="Transitional Housing",
        marker_color="#FFA15A"
    ))
    fig.add_trace(go.Scatter(
        x=avg_df["Days"],
        y=avg_df["Unknown/Other"],
        mode = "lines",
        name="Unknown/Other",
        marker_color="#636EFA"
    ))

    fig.update_layout(
        title="90 Day Exit Moving Averages",
        xaxis = dict(
            tickfont_size = 14,
            #tickangle = -45
        ),
        yaxis=dict(
            title="Percentages",
            titlefont_size=16,
            #tickfont_size=14,
        ),
    )

    return fig.to_json()