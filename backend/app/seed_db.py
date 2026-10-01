from app.database import SessionLocal
from app.models import Project


db = SessionLocal()

try:
    project = Project(
        name="Cloud-Native Portfolio & DevOps Platform",
        description="A production-style cloud and DevOps project.",
        technologies="AWS,Docker,Terraform,Kubernetes,GitHub Actions"
    )

    db.add(project)
    db.commit()

    print("Project added successfully.")

finally:
    db.close()
