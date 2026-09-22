from fastapi import FastAPI

app = FastAPI(
    title="Rasna Cloud Portfolio API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Rasna Cloud Portfolio API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
