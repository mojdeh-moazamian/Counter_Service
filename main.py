from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from route import router as counter_router


app=FastAPI()


origins=[
    "http://localhost:3001"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(counter_router)