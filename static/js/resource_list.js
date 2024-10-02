

document.addEventListener('DOMContentLoaded', function () {
    const showMoreButton = document.getElementById('show-more-button');
    const resourceContainer = document.getElementById('resource-container');
    const resourceEnd = document.getElementById("resource-end");
    const lastRow = document.getElementById("last-list-row");
    let isLoading = false;

    function loadResources() {
        if (isLoading) return;
        isLoading = true;

        const page = showMoreButton.getAttribute('data-page');

        fetch(`/resource_list/?page=${page}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(data => {
                const newResources = (new DOMParser().parseFromString(data, 'text/html')).querySelectorAll('.resource-card-col');

                newResources.forEach(resource => {
                    resourceContainer.appendChild(resource);
                });

                if (newResources.length < 5) {  // Adjust to match paginator count
                    showMoreButton.style.display = 'none';
                    resourceEnd.style.display = 'block';
                } else {
                    showMoreButton.setAttribute('data-page', parseInt(page) + 1);
                }
                isLoading = false;
            })
            .catch(error => console.error('Fetch error:', error));
            isLoading = false;
    }
    
    if (showMoreButton) {
        showMoreButton.addEventListener('click', loadResources);
    }

    let observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting && resourceEnd.style.display !== 'block') {
                loadResources();
            }
        });
    });

    observer.observe(lastRow);

});