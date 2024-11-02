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
Google Chrome's Lighthouse testing has criteria for performance, accessability, best practices and SEO. I tested all pages through the lighthouse tester with high scores for most sections. 

There were some justifiable exceptions or lower resulting scores. Pages with images have lower best practices scores, due to the images being retrieved from Cloudinary and the Heroku server used, does not provide a HTTPS automatic connection for these images. This causes warning in the browser console, although no errors, and can only be remedied with the use of a HTTPS server.

All other results were either in the high 90s or 100, meaning no issues with the tested accessibility, SEO or performance as expected.

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
When testing further for accessibility issues, I used the [WAVE Accessibility Tester](https://wave.webaim.org/) on all pages, ensuring they were populated with content where possible.

The only page with any errors was the create resource page, with the errors for missing form labels being caused by the Summernote content box, as accessibility is a known challenge for summernote. After inspecting the summernote editing box using google chrome dev tools, i found it is created using a div, that generates html when the user enters text in the input div. As the input is a div and not an input or another type of [labelable element](https://html.spec.whatwg.org/multipage/forms.html#category-label), it is not possible to add a label to this type of summernote input. I considered removing the summernote content input, but decided that having the text formatting options outweighed having a missing label and in this case is justifiable.

Here you can find the summernote code causing the errors and wave testing results for the create resource page.
- [Summernote Generated Code](/docmedia/validation/summernote-test-field-code.png)
- [Wave Create Resource Results](/docmedia/validation/wave-create-errors.png)
- [Wave Create Resource Page](/docmedia/validation/wave-create-page-error.png)

The results of the WAVE testing for all pages can be found below.

- [Index](/docmedia/validation/wave-home.png)
- [Log In](/docmedia/validation/wave-login.png)
- [Sign Up](/docmedia/validation/wave-signup.png)
- [Home Page](/docmedia/validation/wave-home-in.png)
- [Create Resource](/docmedia/validation/wave-create.png)
- [Resource List](/docmedia/validation/wave-resource-list.png)

## Unit Testing
When writing unit tests, I used the built in Django test suite. There are 2 python testing files, [test forms](/post/test_forms.py) and [test views](/post/test_views.py), each of which test the respective forms or views. 

I used the [Django Testing Documentation](https://docs.djangoproject.com/en/5.1/topics/testing/tools/) to find and better understand which tests I needed to use. I tried to implement as many tests as I could think of, but I imagine there are more potential tests. I also used a [Stack Overflow](https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages/14909727) thread to help me when creating tests for feedback messages.

The test names for both forms and views testing, as well as a screenshot of the results can be found below.

- [Results](/docmedia/validation/django-tests-results.png)
- Run the tests with the terminal command "python3 manage.py test"

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
When it came to user testing, as I had created the Bee Teach app with my partner in mind, they were my initial go to tester. This meant I could get instant feedback from a target user and make quick changes or implement features and styles suggested. Once the app was in a more complete state, I then asked a small group of people to use the app as they would and let me know of any constructive feedback they had. 

Although positive feedback is helpful and let me know which elements to keep, I wanted to concentrate on what improvements could be made and thus kept a list of some of the constructive feedback I received. The main change made following feedback was due to a bug caused by simple oversight. Initially when posting a resource as draft, the user was directed to their list of posts and could not view a resource before posting, only edit its contents in the edit form. Creating a resource preview was a core feature I overlooked and created as a result of early user testing.

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

Below is an overview of the additional manual testing, with a detailed table of manual tests carried not covered by automated testing. Where automated testing also covers manual testing of the create resource form I have included an overview of the testing verified with both manual and the automated tests listed above.

- Each menu link works correctly from all pages.
- Admin menu links and pages are only displayed for, or accessible by admin users. 
- Both call to action buttons on the index page link to the sign up page as intended.
- Sign up, log in and log out pages work as intended.
- All published resources link to their detail page.
- Images can be added to the create resource page.
- User posted resources page displays a message when there are no added resources.
- Admin users can view and delete any resources or comments.

### Manual Test Results Table

| Feature | Expected Outcome | Test Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Nav Bar |
| Logo text link - Not logged in | When clicked, redirects to the index page | Clicked logo | Redirected to index page | Pass |
| Logo text link - Logged in | When clicked, redirects to the home page | Clicked logo | Redirected to home page | Pass |
| Logo text link: hover (desktop) | Changes curser to pointer | Hovered mouse over link | Curser changed to pointer | Pass |
| Menu burger icon (mobile/tablet) | Displays expanded menu | Clicked menu icon | Expanded menu displayed | Pass |
| Home menu link |  When clicked, redirects to the home page | Clicked logo | Redirected to home page | Pass |
| Home menu link: hover (desktop) | Changes curser to pointer | Hovered mouse over link | Curser changed to pointer | Pass |
| Log In menu link |  When clicked, redirects to the Log In page | Clicked logo | Redirected to Log In page | Pass |
| Log In menu link: hover (desktop) | Changes curser to pointer | Hovered mouse over link | Curser changed to pointer | Pass |
| Sign Up menu link |  When clicked, redirects to the Sign Up page | Clicked logo | Redirected to Sign Up page | Pass |
| Sign Up menu link: hover (desktop) | Changes curser to pointer | Hovered mouse over link | Curser changed to pointer | Pass |
| Admin menu link | Admin menu link displayed | Logged in as admin / superuser | Admin link displayed in menu | Pass |
| Admin menu link | Admin menu link not displayed | Logged in as regular user | No admin link in menu | Pass |
| Admin menu link | When clicked, redirects to the admin page as admin user | Clicked admin link as admin user | Redirected to admin page | Pass |
| Messages |
| Message bar | Message removed | Clicked X button | Message removed from page | Pass |
| Sign Up Page |
| Sign Up button: hover (desktop) | Changes curser to pointer, button changes colour | Hovered mouse over button | Curser changed to pointer, button colour changed | Pass |
| Sign Up form | Error displayed | Clicked sign up button with all fields empty | "Please fill in this field" error pointing at the username box displayed | Pass |
| Sign Up form | Error displayed | Clicked sign up button with only username entered (no passwords) | "Please fill in this field" error pointing at the password box displayed | Pass |
| Sign Up form | Error displayed | Clicked sign up button with username and first password entered (repeat password missing) | "Please fill in this field" error pointing at the repeat password box displayed | Pass |
| Sign Up form | Error displayed, page reloads | Clicked sign up button with username and short passwords entered | page reloads, no error message displayed | Fail |
| Sign Up form | Error displayed, page reloads | Clicked sign up button with username and common passwords entered (tested with "hellohello") | page reloads, no error message displayed | Fail |
| Sign Up form | redirected to home page, welcome message displayed | Clicked sign up button with username and both passwords entered correctly | Redirected to home page with message displaying "Successfully signed in as *username*" | Pass |
| Log In Page |
| Log In button: hover (desktop) | Changes curser to pointer, button changes colour | Hovered mouse over button | Curser changed to pointer, button colour changed | Pass |
| Log In form | Error displayed | Clicked log in button with all fields empty | "Please fill in this field" error pointing at the username box displayed | Pass |
| Log In form | Error displayed | Clicked log in button with only username entered (no password) | "Please fill in this field" error pointing at the password box displayed | Pass |
| Log In form | redirected to home page, welcome message displayed | Clicked log in button with username and password entered correctly | Redirected to home page with message displaying "Successfully signed in as *username*" | Pass |
| Log Out Page |
| Log Out button: hover (desktop) | Changes curser to pointer, button changes colour | Hovered mouse over button | Curser changed to pointer, button colour changed | Pass |
| Log Out button | Redirects to index page, message displayed | Clicked button | Redirected to index page, message displaying "You have signed out." | Pass |
| Index Page |
| Join The Hive button: hover (desktop) | Changes curser to pointer, button changes colour | Hovered mouse over button | Curser changed to pointer, button colour changed | Pass |
| Join The Hive button | Redirects to Sign Up page | Clicked Join The Hive button | Redirected to Sign Up page | Pass |
| Sign Up Now button: hover (desktop) | Changes curser to pointer, button changes colour | Hovered mouse over button | Curser changed to pointer, button colour changed | Pass |
| Sign Up Now button | Redirects to Sign Up page | Clicked Sign Up Now button | Redirected to Sign Up page | Pass |
| Home Page |
| Feature card scroll buttons: hover (desktop) | Changes curser to pointer, button changes colour | Hovered mouse over button | Curser changed to pointer, button colour changed | Pass |
| Feature card | Redirects to the resources detail page | Clicked featured resource | Resource's detail page displayed | Pass |
| Resource card | Redirects to the resources detail page | Clicked resource card | Resource's detail page displayed | Pass |
| Auto load resources | Displays 5 more resources | Scroll to the bottom of the initial page of resources | 5 more resources are added to the bottom of the page | Pass |
| Auto load resources | "No more resources" message displayed | Scroll to the very bottom of the page | Message showing "No more resources" displayed | Pass |
| My Resources Page |
| Resource link: hover (desktop) | Changes curser to pointer, link changes colour | Hovered mouse over link | Curser changed to pointer, link colour changed | Pass |
| Resource link (published resource) | Redirects to the resources detail page | Clicked featured resource | Resource's detail page displayed | Pass |
| Resource link (draft resource) | Redirects to the resources draft preview page | Clicked featured resource | Resource's draft preview page displayed | Pass |
| Resource edit button: hover (desktop) | Changes curser to pointer, button changes colour | Hovered mouse over button | Curser changed to pointer, button colour changed | Pass |
| Resource edit button | Populated form displayed | Clicked edit button on a resource | Pre populated form with the resources details displayed | Pass |
| Resource edit form: automated testing | Resource edited | Edited a resources content individually: title, content, links, key stage and status | Resource edited correctly, verified with automated testing | Pass |
| Resource delete button: hover (desktop) | Changes curser to pointer, button changes colour | Hovered mouse over button | Curser changed to pointer, button colour changed | Pass |
| Resource delete button | Confirm delete displayed | Clicked delete button on a resource | Confirm delete message and button displayed | Pass |
| Resource delete confirmation | Cancel delete, return to resources list | Clicked cancel button | Returned to resources list, resource still displayed in the list | Pass |
| Resource delete confirmation | Return to resources list, resource deleted | Clicked delete button | Returned to resources list, resource deleted from resources list | Pass |
| Resources list (admin user) | List of all published resources displayed | Viewed "my resources" page as an admin user | A list of all published resources displayed with other users resources only displaying a delete button | Pass |
| Resource delete button (admin user) | Confirm delete displayed | Clicked delete button on another users posted resource | Confirm delete message and button displayed | Pass |
| Resource delete confirmation (admin user) | Cancel delete, return to resources list | Clicked cancel button | Returned to resources list, resource still displayed in the list | Pass |
| Resource delete confirmation (admin user) | Return to resources list, resource deleted | Clicked delete button | Returned to resources list, resource deleted from resources list | Pass |
| Create Resource Page |
| Create resource form submit button: hover (desktop) | Changes curser to pointer, button changes colour | Hovered mouse over button | Curser changed to pointer, button colour changed | Pass |
| Create resource form | Error displayed | Clicked submit without entering a title | "Please fill in this field" error pointing at the title box displayed | Pass |
| Create resource form | Images added to the resource | Clicked choose files button and selected multiple images and published the resource | Added images displayed in a carousel in the resource | Pass |
| Resource Detail Page |
| Resource card | No footer links displayed | Viewed a resource without added links | No footer on resource detail card | Pass |
| Resource card link: hover (desktop) | Changes curser to pointer, link changes colour | Hovered mouse over link | Curser changed to pointer, link colour changed | Pass |
| Resource card | No text displayed | Viewed a resource without added text content | No text content on resource detail card | Pass |
| Resource card | Default image displayed | Viewed a resource without added images | Default image of a bee displayed | Pass |
| Resource card download image button | Image opened in separate tab | Clicked download image button | Image opened in a separate tab for saving | Pass |
| Resource card download image button: hover (desktop) | Changes curser to pointer, link changes colour | Hovered mouse over link | Curser changed to pointer, link colour changed | Pass |
| Like button: hover (desktop) | Changes curser to pointer, button changes colour | Hovered mouse over button | Curser changed to pointer, button colour changed | Pass |
| Comment tab: hover (desktop) | Changes curser to pointer | Hovered mouse over button | Curser changed to pointer | Pass |
| Comment tab | Comment form expands | Clicked tab | Comment tab expands to reveal a comment form | Pass |
| Comment submit button: hover (desktop) | Changes curser to pointer, button changes colour | Hovered mouse over button | Curser changed to pointer, button colour changed | Pass |
| Comment edit button: hover (desktop) | Changes curser to pointer, button changes colour | Hovered mouse over button | Curser changed to pointer, button colour changed | Pass |
| Comment edit button | Populates comment form | Clicked edit button on a comment | Comment form populated with the chosen comment | Pass |
