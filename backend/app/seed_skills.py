from app.database import SessionLocal
from app.models import Skill


db = SessionLocal()

skills = [
    "Python",
    "ERPNext",
    "Frappe",
    "Linux",
    "Git",
    "Docker",
    "AWS",
    "Terraform",
    "Kubernetes",
    "GitHub Actions",
    "Prometheus",
    "Grafana",
]

for skill_name in skills:
    existing_skill = db.query(Skill).filter(Skill.name == skill_name).first()

    if not existing_skill:
        db.add(Skill(name=skill_name))

db.commit()
db.close()

print("Skills added successfully.")
