from fastapi import FastAPI

from app.api.routers.auth import router as auth_router

app = FastAPI(title="TMS Backend")

app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "TMS running"}
