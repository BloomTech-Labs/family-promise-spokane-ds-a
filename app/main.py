"""
Main file for routes
"""

from fastapi import Depends, FastAPI, HTTPException, Path
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import MetaData
from sqlalchemy.orm import Session
from sqlalchemy.inspection import inspect
from .db_init import SessionLocal, engine, Members, Families
from .crud import view_family, view_member, count_exits, avg_stay, income_increase

app = FastAPI()


app.add_middleware(CORSMiddleware, allow_origins = ["*"], allow_methods = ["*"], allow_headers = ["*"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.get("/members/{member_id}")
def read_member(member_id: int = Path(..., gt = 0), db: Session = Depends(get_db)):
    db_member = view_member(db, member_id= member_id)
    if db_member is None:
        raise HTTPException(status_code = 404, detail = "Member not found in DB")
    return db_member

@app.get("/families/{family_id}")
def read_family(family_id: int = Path(..., gt= 0), db: Session = Depends(get_db)):
    db_family = view_family(db, family_id = family_id)
    if db_family is None:
        raise HTTPException(status_code= 404, detail = "Family not found in DB")
    return db_family


@app.get("/exits/{time_range}")
def all_exits(time_range: int = Path(..., gt = 0, le = 365), db: Session = Depends(get_db)):
    permanents = count_exits(db, exit_type = 'Permanent Exit', time_range= time_range)
    temps = count_exits(db, exit_type= 'Temporary Exit', time_range= time_range)
    transitionals = count_exits(db, exit_type= 'Transitional Housing', time_range= time_range)
    unknowns = count_exits(db, exit_type= 'Unknown/Other', time_range= time_range)
    emergencies = count_exits(db, exit_type= 'Emergency Shelter', time_range= time_range)
    exits = {"Permanent Exits" : permanents, "Emergency Shelter" : emergencies, "Temporary Exits" : temps, "Transitional Homes" : transitionals, "Unknown/Other" : unknowns}
    return exits

@app.get("/average_stay/{time_range}")
def average_stay(time_range: int = Path(..., gt = 0, le = 365), db: Session = Depends(get_db)):
    stay_avg = avg_stay(db, time_range = time_range) #TODO: Find out how they want the avg rounded
    avg = {"Average Stay" : stay_avg}
    return avg

@app.get("/income/{time_range}")
def view_income(time_range: int = Path(..., gt = 0, le = 365), db: Session = Depends(get_db)):
    income = income_increase(db, time_range = time_range)
    return income




# Debugging routes
#@app.get("/DBRelations")
def view_relations():
    all_relations = {"members" : [], "families" : []}
    member_relations = inspect(Members).relationships.items()
    for m in member_relations:
        all_relations["members"].append(m)
    family_relations = inspect(Families).relationships.items()
    for f in family_relations:
        all_relations["families"].append(f)
    return all_relations


if __name__ == "__main__":
    #print(view_relations())
    meta = MetaData()
    meta.reflect(bind= engine)
    print(meta.sorted_tables)