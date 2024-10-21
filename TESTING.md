# Bee Teach Testing

Testing of the Bee Teach app was done using both manual and automated testing methods. Manual testing was done both during and post development, with in-development testing carried out using Google Chrome Developer Tools. Automated testing carried out using the built in Django test suite. Here you can find details of all the app testing, including validation and accessability tests.

[Bee Teach Live App](https://bee-teach-95df758315f5.herokuapp.com/)
[Bee Teach Repo](https://github.com/KyleMardell/bee-teach)

## Contents

## Validation

### HTML Validation
In order to validate each html page, I first used Google Chrome developer tools to view each pages source code once rendered to the browser. This means I have the end HTML documents to full validate, compared to the django templates that can only contain part of the end html, and often use python or javascript to generate HTML to the browser. I then ran each pages full HTML documents through the [Web3 HTML Validator](https://validator.w3.org/). 
The only Page with errors was the Sign Up page. These errors are caused by the auto generated password requirements text, as there is an unordered list contained inside a paragraph. Although it generates errors through the validator, when testing on multiple devices these requirements are displayed as intended. Due to this I have left this page as it is, rather than removing the text using django or javascript and inserting my own.

The results of HTML page validation can be found below.

- [Index](/docmedia/validation/validation-html-index.png)
- [Home](/docmedia/validation/validation-html-home.png)
- [User Resources](/docmedia/validation/validation-html-posts.png)
- [Create Resource](/docmedia/validation/validation-html-create.png)
- [Resource Detail](/docmedia/validation/validation-html-detail.png)
- [Resource Draft](/docmedia/validation/validation-html-draft.png)
- [Admin](/docmedia/validation/validation-html-admin.png)
- [Sign Up - Errors](/docmedia/validation/validation-html-signup.png)
- [Log In](/docmedia/validation/validation-html-login.png)
- [Log Out](/docmedia/validation/validation-html-logout.png)

### CSS Validation
To validate the CSS I created, I used the [WEB3 CSS Validator](https://jigsaw.w3.org/css-validator/) on my single CSS file.

The results of the CSS validation can be found below.

- [CSS Validation](/docmedia/validation/validation-css.png)

### Python Linter
For the Python files in the project I used the [CI Python Linter](https://pep8ci.herokuapp.com/#) to check all my files complied with python standards.
I tested files such as views, urls, models and testing. All files pass the linter clear and error free.

The results of the Python linter validation can be found below.

- [Views](/docmedia/validation/linter-views.png)
- [Models](/docmedia/validation/linter-models.png)
- [Post URLs](/docmedia/validation/linter-posturls.png)
- [App URLs](/docmedia/validation/linter-appurls.png)
- [Forms](/docmedia/validation/linter-forms.png)
- [Admin](/docmedia/validation/linter-admin.png)
- [Test Forms](/docmedia/validation/linter-testform.png)
- [Test Views](/docmedia/validation/linter-testview.png)

### JavaScript
When it came to the JavaScript for the project, I checked each of my files and page scripts using [jshint](https://jshint.com/), with no major errors or issues across any of the scripts. There was a caution for the functions created within loops (used for multiple edit buttons) having the potential to cause confusing semantics, but the previously described HTML validation confirms no errors are created.


## Accessibility and Performance

### Lighthouse Testing
Google Chrome's Lighthouse testing has criteria for performance, accessability, best practices and SEO. I tested all pages through the lighthouse tester with high scores for most sections. There were some justifiable exceptions or lower resulting scores. Firstly pages with images have lower best practices scores due to the images being retrieved from Cloudinary, and the Heroku server used does not provide a HTTPS automatic connection for these images. This causes warning in the console browser and can only be remedied with the use of a HTTPS server. Secondly there are a couple of pages with lower SEO scores. This is due to the pages only being displayed when logged in, such as creating a resource and therefore do not need high SEO scores.

The results of the Lighthouse testing can be found below.

- [Index](/docmedia/validation/lighhouse-index.png)
- [Home](/docmedia/validation/lighthouse-home.png)
- [Users Resources](/docmedia/validation/lighthouse-userposts.png)
- [Create Resource](/docmedia/validation/lighthouse-create.png)
- [Resource Detail](/docmedia/validation/lighthouse-detail.png)
- [Resource Draft](/docmedia/validation/lighthouse-draft.png)
- [Admin](/docmedia/validation/lighthouse-admin.png)
- [Sign Up](/docmedia/validation/lighthouse-signup.png)
- [Log In](/docmedia/validation/lighthouse-login.png)
- [Log Out](/docmedia/validation/lighthouse-logout.png)

### Wave Testing
When testing further for accessibility issues, I used the [WAVE Accessibility Tester](https://wave.webaim.org/) on the pages I was able to. These were the pages that do not require users to be logged in, the index page, log in and sign up pages. Each of these pages had no errors when tested using the WAVE tool.

The results of the WAVE testing can be found below.

- [Index](/docmedia/validation/wave-home.png)
- [Log In](/docmedia/validation/wave-login.png)
- [Sign Up](/docmedia/validation/wave-signup.png)

## Unit Testing
When writing unit tests, I used the built in Django test suite. There are 2 python testing files, [test forms](/post/test_forms.py) and [test views](/post/test_views.py), each of which test the respective forms or views. I used the [Django Testing Documentation](https://docs.djangoproject.com/en/5.1/topics/testing/tools/) to find and better understand which tests I needed to use. I tried to implement as many tests as I could think of, but I imagine there are more potential tests. I also used a [Stack Overflow](https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages/14909727) thread to help me when creating tests for feedback messages.

The test names for both forms and views testing can be found below.

- Forms
    - Comment Form
        - test_form_is_valid
        - test_form_is_invalid
    - Resource Form
        - test_form_is_valid_with_empty_content_and_links_draft
        - test_form_is_valid_with_empty_content_and_links_published
        - test_form_is_valid_full_input
        - test_form_is_valid_with_empty_links
        - test_form_is_valid_with_empty_content
        - test_form_is_valid_title_character_limit
        - test_form_is_valid_key_stage_one
        - test_form_is_valid_key_stage_two
        - test_form_is_valid_key_stage_three
        - test_form_is_invalid_blank_form
        - test_form_is_invalid_missing_key_stage
        - test_form_is_invalid_missing_status
        - test_form_is_invalid_negative_one_key_stage
        - test_form_is_invalid_negative_zero_key_stage
        - test_form_is_invalid_negative_one_status
        - test_form_is_invalid_negative_zero_status
        - test_form_is_invalid_top_edge_key_stage
        - test_form_is_invalid_top_edge_status
        - test_form_is_invalid_non_numeric_key_stage
        - test_form_is_invalid_non_numeric_status
        - test_form_is_invalid_overly_long_title
        - test_form_is_invalid_only_optional_fields

- Views
    - Index
        - test_index_page_status_code
        - test_index_page_uses_correct_template
        - test_index_page_shows_four_latest_resources
        - test_index_page_shows_only_published_resources
    - Home
        - test_home_page_status_code
        - test_home_page_requires_authentication
        - test_home_page_uses_correct_template
        - test_partial_template
        - test_home_page_shows_only_published_resources
        - test_featured_resources
    - User Posts
        - test_user_resources_page_status
        - test_user_resources_page_requires_authentication
        - test_user_resources_page_uses_correct_template
        - test_user_resources_shows_published_resources
        - test_user_resources_shows_draft_resources
    - Resource Detail
        - test_resource_detail_page_status_code
        - test_resource_detail_page_requires_authentication
        - test_resource_detail_uses_correct_template
        - test_resource_detail_page_with_comment_form
        - test_successful_comment_submission
    - Resource Preview
        - test_resource_preview_page_status_code
        - test_resource_preview_page_requires_authentication
        - test_resource_preview_uses_correct_template
    - Resource Create
        - test_resource_create_page_status_code
        - test_resource_create_page_uses_correct_template
        - test_resource_create_page_with_resource_form
        - test_successful_published_resource_form_submission
        - test_successful_draft_resource_form_submission
    - Resource Edit
        - test_successful_published_resource_edit_submission
        - test_successful_draft_resource_edit_submission
    - Resource Delete
        - test_resource_delete_success
        - test_resource_delete_not_author
    - Comment Edit
        - test_successful_comment_edit
        - test_comment_edit_not_author
    - Comment Delete
        - test_comment_delete_success
        - test_comment_delete_not_author
    - Resource Likes
        - test_successful_resource_like
        - test_successful_resource_unlike

## Manual Testing

### In Development
In development testing was done using Google Chrome developer tools and the inspect function. I used console log and print to check data when creating the Javascript scripts as well as when creating the Python view functions. This way I could keep track of the transfer and transformation of the data passed between functions, as well as from the back end to the front end, and visa versa. 
I also used the mock device sizes to check the apps pages were fully responsive across all screen sizes when styling the app. In the inspect view, I highlighted the Django auto created form elements so I could target them via their id in either CSS or Javascript, adding further styles or functionality.
As I chose to deploy the app to Heroku early in development, I would also frequently check features or styles were displaying correctly over the internet on the devices I had access to: an iPhone 14 & 15, iPad Pro, Android tablet and 2 PC screens, a 1080 and a 4k monitor.

### User Testing
When it came to user testing, as I had created the Bee Teach app with my partner in mind, they were my initial go to tester. This meant I could get instant feedback from a target user and make quick changes or implement features and styles suggested. Once the app was in a more complete state, I then asked a small group of people to use the app as they would and let me know of any constructive feedback they had. Although positive feedback is helpful and let me know which elements to keep, I wanted to concentrate on what improvements could be made and thus kept a list of some of the constructive feedback I received. The main change made following feedback was due to a bug caused by simple oversight. Initially when posting a resource as draft, the user was directed to their list of posts and could not view a resource before posting, only edit its contents in the edit form. Creating a resource preview was a core feature I overlooked and created as a result of early user testing.

Below is some of the constructive feedback from a small group of users.
- Landscape images are aligned at the top of a card rather than in the preferred center such as portrait or square images.
- Filtering by key stage would be good when there are lots of resources.
- A user profile page or profile picture next to the name of the person who posted the resource.
- Help or info might be needed on the resource list and create pages.
- It would be nice if resources loaded automatically instead of pressing the view more button.
- More indication of a draft resource, more info to let you know it will be draft by default.
- A preview page for draft resources to view before posting.
- You should be able to click the entire resource preview card to link to its detail page, not just the title text.
- Being able to see thumbnails of the pictures you have added in the create resource page.
- Being able to add PDFs to a resource in place of, or as well as images.

Some of these features I implemented during the development phase and some I did not get chance to implement but are considerations for future features.

### Final Development Phases
In the final development phases I carried out manual testing of all the links, buttons, pages and admin permissions across the site, ensuring fully correct functionality of all the features I did not test using automated testing. As the automated testing was fairly robust, I found that did not leave a lot of manual testing that was needed. That being said, I still tested all the features manually incase I had missed anything when writing tests. 

Below is an overview of the manual tests I carried out not covered by automated testing.

- Each menu link works correctly from all pages.
- Admin menu links and pages are only displayed for, or accessible by admin users. 
- Both call to action buttons on the index page link to the sign up page as intended.
- Sign up, log in and log out pages work as intended.
- All published resources link to their detail page.
- Images can be added to the create resource page.
- User posted resources page displays a message when there are no added resources.
- Admin users can view and delete any resources, comments or image media.
- Admin users can view a list of users and delete or ban accounts.