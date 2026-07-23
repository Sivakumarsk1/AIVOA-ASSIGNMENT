from sqlalchemy.orm import Session
from app.models.complaint import Complaint
from app.schemas.complaint import ComplaintCreate, ComplaintUpdate
import random

def generate_complaint_number(db: Session) -> str:
    while True:
        num = random.randint(10000, 99999)
        complaint_number = f"CC-2026-{num}"
        existing = db.query(Complaint).filter(Complaint.complaint_number == complaint_number).first()
        if not existing:
            return complaint_number

def get_complaint(db: Session, complaint_id: int):
    return db.query(Complaint).filter(Complaint.id == complaint_id).first()

def get_complaints(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Complaint).offset(skip).limit(limit).all()

def create_complaint(db: Session, complaint: ComplaintCreate):
    complaint_number = generate_complaint_number(db)
    db_complaint = Complaint(**complaint.model_dump(), complaint_number=complaint_number)
    db.add(db_complaint)
    db.commit()
    db.refresh(db_complaint)
    return db_complaint

def update_complaint(db: Session, complaint_id: int, complaint: ComplaintUpdate):
    db_complaint = get_complaint(db, complaint_id)
    if db_complaint:
        update_data = complaint.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_complaint, key, value)
        db.commit()
        db.refresh(db_complaint)
    return db_complaint

def delete_complaint(db: Session, complaint_id: int):
    db_complaint = get_complaint(db, complaint_id)
    if db_complaint:
        db.delete(db_complaint)
        db.commit()
        return True
    return False
