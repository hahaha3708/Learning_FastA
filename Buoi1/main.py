"""
Bài 1: Hệ thống cơ bản
1.1 Tạo hàng rào FastAPI
python -m venv venv
venv\Scripts\activate
pip install fastapi uvicorn

"""

from fastapi import FastAPI

# Khai báo app
app = FastAPI(
    title="Hello World",
    description="Backend API for Hello World",
    version="0.1.0"
)

# Định nghĩa endpoint
@app.get("/health", tags=["System"])
async def health_check():
    return {
        "status": "ok",
        "message": "Hello World",
        "version": "0.1.0"
    }
