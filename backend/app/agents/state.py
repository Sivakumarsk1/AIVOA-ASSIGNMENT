from typing import TypedDict, Dict, Any, List

class AgentState(TypedDict):
    raw_text: str
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
    messages: List[Dict[str, str]]
    progress: int
    errors: List[str]
