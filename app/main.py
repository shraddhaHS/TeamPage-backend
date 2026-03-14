from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import FRONTEND_URL

from app.api.team_members import router as team_router

app = FastAPI(title="Team Members API")

# CORS configuration
origins = [ FRONTEND_URL ]

app.add_middleware( 
    CORSMiddleware,
    allow_origins=origins,      
    allow_credentials=True,
    allow_methods=["*"],        
    allow_headers=["*"],        
)

@app.get("/health")
async def health():
    return {
        "flag": 1,
        "message": "Server running",
        "data": None
    }

app.include_router(team_router)