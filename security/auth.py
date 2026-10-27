from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader

API_KEY_NAME = "X-Neural-Token"
# مفتاح الأمان المؤقت للنظام (سنقوم بتطويره لاحقاً لنظام تشفير متقدم)
SECRET_NEURAL_KEY = "SB61-SECURE-NEURAL-KEY-2026"

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def verify_neural_token(api_key: str = Security(api_key_header)):
    if api_key == SECRET_NEURAL_KEY:
        return api_key
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Access Denied: Invalid or Missing Neural Security Token."
    )

