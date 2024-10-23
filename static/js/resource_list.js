document.addEventListener('DOMContentLoaded', function () {
    const showMoreButton = document.getElementById('show-more-button');
    const resourceContainer = document.getElementById('resource-container');
    const resourceEnd = document.getElementById("resource-end");
    const lastRow = document.getElementById("last-list-row");
    const paginationAmount = 5;  // Adjust to match paginator amount in views.py
    let isLoading = false;

    /*
    Function to load the next pagination of resources, set pagination number to match the view.
    isLoading boolean used to stop the function from being called multiple times before finishing.
    */
    function loadResources() {
        if (isLoading) return;
        isLoading = true;

        // gets current page number
        const page = showMoreButton.getAttribute('data-page');

        // uses fetch to get the next resources from the django view
        fetch(`/resource_list/?page=${page}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(data => {
                // parses the new resources from the api call into text/html
                const newResources = (new DOMParser().parseFromString(data, 'text/html')).querySelectorAll('.resource-card-col');

                // loop through the new resources and add them to the resource container
                newResources.forEach(resource => {
                    resourceContainer.appendChild(resource);
                });

                // checks if the last retrieved number of resources is less than the pagination amount
                if (newResources.length < paginationAmount) {
                    showMoreButton.style.display = 'none';
                    resourceEnd.style.display = 'block';
                } else {
                    // increases the page number attribute on the show more button
                    showMoreButton.setAttribute('data-page', parseInt(page) + 1);
                }
                isLoading = false;
            })
            .catch(error => console.error('Fetch error:', error));
            isLoading = false;
    }
    
    // show more button event listener used as backup to auto loading
    if (showMoreButton) {
        showMoreButton.addEventListener('click', loadResources);
    }

    // creates an observer to check if the show more button is shown on screen and then
    // automatically runs the loadResources function to get the next resources
    let observer = new IntersectionObserver(function(e) {
        e.forEach(e => {
            if (e.isIntersecting && resourceEnd.style.display !== 'block') {
                loadResources();
            }
        });
    });

    // sets the observer
    observer.observe(lastRow);

});