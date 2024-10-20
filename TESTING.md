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
When writing unit tests, I used the built in Django test suite. There are 2 python testing files, [test forms](/post/test_forms.py) and [test views](/post/test_views.py), each of which test the respective forms or views. I used the [Django Testing Documentation](https://docs.djangoproject.com/en/5.1/topics/testing/tools/), to better understand which tests I needed to use and tried to implement as many tests as I could. I also used a [Stack Overflow](https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages/14909727) thread to help in creating tests for feedback messages.

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
        - 

## Manual Testing

## User Testing