const editButtons = document.getElementsByClassName("edit-button");

const resource_title = document.getElementById("id_title");
const resource_key_stage = document.getElementById("id_key_stage");
const resource_content = document.getElementById("id_content");
const resource_links = document.getElementById("id_links");
const resource_status = document.getElementById("id_status");

const resourceCard = document.getElementById("editResourceCard");
const resourceForm = document.getElementById("editResourceForm");
const submitButton = document.getElementById("submitEditButton");

/*
Adds an event listener to each resource edit button and populates 
the edit form with the resource details when clicked.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {

    // displays the form
    resourceCard.style.display = "Flex";

    // resource data from the edit button
    let resourceId = e.target.getAttribute("data-resource_id");
    let resourceTitle = e.target.getAttribute("data-resource_title");
    let resourceKeyStage = e.target.getAttribute("data-resource_key_stage");
    let resourceContent = e.target.getAttribute("data-resource_content");
    let resourceLinks = e.target.getAttribute("data-resource_links");
    let resourceStatus = e.target.getAttribute("data-resource_status");

    // populates the form
    resource_title.value = resourceTitle;
    resource_key_stage.value = resourceKeyStage;
    resource_links.value = resourceLinks;
    resource_status.value = resourceStatus;

    // uses django summernote for the resource content
    $(resource_content).summernote('code', resourceContent);

    // sets the action of the edit button to the url for editing the selected resource
    resourceForm.setAttribute("action", `edit_resource/${resourceId}`);
    submitButton.innerText = "Update";
  });
}