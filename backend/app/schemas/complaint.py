from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime

class ComplaintBase(BaseModel):
    complaint_source: str
    customer_name: str
    product_name: str
    product_strength_grade: str
    batch_lot_number: str
    manufacturing_date: Optional[str] = None
    expiry_date: Optional[str] = None
    quantity_affected: Optional[str] = None
    quantity_unit: str = "kg"
    complaint_type: str
    complaint_date: Optional[str] = None
    detailed_description: str
    initial_severity: str
    priority: str

class ComplaintCreate(ComplaintBase):
    pass

class ComplaintUpdate(BaseModel):
    status: Optional[str] = None
    complaint_source: Optional[str] = None
    customer_name: Optional[str] = None
    product_name: Optional[str] = None
    product_strength_grade: Optional[str] = None
    batch_lot_number: Optional[str] = None
    manufacturing_date: Optional[str] = None
    expiry_date: Optional[str] = None
    quantity_affected: Optional[str] = None
    quantity_unit: Optional[str] = None
    complaint_type: Optional[str] = None
    complaint_date: Optional[str] = None
    detailed_description: Optional[str] = None
    initial_severity: Optional[str] = None
    priority: Optional[str] = None
    ai_risk_classification: Optional[str] = None
    ai_summary: Optional[str] = None
    ai_root_cause: Optional[str] = None
    ai_capa_recommendation: Optional[str] = None
    ai_completeness_score: Optional[float] = None
    is_duplicate: Optional[bool] = None
    duplicate_of_id: Optional[int] = None

class ComplaintResponse(ComplaintBase):
    id: int
    complaint_number: str
    status: str
    ai_risk_classification: Optional[str] = None
    ai_summary: Optional[str] = None
    ai_root_cause: Optional[str] = None
    ai_capa_recommendation: Optional[str] = None
    ai_completeness_score: Optional[float] = None
    is_duplicate: bool
    duplicate_of_id: Optional[int] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class DocumentUpload(BaseModel):
    file_name: str
    file_type: str
    file_content: str

class TextExtractRequest(BaseModel):
    text: str

class AIChatRequest(BaseModel):
    message: str
    complaint_id: Optional[int] = None
    context: Optional[str] = None

class AIChatResponse(BaseModel):
    response: str

class AIExtractionResponse(BaseModel):
    extracted_fields: Dict[str, Any]
    severity: str
    priority: str
    risk_classification: str
    completeness_score: float
    completeness_details: Dict[str, Any]
    is_duplicate: bool
    duplicate_details: str
    capa_recommendation: str
    root_cause: str
    summary: str
