from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controller.rotas import router

# Inicia o FastAPI - framework responsável por criar o backend
app = FastAPI()

# Definições de acesso
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET","POST"],
    allow_headers=["*"],
)

app.include_router(router.router)