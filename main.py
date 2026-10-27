from fastapi import FastAPI, Depends, HTTPException
from security.auth import verify_neural_token
from core.engine import neural_core
from pydantic import BaseModel

app = FastAPI(
    title="SB-61-Core Neural Architecture",
    description="Enterprise-Grade Secure Neural Architecture featuring 86 Processing Stations and 5M Synaptic Matrix.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

class NeuralInput(BaseModel):
    data_signal: str

@app.get("/", tags=["System Status"])
async def root():
    return {
        "system": "SB-61-Core",
        "status": "Operational",
        "security_status": "Protected"
    }

@app.get("/secure-status", tags=["Security"], dependencies=[Depends(verify_neural_token)])
async def secure_status():
    return {
        "system": "SB-61-Core",
        "authorization": "Granted",
        "message": "Welcome to the secure core matrix of SB-61."
    }

@app.post("/process", tags=["Neural Engine"], dependencies=[Depends(verify_neural_token)])
async def process_neural_data(payload: NeuralInput):
    result = neural_core.process_signal(payload.data_signal)
    return result

