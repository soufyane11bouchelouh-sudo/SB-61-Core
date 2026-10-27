from fastapi import FastAPI, Depends, HTTPException
from security.auth import verify_neural_token
from core.engine import neural_core
from pydantic import BaseModel

app = FastAPI(
    title="SB-61-Core Neural System",
    description="Secure Neural Architecture with 86 Processing Stations and 5M Synaptic Matrix",
    version="1.0.0"
)

class NeuralInput(BaseModel):
    data_signal: str

@app.get("/")
async def root():
    return {
        "system": "SB-61-Core",
        "status": "Operational",
        "security_status": "Protected"
    }

@app.get("/secure-status", dependencies=[Depends(verify_neural_token)])
async def secure_status():
    return {
        "system": "SB-61-Core",
        "authorization": "Granted",
        "message": "Welcome to the secure core matrix of SB-61."
    }

# نقطة نهاية معالجة الإشارات العصبية (محمية بالمفتاح الآمن)
@app.post("/process", dependencies=[Depends(verify_neural_token)])
async def process_neural_data(payload: NeuralInput):
    result = neural_core.process_signal(payload.data_signal)
    return result

