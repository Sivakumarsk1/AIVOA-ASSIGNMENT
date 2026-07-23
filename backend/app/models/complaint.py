from sqlalchemy import Column, Integer, String, Text, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    complaint_number = Column(String, unique=True, index=True)
    status = Column(String, default="Pending Triage")
    complaint_source = Column(String)
    customer_name = Column(String)
    product_name = Column(String)
    product_strength_grade = Column(String)
    batch_lot_number = Column(String)
    manufacturing_date = Column(String, nullable=True)
    expiry_date = Column(String, nullable=True)
    quantity_affected = Column(String, nullable=True)
    quantity_unit = Column(String, default="kg")
    complaint_type = Column(String)
    complaint_date = Column(String, nullable=True)
    detailed_description = Column(Text)
    initial_severity = Column(String)
    priority = Column(String)
    ai_risk_classification = Column(String, nullable=True)
    ai_summary = Column(Text, nullable=True)
    ai_root_cause = Column(Text, nullable=True)
    ai_capa_recommendation = Column(Text, nullable=True)
    ai_completeness_score = Column(Float, nullable=True)
    is_duplicate = Column(Boolean, default=False)
    duplicate_of_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    documents = relationship("ComplaintDocument", back_populates="complaint")
    messages = relationship("AIChatMessage", back_populates="complaint")


class ComplaintDocument(Base):
    __tablename__ = "complaint_documents"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    complaint_id = Column(Integer, ForeignKey("complaints.id"))
    file_name = Column(String)
    file_type = Column(String)
    file_content = Column(Text)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    complaint = relationship("Complaint", back_populates="documents")


class AIChatMessage(Base):
    __tablename__ = "ai_chat_messages"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    complaint_id = Column(Integer, ForeignKey("complaints.id"), nullable=True)
    role = Column(String)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    complaint = relationship("Complaint", back_populates="messages")
