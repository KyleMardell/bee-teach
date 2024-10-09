// function executes when the dom has finished loading
document.addEventListener('DOMContentLoaded', function () {

    // hides the django generated comment label
    const commentFormLabel = document.querySelector('label[for="id_body"]');
    if (commentFormLabel) {
        console.log("found");
        commentFormLabel.style.display = "none";
    }

    // finds all instances of key-stage and applies the associated wording labels
    let keyStageLabels = document.getElementsByClassName('key-stage');
    for (let keyStageLabel of keyStageLabels) {

        switch (keyStageLabel.innerText) {  // Use innerText to get the element's text
            case "0":
                keyStageLabel.innerText = "Key-Stage: Early years";
                break;
            case "1":
                keyStageLabel.innerText = "Key-Stage: 1";
                break;
            case "2":
                keyStageLabel.innerText = "Key-Stage: 2";
                break;
            case "3":
                keyStageLabel.innerText = "Key-Stage: 3";
                break;
            default:
                keyStageLabel.innerText = "Key-Stage: Not Found";
                break;
        }
    }
});
