import pandas as pd
import plotly.graph_objects as go
from datetime import date, timedelta
from sqlalchemy.orm import Session

from .crud import exit_date_subset

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