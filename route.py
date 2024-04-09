from fastapi import APIRouter, HTTPException, Depends
from typing import List,Optional, Annotated
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
from model import Counter


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


class CounterCreate(BaseModel):
    initial_value: int


class CounterResponse(BaseModel):
    id: int
    value: int
    

@router.post("/counter/", response_model=CounterResponse)
async def create_counter(counter_create: CounterCreate, db: db_dependency):
    if counter_create.initial_value < 0:
        raise HTTPException(status_code=400, detail="Initial value must be a non-negative integer")
    
    counter = Counter(value=counter_create.initial_value)
    db.add(counter)
    db.commit()
    db.refresh(counter)
    
    return counter


@router.patch("/counter/{counter_id}/", response_model=CounterResponse)
async def increment_counter(counter_id: int, db: db_dependency):
    with db.begin():
        counter = db.query(Counter).filter(Counter.id == counter_id).with_for_update().first()
        if not counter:
            raise HTTPException(status_code=404, detail="Counter not found")
        counter.value += 1
    return counter


@router.get("/counters/", response_model=List[CounterResponse])
async def get_counters(db: db_dependency):
    counters = db.query(Counter).all()
    return counters
