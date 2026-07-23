from app.agents.graph import run_extraction_agent, run_chat_agent
from app.schemas.complaint import AIExtractionResponse
import json

def extract_from_text(text: str) -> AIExtractionResponse:
    result = run_extraction_agent(text)
    
    return AIExtractionResponse(
        extracted_fields=result.get("extracted_fields", {}),
        severity=result.get("severity", ""),
        priority=result.get("priority", ""),
        risk_classification=result.get("risk_classification", ""),
        completeness_score=result.get("completeness_score", 0.0),
        completeness_details=result.get("completeness_details", {}),
        is_duplicate=result.get("is_duplicate", False),
        duplicate_details=result.get("duplicate_details", ""),
        capa_recommendation=result.get("capa_recommendation", ""),
        root_cause=result.get("root_cause", ""),
        summary=result.get("summary", "")
    )

def extract_from_file(file_content: str, file_type: str) -> AIExtractionResponse:
    # Just treat file content as text for now
    return extract_from_text(file_content)

def chat_with_ai(message: str, complaint_context: str) -> str:
    return run_chat_agent(message, complaint_context)

def classify_risk(complaint_data: dict) -> str:
    # Simple standalone call, or we can use the graph
    # For now, simulate standalone
    return "Medium"

def check_completeness(complaint_data: dict) -> dict:
    return {"score": 85.0}

def recommend_capa(complaint_data: dict) -> str:
    return "Investigate batch"

def detect_duplicate(complaint_data: dict, existing_complaints: list) -> dict:
    return {"is_duplicate": False, "duplicate_id": None}

def generate_summary(complaint_data: dict) -> str:
    return "Summary of complaint"

def recommend_root_cause(complaint_data: dict) -> str:
    return "Unknown root cause"
