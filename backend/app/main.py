from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database import get_db
from app.models import Project, Skill, Profile


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


# -------------------------
# Project Schemas
# -------------------------

class ProjectCreate(BaseModel):
    name: str
    description: str
    technologies: list[str]


class ProjectUpdate(BaseModel):
    name: str
    description: str
    technologies: list[str]


# -------------------------
# Projects
# -------------------------

@app.get("/api/projects")
def get_projects(db: Session = Depends(get_db)):
    projects = db.query(Project).order_by(Project.id).all()

    return [
        {
            "id": project.id,
            "name": project.name,
            "description": project.description,
            "technologies": project.technologies.split(",")
        }
        for project in projects
    ]


@app.get("/api/projects/{project_id}")
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {
        "id": project.id,
        "name": project.name,
        "description": project.description,
        "technologies": project.technologies.split(",")
    }


@app.post("/api/projects")
def create_project(
    project_data: ProjectCreate,
    db: Session = Depends(get_db)
):
    project = Project(
        name=project_data.name,
        description=project_data.description,
        technologies=",".join(project_data.technologies)
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return {
        "id": project.id,
        "name": project.name,
        "description": project.description,
        "technologies": project.technologies.split(",")
    }


@app.put("/api/projects/{project_id}")
def update_project(
    project_id: int,
    project_data: ProjectUpdate,
    db: Session = Depends(get_db)
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    project.name = project_data.name
    project.description = project_data.description
    project.technologies = ",".join(project_data.technologies)

    db.commit()
    db.refresh(project)

    return {
        "id": project.id,
        "name": project.name,
        "description": project.description,
        "technologies": project.technologies.split(",")
    }


@app.delete("/api/projects/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    db.delete(project)
    db.commit()

    return {
        "message": "Project deleted successfully"
    }


# -------------------------
# Skills
# -------------------------

# -------------------------
# Skills
# -------------------------

class SkillCreate(BaseModel):
    name: str


class SkillUpdate(BaseModel):
    name: str


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


@app.get("/api/skills/{skill_id}")
def get_skill(skill_id: int, db: Session = Depends(get_db)):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()

    if not skill:
        raise HTTPException(
            status_code=404,
            detail="Skill not found"
        )

    return {
        "id": skill.id,
        "name": skill.name
    }


@app.post("/api/skills")
def create_skill(
    skill_data: SkillCreate,
    db: Session = Depends(get_db)
):
    skill = Skill(
        name=skill_data.name
    )

    db.add(skill)
    db.commit()
    db.refresh(skill)

    return {
        "id": skill.id,
        "name": skill.name
    }


@app.put("/api/skills/{skill_id}")
def update_skill(
    skill_id: int,
    skill_data: SkillUpdate,
    db: Session = Depends(get_db)
):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()

    if not skill:
        raise HTTPException(
            status_code=404,
            detail="Skill not found"
        )

    skill.name = skill_data.name

    db.commit()
    db.refresh(skill)

    return {
        "id": skill.id,
        "name": skill.name
    }


@app.delete("/api/skills/{skill_id}")
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db)
):
    skill = db.query(Skill).filter(Skill.id == skill_id).first()

    if not skill:
        raise HTTPException(
            status_code=404,
            detail="Skill not found"
        )

    db.delete(skill)
    db.commit()

    return {
        "message": "Skill deleted successfully"
    }

@app.get("/api/profile")
def get_profile(db: Session = Depends(get_db)):
    profile = db.query(Profile).first()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    return {
        "id": profile.id,
        "name": profile.name,
        "title": profile.title,
        "intro": profile.intro,
        "about": profile.about,
        "email": profile.email,
        "github_url": profile.github_url
    }