from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from app.views import endpoints
from app.config.database import Base, engine

# Migrate Table
Base.metadata.create_all(bind=engine)

# Init Server
app = FastAPI()

# Apply Cors Configuration
app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Handle views
app.include_router(endpoints.router)