from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.complaint import TextExtractRequest, AIExtractionResponse, AIChatRequest, AIChatResponse
from app.services import ai_service, complaint_service

router = APIRouter(prefix="/api/ai", tags=["ai"])

@router.post("/extract", response_model=AIExtractionResponse)
async def extract_from_file(file: UploadFile = File(...)):
    content = await file.read()
    # Decoding assuming text for simplicity
    text_content = content.decode('utf-8', errors='ignore')
    return ai_service.extract_from_file(text_content, file.content_type)

@router.post("/extract-text", response_model=AIExtractionResponse)
def extract_text(request: TextExtractRequest):
    return ai_service.extract_from_text(request.text)

@router.post("/chat", response_model=AIChatResponse)
def chat(request: AIChatRequest, db: Session = Depends(get_db)):
    context = request.context or ""
    if request.complaint_id:
        complaint = complaint_service.get_complaint(db, request.complaint_id)
        if complaint:
            context = f"Complaint {complaint.complaint_number}: {complaint.detailed_description}"
            
    response_text = ai_service.chat_with_ai(request.message, context)
    return AIChatResponse(response=response_text)

@router.post("/classify-risk")
def classify_risk(data: dict):
    return {"risk": ai_service.classify_risk(data)}

@router.post("/check-completeness")
def check_completeness(data: dict):
    return ai_service.check_completeness(data)

@router.post("/recommend-capa")
def recommend_capa(data: dict):
    return {"capa": ai_service.recommend_capa(data)}

@router.post("/detect-duplicate")
def detect_duplicate(data: dict):
    return ai_service.detect_duplicate(data, [])

@router.post("/summarize")
def summarize(data: dict):
    return {"summary": ai_service.generate_summary(data)}

@router.post("/root-cause")
def root_cause(data: dict):
    return {"root_cause": ai_service.recommend_root_cause(data)}
