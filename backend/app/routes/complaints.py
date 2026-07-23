from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.complaint import ComplaintCreate, ComplaintUpdate, ComplaintResponse
from app.services import complaint_service

router = APIRouter(prefix="/api/complaints", tags=["complaints"])

@router.post("/", response_model=ComplaintResponse)
def create_complaint(complaint: ComplaintCreate, db: Session = Depends(get_db)):
    return complaint_service.create_complaint(db, complaint)

@router.get("/", response_model=List[ComplaintResponse])
def list_complaints(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return complaint_service.get_complaints(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=ComplaintResponse)
def get_complaint(id: int, db: Session = Depends(get_db)):
    db_complaint = complaint_service.get_complaint(db, id)
    if not db_complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")
    return db_complaint

@router.put("/{id}", response_model=ComplaintResponse)
def update_complaint(id: int, complaint: ComplaintUpdate, db: Session = Depends(get_db)):
    db_complaint = complaint_service.update_complaint(db, id, complaint)
    if not db_complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")
    return db_complaint

@router.delete("/{id}")
def delete_complaint(id: int, db: Session = Depends(get_db)):
    success = complaint_service.delete_complaint(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="Complaint not found")
    return {"message": "Complaint deleted successfully"}
