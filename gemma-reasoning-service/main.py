from fastapi import FastAPI
from src.api.routes import router
from src.core.config import settings

app = FastAPI(
    title="GotiHub Gemma Bridge",
    description="Agentic Reasoning Layer for Sovereign Governance",
    version="1.0.0"
)

# Registering the Audit Router
app.include_router(router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "gemma-bridge"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=settings.DEBUG)