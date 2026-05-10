from fastapi import APIRouter, HTTPException
from src.schemas.audit import AuditRequest, AuditResult
from src.services.reasoning_service import ReasoningService

router = APIRouter()
reasoning_service = ReasoningService()

@router.post("/audit", response_model=AuditResult)
async def run_audit(request: AuditRequest):
    try:
        return await reasoning_service.evaluate_dna_sequence(
            transaction_id=request.transaction_id,
            audit_type=request.audit_type
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Reasoning Error: {str(e)}")