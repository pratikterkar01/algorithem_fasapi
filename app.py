# app.py
from fastapi import FastAPI
from controller.algo_controller import router as user_router

app = FastAPI(title="My Clean FastAPI Architecture")

# Register routes
app.include_router(user_router, prefix="/api")

