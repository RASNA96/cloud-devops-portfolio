from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Rasna Cloud Portfolio API",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:3000",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

@app.get("/api/projects")
def get_projects():
    return [
        {
            "name": "Cloud-Native Portfolio & DevOps Platform",
            "description": "A production-style cloud and DevOps project.",
            "technologies": [
                "AWS",
                "Docker",
                "Terraform",
                "Kubernetes",
                "GitHub Actions"
            ]
        }
    ]
