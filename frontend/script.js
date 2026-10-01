async function loadProjects() {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/projects");

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const projects = await response.json();

        const projectsContainer = document.querySelector("#projects-container");

        if (!projectsContainer) {
            return;
        }

        projectsContainer.innerHTML = projects.map(project => `
            <div class="project-card">

                <h3>${project.name}</h3>

                <p>
                    ${project.description}
                </p>

                <div class="technologies">
                    ${project.technologies
                        .map(technology => `<span>${technology}</span>`)
                        .join("")}
                </div>

            </div>
        `).join("");

    } catch (error) {
        console.error("Unable to load projects:", error);
    }
}
async function loadSkills() {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/skills");

        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const skills = await response.json();

        const skillsContainer = document.querySelector("#skills-container");

        if (!skillsContainer) {
            return;
        }

        skillsContainer.innerHTML = skills.map(skill => `
            <div>${skill.name}</div>
        `).join("");

    } catch (error) {
        console.error("Unable to load skills:", error);
    }
}

loadProjects();
loadSkills();