from langgraph.graph import StateGraph, START, END
from app.agents.state import AgentState
from app.agents.nodes import (
    parse_document, extract_fields, classify_severity, assess_risk,
    check_completeness, detect_duplicates, recommend_root_cause,
    recommend_capa, generate_summary, get_llm
)

# Build extraction graph
workflow = StateGraph(AgentState)

workflow.add_node("parse_document", parse_document)
workflow.add_node("extract_fields", extract_fields)
workflow.add_node("classify_severity", classify_severity)
workflow.add_node("assess_risk", assess_risk)
workflow.add_node("check_completeness", check_completeness)
workflow.add_node("detect_duplicates", detect_duplicates)
workflow.add_node("recommend_root_cause", recommend_root_cause)
workflow.add_node("recommend_capa", recommend_capa)
workflow.add_node("generate_summary", generate_summary)

workflow.add_edge(START, "parse_document")
workflow.add_edge("parse_document", "extract_fields")
workflow.add_edge("extract_fields", "classify_severity")
workflow.add_edge("classify_severity", "assess_risk")
workflow.add_edge("assess_risk", "check_completeness")
workflow.add_edge("check_completeness", "recommend_root_cause")
workflow.add_edge("recommend_root_cause", "recommend_capa")
workflow.add_edge("recommend_capa", "generate_summary")
workflow.add_edge("generate_summary", END)

extraction_app = workflow.compile()

def run_extraction_agent(text: str) -> dict:
    initial_state = {
        "raw_text": text,
        "extracted_fields": {},
        "severity": "",
        "priority": "",
        "risk_classification": "",
        "completeness_score": 0.0,
        "completeness_details": {},
        "is_duplicate": False,
        "duplicate_details": "",
        "capa_recommendation": "",
        "root_cause": "",
        "summary": "",
        "messages": [],
        "progress": 0,
        "errors": []
    }
    
    result = extraction_app.invoke(initial_state)
    return result

def run_chat_agent(message: str, context: str) -> str:
    prompt = f"""You are a pharmaceutical complaint management AI assistant.
Context about the complaint:
{context}

User message:
{message}
"""
    try:
        llm = get_llm()
        if llm:
            response = llm.invoke(prompt)
            return response.content
        else:
            return f"AI Assistant response: I have logged your message regarding '{message}'."
    except Exception as e:
        return f"AI Assistant response: I have logged your message regarding '{message}'."
