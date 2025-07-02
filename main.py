from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy import or_
from sqlalchemy.orm import Session

import database
import models
import schemas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="ASUU Legislation Tracker API")


@app.get("/legislation", response_model=list[schemas.Legislation])
def list_legislation(
    *,
    q: str | None = Query(default=None, description="Search text"),
    type: str | None = Query(default=None, description="Filter by type"),
    status: str | None = Query(default=None, description="Filter by status"),
    db: Session = Depends(database.get_db),
):
    query = db.query(models.Legislation)
    if q:
        like = f"%{q}%"
        query = query.filter(
            or_(
                models.Legislation.title.ilike(like),
                models.Legislation.summary.ilike(like),
            )
        )
    if type:
        query = query.filter(models.Legislation.type == type)
    if status:
        query = query.filter(models.Legislation.status == status)
    return query.order_by(models.Legislation.introduced_date.desc()).all()


@app.get("/legislation/senate", response_model=list[schemas.Legislation])
def list_senate_legislation(
    q: str | None = Query(default=None, description="Search text"),
    status: str | None = Query(default=None, description="Filter by status"),
    db: Session = Depends(database.get_db),
):
    return list_legislation(q=q, type="Senate", status=status, db=db)


@app.get("/legislation/assembly", response_model=list[schemas.Legislation])
def list_assembly_legislation(
    q: str | None = Query(default=None, description="Search text"),
    status: str | None = Query(default=None, description="Filter by status"),
    db: Session = Depends(database.get_db),
):
    return list_legislation(q=q, type="Assembly", status=status, db=db)


@app.get("/legislation/joint", response_model=list[schemas.Legislation])
def list_joint_legislation(
    q: str | None = Query(default=None, description="Search text"),
    status: str | None = Query(default=None, description="Filter by status"),
    db: Session = Depends(database.get_db),
):
    return list_legislation(q=q, type="Joint", status=status, db=db)


@app.get("/legislation/{item_id}", response_model=schemas.Legislation)
def get_legislation(item_id: int, db: Session = Depends(database.get_db)):
    item = db.query(models.Legislation).get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Legislation not found")
    return item


@app.post("/legislation", response_model=schemas.Legislation, status_code=201)
def create_legislation(
    data: schemas.LegislationCreate, db: Session = Depends(database.get_db)
):
    new_item = models.Legislation(**data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@app.put("/legislation/{item_id}", response_model=schemas.Legislation)
def update_legislation(
    item_id: int,
    data: schemas.LegislationUpdate,
    db: Session = Depends(database.get_db),
):
    item = db.query(models.Legislation).get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Legislation not found")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


@app.delete("/legislation/{item_id}", status_code=204)
def delete_legislation(item_id: int, db: Session = Depends(database.get_db)):
    item = db.query(models.Legislation).get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Legislation not found")
    db.delete(item)
    db.commit()
    return
