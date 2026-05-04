from fastapi import APIRouter

from app.api.v1.endpoints import authors, users

api_router = APIRouter()
api_router.include_router(authors.router, prefix='/authors', tags=['authors'])
api_router.include_router(users.router, prefix='/users', tags=['users'])
