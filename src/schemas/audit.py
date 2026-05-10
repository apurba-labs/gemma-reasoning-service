from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class AuditRequest(BaseModel):
    transaction_id: str = Field(..., example="ALUM-2026-DHAKA-001")
    audit_type: str = Field(..., example="identity")
    metadata: Dict[str, Any] = Field(default_factory=dict)

class AuditResult(BaseModel):
    decision: str = Field(..., description="APPROVED or REJECTED")
    reasoning: List[str] = Field(..., description="Steps taken by the multi-agent loop")
    confidence_score: float = Field(..., ge=0, le=1)
    agent_version: str = "Gemma-4b-Sovereign-v1"