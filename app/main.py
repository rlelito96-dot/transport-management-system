from fastapi import FastAPI

app = FastAPI(title="TMS Backend")


@app.get("/")
def root():
    return {"message": "TMS running"}
