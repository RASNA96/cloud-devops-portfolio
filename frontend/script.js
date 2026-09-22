async function loadProjects() {
    try {
        const response = await fetch("http://127.0.0.1:8000/api/projects");

        const projects = await response.json();

        const projectsContainer = document.querySelector(".project-card");

        if (!projectsContainer) {
            return;
        }

        const project = projects[0];

        projectsContainer.innerHTML = `
            <h3>${project.name}</h3>

            <p>
                ${project.description}
            </p>

            <div class="technologies">
                ${project.technologies
                    .map(technology => `<span>${technology}</span>`)
                    .join("")}
            </div>
        `;

    } catch (error) {
        console.error("Unable to load projects:", error);
    }
}


loadProjects();
