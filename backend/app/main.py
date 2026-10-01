from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Project, Skill

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
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).all()

    return [
        {
            "id": project.id,
            "name": project.name,
            "description": project.description,
            "technologies": project.technologies.split(",")
        }
        for project in projects
    ]

@app.get("/api/skills")
def get_skills(db: Session = Depends(get_db)):
    skills = db.query(Skill).order_by(Skill.id).all()

    return [
        {
            "id": skill.id,
            "name": skill.name
        }
        for skill in skills
    ]
