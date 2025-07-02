from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
import database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="ASUU Legislation Tracker API")

@app.get("/legislation", response_model=list[schemas.Legislation])
def list_legislation(db: Session = Depends(database.get_db)):
    return db.query(models.Legislation).order_by(models.Legislation.introduced_date.desc()).all()

@app.get("/legislation/{item_id}", response_model=schemas.Legislation)
def get_legislation(item_id: int, db: Session = Depends(database.get_db)):
    item = db.query(models.Legislation).get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Legislation not found")
    return item

@app.post("/legislation", response_model=schemas.Legislation, status_code=201)
def create_legislation(data: schemas.LegislationCreate, db: Session = Depends(database.get_db)):
    new_item = models.Legislation(**data.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@app.put("/legislation/{item_id}", response_model=schemas.Legislation)
def update_legislation(item_id: int, data: schemas.LegislationUpdate, db: Session = Depends(database.get_db)):
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
