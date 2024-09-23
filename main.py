from fastapi import FastAPI

from Core.config import settings
from API.v1.API import api_router

app = FastAPI(title='Curso API - Segurança', docs_url="/docs")

app.include_router(api_router, prefix=settings.API_V1_STR)



#   Token: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzI3NjQzNDE0LCJpYXQiOjE3MjcwMzg2MTQsInN1YiI6IjYifQ.GvkzTW8UE_3CrTP7M8rac_w4gzbyyg2O4Bpcr2ZPpLA
#   type: "bearer"
