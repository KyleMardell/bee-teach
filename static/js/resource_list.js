console.log("Resource Page")

document.addEventListener('DOMContentLoaded', function () {
    const showMoreButton = document.getElementById('show-more-button');
    
    if (showMoreButton) {
        showMoreButton.addEventListener('click', function () {
            const page = showMoreButton.getAttribute('data-page');

            fetch(`/resource_list/?page=${page}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.text();
                })
                .then(data => {
                    console.log(data);
                    const resourceContainer = document.getElementById('resource-container');
                    resourceContainer.insertAdjacentHTML('beforeend', data);
                    
                    const newResourcesCount = (new DOMParser().parseFromString(data, 'text/html')).querySelectorAll('.resource-card').length;
                    if (newResourcesCount < 3) {  // Adjust to match paginator count
                        showMoreButton.style.display = 'none';
                    } else {
                        showMoreButton.setAttribute('data-page', parseInt(page) + 1);
                    }
                })
                .catch(error => console.error('Fetch error:', error));
        });
    }
});