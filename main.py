from fastapi import FastAPI, Depends
from security.auth import verify_neural_token

app = FastAPI(
    title="SB-61-Core Neural System",
    description="Secure Neural Architecture with 86 Processing Stations",
    version="1.0.0"
)

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

