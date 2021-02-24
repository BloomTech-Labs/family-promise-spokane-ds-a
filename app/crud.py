"""
File for all our CRUD code.
Just testing viewing a specific member or family for now
"""

from datetime import date, timedelta
from sqlalchemy import and_
from sqlalchemy import Integer
from sqlalchemy.sql import func
from sqlalchemy.orm import Session
from .db_init import Members, Families

def view_member(db: Session, member_id: int):
    return db.query(Members).filter(Members.id == member_id).first()

def view_family(db: Session, family_id: int):
    return db.query(Families).filter(Families.id == family_id).first()

def exit_date_subset(*, db: Session, table = Members, today_delta = 210, start_range: int):
    today = date.today() - timedelta(days = today_delta)
    start = today - timedelta(days = start_range)
    subset = db.query(table).filter(and_(table.date_of_exit >= start, table.date_of_exit <= today)).subquery()
    return subset

def count_exits(db: Session, exit_type: str, time_range: int):
    # today = date.today() - timedelta(days=210)
    # start = today - timedelta(days = time_range)
    # date_subset = db.query(Members).filter(and_(Members.date_of_exit >= start, Members.date_of_exit <= today)).subquery()
    date_subset = exit_date_subset(db = db, start_range=time_range)
    count = db.query(func.count(date_subset.c.exit_destination)).one()[0]
    exit_subset = db.query(date_subset).filter(date_subset.c.exit_destination.like(exit_type))
    exit_count = exit_subset.count()
    return round((exit_count / count) * 100)

def avg_stay(db: Session, time_range: int):
    date_subset = exit_date_subset(db=db, start_range= time_range)
    avg = db.query(func.avg(date_subset.c.length_of_stay)).one()[0]
    return avg

def income_increase(db: Session, time_range: int):
    date_subset = exit_date_subset(db=db, start_range=time_range)
    #income = db.query(date_subset).filter(date_subset.c.demographics["income"].astext.cast(Integer) != -1)
    # date_subset.c.income_at_exit > date_subset.c.demographics["income"].astext.cast(Integer)
    income = db.query(date_subset).filter(date_subset.c.income_at_exit != -1)
    return income.count()