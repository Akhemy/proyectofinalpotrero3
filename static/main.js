document.addEventListener('DOMContentLoaded', () => {
    fetch('/api/courses')
        .then(response => response.json())
        .then(data => {
            const coursesDiv = document.getElementById('courses-container');
            data.forEach(course => {
                const courseElement = document.createElement('div');
                courseElement.classList.add('col-md-4');
                courseElement.innerHTML = `
                    <div class="card mb-4">
                        <div class="card-body">
                            <h5 class="card-title">${course.title}</h5>
                            <p class="card-text">${course.description}</p>
                            <a href="/courses/${course.id}" class="btn btn-primary">Ver Curso</a>
                        </div>
                    </div>
                `;
                coursesDiv.appendChild(courseElement);
            });
        })
        .catch(error => console.error('Error fetching courses:', error));
});

