# Bee Teach

Bee Teach is an educational resource sharing app. The Bee Teach app is aimed at teachers, parents and educators in general who want to share and access educational resources in the form of posts. Users can view a lists of resources that other users have shared and view the resource in further detail, including written content and shared images.

[Bee Teach Live App](https://bee-teach-95df758315f5.herokuapp.com/)

[Bee Teach Repo](https://github.com/KyleMardell/bee-teach)


## Contents


## User Experience

### First time visitor goals
First time users of the Bee Teach app are likely to be educators, seeking resources to use while teaching children. With this in mind, first time visitor goals are to provide free high quality educational resources, in a simple to navigate environment, with a familiar feeling when viewing, posting and editing resources. First time visitors should be impressed by simplicity and usability of the app, the quality of resource and the sense of community, hopefully encouraging them to share resources of their own.

### Returning visitor goals
Returning visitors to the Bee Teach app are expected to be educators, impressed by their initial interaction with the app, looking to find or share more educational resources. Users may also return to the app to get involved in the Bee Teach community by reading and posting comments left on different resources. For returning visitors, the newest or most recently posted resources will be at the front or top of the page, providing them an quick and easy way to view the newest posted resources.

### App use goals
The app use goals are to provide a solution to a real-world problem, providing free educational resources, through a simple, familiar feeling, easy to navigate web app. The app should provide educators with a way to find free resource materials, share resources of their own through images, written content or links, and get involved in the Bee Teach community by posting comments. Overall the app should be a helpful free tool for all educators.


## Design

### Concept
My inspiration for the concept of the Bee Teach app came from my partner, who is a nursery teacher and often spends hours on an evening searching for fun resources to educate and entertain the classes children. Resources could be lesson plans, work/play-sheets, craft ideas, stories, or alternative lesson ideas. This meant each "educational resource" would commonly have written content, images or a mix of both, and when designing an app for this purpose, having a mixture of content available was a high priority, especially including multiple images per resource. I wanted to create an app where teachers and eductors could share resources they have created with a community, creating a bank of free resources, created by the Bee Teach community. I also wanted users to be able to like or comment on resources so they could show each other appreciation and share ideas with each other in a conversational style. This way users can see other educators positive reactions to their created or shared resources.

### Database
When designing the Bee Teach app, creating a solid database schema was paramount as I wanted to avoid making large changes or unnecessary migrations later in the development phase. With this in mind, I designed my app using the wire-frame software [Excalidraw](https://excalidraw.com/) to help envision what pages the app would need, thus helping me to understand the models my database would require. I created my [Database Schema](/docmedia/wireframes/db-schema.png) using the same wire-frame software, checking multiple times before finalising my plans and creating the database models. 

### Functionality
The functionality of the Bee Teach app needed to reflect the core idea of sharing educational resources and provide both a quick way to find and obtain resources, as well as being able to easily share resources. With this in mind, the user needed only a few core functions in the app: view a list of resources posted by other users, post their own resources, view a list of their own posted resources, and finally be able to edit or delete resources they have posted. 

To extend the core functionality and allow users to give support and feedback to other users resources, I also wanted to add the ability to like or comment on a resource. This would become a more social media based approach, providing the familiarity I wanted to app to have, and create a fuller experience for educators when sharing resources and ideas. This kind of functionality meant the users need the ability to create an account with an associated username, and therefore some form of authorisation would also be needed.

As the user will need to make an account and sign in, this meant I could create a hero page introducing new users to the app. The hero page needed to inform new users of the Bee Teach apps purpose, explain its core ethos, display some example posts and have a call to action to encourage new users to sign up. 
In order to keep the app simple and familiar feeling, once a user is logged in they should be instantly shown a list of the most recent resources and be able to scroll through them. This meant I needed to think about the apps performance, as loading potentially a large amount of resources in one go would not be ideal, and therefore the user would need to be able to load resources upon request.

Resources themselves needed to be able to hold different types of information or data depending on what that resource is, and not all data may be needed for all resources. This meant the only mandatory resource information would be the title and the key-stage (which also has a default value) for simplicity. The other types of data in a resource could then be a combination of text, links or images, all of which are optional. Each resource can be either posted immediately or saved as a draft.

The user should be able to view a list of resources they have posted or saved as draft. The list simply comprises of the resource titles and creation dates, each linking to the posted or draft resource page. This is where the user can edit or delete a resource. If the user deleted a resource, they are shown a confirmation notice and must click a second delete button to permanently delete the resource. When editing a resource, a pre populated form should be displayed at the top of the page and the user can edit the resource information before saving.

Users can comment on resources when viewing them in detail, or once clicked on to view its page. Once a comment has been posted, edit and delete buttons for the users posted comments are then attached to each comment. Similarly to deleting a resource, when deleting a comment the user must also confirm the deletion. When editing a comment, the form used to post the comment on tha particular resource should be pre populated with the comment for editing. A user can also like a resource when viewing it in detail. Liking a resource should be as simple as pressing a single like button to both like and unlike a resource.

Using this functionality brief, I then created some of the [User Stories](/docmedia/wireframes/user-stories.png) in a document before transferring to the Github project later, as they would help in the wire frame design process.  


### Wireframes
When beginning to visualise the Bee Teach app, I used the wire-framing web app [Excalidraw](https://excalidraw.com/) to create initial rough designs of the pages I would need, so I had a guide to follow when developing the app. As I began by creating these wire frames I did not follow them exactly, but they were a good starting point and guide. Using an agile methodology when developing meant the app was fluid in design and the end product or mvp could change from the original designs and some may not have being used at all, that being said, they were still very helpful when developing the app.

Here are the initial wire-frames I created.
- [Hero Page](/docmedia/wireframes/wireframe-hero.png)
- [Home Page](/docmedia/wireframes/wireframe-home.png)
- [Sign-Up Page](/docmedia/wireframes/wireframe-signup.png)
- [Log-In Page](/docmedia/wireframes/wireframe-login.png)
- [Log-Out Page](/docmedia/wireframes/wireframe-logout.png)
- [Resources](/docmedia/wireframes/wireframe-posts.png)
- [Create Resource](/docmedia/wireframes/wireframe-createpost.png)
- [User Resources](/docmedia/wireframes/wireframe-usersposts.png)
- [About Page](/docmedia/wireframes/wireframe-about.png)
- [Profile Page](/docmedia/wireframes/wireframe-signup.png)

### Colour Scheme
When it came to choosing a [Colour Scheme](/docmedia/designs/colour-scheme.png) for the app, I wanted to keep the colours quite muted and stick to one colour, creating a brand associated colour. Using a single colour also helps to maintain the focus on the resources or content of the app, as using a large number of different colours can sometimes distract from the user posted content, and I wanted the resources to be the focal point of the Bee Teach app. In the end I chose an all green colour scheme, green being a colour invoking feelings of positivity and nature. I also chose a yellow for accenting and an off white that i could use for light coloured text.

### Typography
For the typography I wanted To use a chunky style font I could use for things such as headings and buttons, and a contrasting written style font for things such as main content and comments. Both fonts needed to be screen friendly and therefore I chose san-serif fonts to use in the app. 

I used the [Farsan Font](/docmedia/designs/farsan-font.png) and [Concert One Font](/docmedia/designs/concert-font.png) from [Google Fonts](https://fonts.google.com/).

### Agile & Kanban
When developing the app I wanted to use an agile methodology to maintain structure and vision while being flexible to changes throughout the design and build process. I used githubs project board and issues to create a kanban board with story point issues for each part of the development process. I found using both an agile methodology and an organised project board helped vastly in staying on target, knowing what tasks needed completing, and embracing design or functionality changes.

To maintain a reasonable time scale for each part of the development process, I used githubs milestones and added sprint labels to each issue. This way I could easily keep track of har far along the development process I was, and through using an agile methodology could increase or reduce the workload for each sprint or milestone. As this was my first time using these methods of working, I had to use my best judgement to assign a story point value to tasks and decide how much work each feature would require. Although not all predictions worked out exactly, I still found it useful to visually see how much time I might need to spend on tasks, versus the amount of time I had for each sprint.

### User Stories & Issues
Before beginning to write any code, I set up the user stories I had written in the design phase each as an issue using a template I created. I then used custom labels to categorise the user story and add a predicted story point value. This meant I could quickly see how many of each issue type there were and begin to plan the amount of time I might need to spend on each story point. I also made sure to add a short description and acceptance criteria for each user story to help know when the issue could be closed.
To keep track of the design and documentation stages, I also created issues added to my kanban board. This meant I had a visual representation of the design processes, helping to make sure something wasn't easily overlooked.

The user stories used in the project board, defined the features of the app and meant each feature had a clear objective. In some cases multiple user stories were satisfied in a single feature, although that feature would be a potentially large section of the app. For example the user story of being able to view a list of resources, meant that resources must be able to be created, and have an associated card preview, which are both other examples of user stories. 

Even though I knew I would not have time to create some of the features I added issues or user stories for, I still wanted to add them to the project for two main reasons. Firstly, incase I found I had the time to add further features after creating the main MVP functionality, and secondly for if I choose to revisit and further develop the app in the future. This way I have reference issues to create additional functionality and continue development down the line.

## Features

### Existing Features

#### Favicon 
The [Favicon](/static/favicon/favicon.ico) uses colours from the colour theme, simply with the word "Bee" to provide a quick visual reference to the bee teach app.

#### Nav Bar
The nav bar for the Bee Teach app has the Logo Text as a link to the home page, and directs to the hero page or logged-in home page depending if the user is logged in or not. The menu is also both responsive to a user being logged in and screen size. If a user is not logged in, the menu has options to sign up or log in as well a a home page link. If the user is logged in, the menu displays links to create a resource, view a list of resources as well as a home page link. Finally if the user is an admin user, they are also shown a link to the admin page.
If the screen size is of that or a phone or tablet sized device, a burger style dropdown menu is shown, otherwise for larger screens, the page links are shown in a horizontal list to the right of the menu bar.

- [Nav Mobile Collapsed](/docmedia/designs/screenshots/nav-mobile-collapse.png)
- [Nav Mobile Open](/docmedia/designs/screenshots/nav-mobile-open.png)
- [Nav Desktop](/docmedia/designs/screenshots/nav-desktop.png)

#### Hero Page
The hero page or index page of the Bee Teach app serves to introduce and entice users to join the app. An opening hero section covers the top section of the page on a users first visit, along with a call to action button linking to the sign up page. This makes is easy for the user to see some initial information and be able to instantly sign up. Scrolling down the page, there is further information about the app, broken up by images of the Bee Teach default mascot image before 4 of the most recent resources posted by existing users as an example of the kinds of resources the Bee Teach users share. This way, if a user is undecided if they wanted to sign up the first time and return to the site again, there will be updated example resources on each visit. Finally there is another call to action button to further urge the visitor to sign up.

The hero page is fully responsive across all screen sizes, with the example posts shifting position depending on screen size, while still keeping a consistent feeling over multiple devices.

- [Mobile Hero Page](/docmedia/designs/gifs/mobile-hero.gif)
- [Tablet Hero Page](/docmedia/designs/gifs/tablet-hero.gif)
- [Desktop Hero Page](/docmedia/designs/gifs/desktop-hero.gif)

#### Sign Up, Log In and Log Out
In order for the user to create an account I user Django's built in authorisation, and adjusted the sign up, log in and log out pages and added styles to match the Bee Teach apps theme while still remaining simple and intuitive. All the log in pages are fully responsive across all screen sizes while keeping consistent in style and layout.

- Sign Up
    - [Mobile](/docmedia/designs/screenshots/signup-mobile.png)
    - [Tablet](/docmedia/designs/screenshots/signup-tablet.png)
    - [Desktop](/docmedia/designs/screenshots/signup-desktop.png)
- Log In
    - [Mobile](/docmedia/designs/screenshots/login-mobile.png)
    - [Tablet](/docmedia/designs/screenshots/login-tablet.png)
    - [Desktop](/docmedia/designs/screenshots/login-desktop.png)
- Log Out
    - [Mobile](/docmedia/designs/screenshots/logout-mobile.png)
    - [Tablet](/docmedia/designs/screenshots/logout-tablet.png)
    - [Desktop](/docmedia/designs/screenshots/logout-desktop.png)

#### Home Page
The home page is only shown when a user is logged in to the Bee Teach app. This page has a features section at the top of the page where admin users can highlight resources in a scrolling carousel. Each feature can have its own title and content as well as a resource preview that links to the resource when clicked. Below the features section is a list of all resources from newest to oldest, although initially only 5 resources are displayed, when scrolling down the page, further resources are automatically loaded and rendered on the page until no more resources are available. Each resource is shown as a preview displaying its title, all attached images auto scrolling, its author and if there are any comments, a comment bubble icon with the number of comments on that resource. This keeps the home page a simple and easy way to view all resources, while keeping load times low, as well as highlighting featured resources.

- [Mobile](/docmedia/designs/gifs/mobile-home.gif)
- [Tablet](/docmedia/designs/gifs/tablet-home.gif)
- [Desktop](/docmedia/designs/gifs/desktop-hero.gif)

#### Create Resource
The create resource page is where logged in users can add resources of their own to the Bee Teach App. It has a simple form users can add their resources information, images and link to. The form has text in for the Title (required), text content and a link, a select option for the key stage (required) with options for early years and key stages 1, 2 and 3. Finally users can add multiple images using a file explorer. Once the required fields are filled in, the user can choose to publish a resource or save it as a draft.

- [Mobile](/docmedia/designs/gifs/tablet-create-resource.gif)
- [Tablet](/docmedia/designs/gifs/tablet-create-resource.gif)
- [Desktop](/docmedia/designs/gifs/desktop-create-resource.gif)

#### Resource Detail
When a resource preview is clicked on from the home page, a resource detail page is shown, which displays the entire resource, all its images, content and link if added. Each resource detail page uses a card style design to keep the resource information easy to navigate and read, with the title, author and key stage at the top, followed by the text content, then any images added in a scrolling carousel with navigation arrows, with a link at the bottom of the page.

Below the resource card is the comments section where there is a collapsible comment box for users to add their own comments, and below are any comments left on the resource. If there are no comments, only the collapsible comment box is displayed.

- [Mobile](/docmedia/designs/gifs/mobile-resource-detail.gif)
- [Tablet](/docmedia/designs/gifs/tablet-resource-detail.gif)
- [Desktop](/docmedia/designs/gifs/desktop-resource-detail.gif)

#### Resource Draft
If a resource is saved as a draft when created or edited, a user can view a preview of the resource from the users resources list. This preview is identical to a resource detail page, omitting the comments section. This gives the user a way to see what a resource may look like before publishing or posting.

- [Mobile](/docmedia/designs/screenshots/mobile-draft.png)
- [Tablet](/docmedia/designs/screenshots/tablet-draft.png)
- [Desktop](/docmedia/designs/screenshots/desktop-draft.png)

#### User Resources List
This page displays a simple list of any resources a logged in user has posted. Each list item has a clickable link that takes the user to either the resource detail or draft pages, the date posted and number of comments on that resource. There are also buttons to edit and delete each resource. When a delete button is clicked, a modal confirmation box is displayed and the user must click a confirmation delete button to delete a resource. When editing a resource, a form similar to the create resource form is displayed, pre populated with the chosen resources detail to be edited and again confirmed. 

- [Mobile](/docmedia/designs/gifs/mobile-resource-list.gif)
- [Tablet](/docmedia/designs/gifs/tablet-resource-list.gif)
- [Desktop](/docmedia/designs/gifs/desktop-resource-list.gif)

#### Admin Page
The admin page uses the built in Django admin features. The only reason to use the admin panel would be to delete or ban a user, delete images or add a feature. In the future I wish to add the ability to add features from within the app for admin users instead of the admin panel. Even though I did not have enough time to add this ability to the app, I still wanted to add featured resources to the MVP.

#### 404 & 500 Pages
In order to keep the user within the app if either a 404 - page not found, or 500 - server error occurs I have created simple 404 and 500 pages. They simply show the error number and message on the page, allowing the user to still use the navigation menu to return to a valid page. I considered adding a 403 - Access forbidden page, but felt I used enough defensive programming to avoid needing this page.

### Defensive Programming
In order to keep the app and users accounts safe, I added certain defensive programming measures. Firstly the use of authorisation for users meant I could ensure users have to be logged in to access the main features of the app, and guest users can only view the home page with examples of the apps content. With the use of authorisation I could also add defensive programming to users resources and comments, meaning users cannot edit, delete or otherwise manipulate content not created by themselves. This is true even if a user tries to enter a URL not accessible by themselves, such as the URL to edit another users posted resource.

As django is a server run application, that means all the main functions of the app are run server side, again adding to defensive programming by minimising the amount of data processed in the front end. In each of the view functions I have ensured that only logged in users can access the crud functionality of the app, and when doing so there are coded measures to verify that only the creator of any content can edit or delete that content. Other than admin superusers who can delete any published content for basic moderation safety.

### Future Features
As I was planning and developing the Bee Teach app, I had to keep scope at the front of my mind as I found it had the potential to be very large and have a lot of features. With this thought, I tried to keep the MVP scope as realistic as possible for the timescale, while also leaving room for growth in the future. Here are some of the features I plan to add in the future to create a fuller experience when visiting the Bee Teach app.

#### Profile Page
In the future I would like to add a profile page for each user. I originally added a profile page to my designs and plans, although due to time constraints I knew this was a "nice to have" feature. This page would let users add their own profile details such as their name, about section, their posted resources and potentially resources they have liked, creating more depth to the app and letting users easily share more information about themselves or find all the resources posted by a single user.

#### Featured Resources
As mentioned in the admin page section, I wish to add the ability for admin users to create featured resources from within the app, or in the front end. This would mean creating a page for admin users to view, edit and delete currently featured resources, as well as a form to add new featured resources. To extend the functionality I would also like to add time frames to featured resources, meaning an admin user could schedule a feature to run for a set length of time or on a specific date and time.

#### Search Function
If the app became populated with a large number of resources, it would be helpful to be able to search for resources. Each resource currently has an associated ket stage that is shown when a resource is viewed in detail and I added this detail to help create a search function where users could filter resources by key stage and easily see all the resources aimed at a certain age range. I would also like to add a word search function so users could search for a resource containing a certain word. For example a user could search "Bee" to find all resources about bees.

#### User Comments
I would also like to add a page or section where the user could see all comments they have left on other users resources in a single list, much like the current user resources list. This way a user could not only see all their comments in a single place, but they could also edit or delete those comments.
In my database schema I added the ability to comment on an existing comment but when creating the database I simplified comments to only apply to resources to stay in the scope of the project. In the future this is a feature I would like to add to create more of a conversational feeling in the comments section. 

#### Media Types
As resources are the main feature of the app, I would also like users to be able to add multiple types of media such as PDF files, videos or other media types. This would extend the amount and types of resources that users can share within the app.

#### Design features
Although I believe the design, layout and colour schemes currently suit the app, I also think they could be improved and would like to consider some re-designing of the app. This would be things such as ensuring forms fill a single screen or viewport height to make the design feel slightly more intuitive. I also believe the colour scheme of the app could be revised and improved and may consider this in the future too.

## Testing
Testing can be found in the [testing file](/TESTING.md) and features manual and automated testings, validation and accessibility testing.

## Deployment
When deploying the Bee Teach app there are multiple steps that must be taken to ensure the app is functioning correctly. A pre requisite is there needs to be a functioning database. In this case I used one of the [Code Institute](https://codeinstitute.net/) provided PostgreSQL databases. If there is an active database, the app can then be reproduced by cloning the repo and deploying locally or on a hosting service, in this case Heroku. The steps taken to deploy the app are detailed below.

### GitHub

#### Fork Repository

- To fork the repository
    - Login or Sign Up to GitHub
    - Navigate to the repository for this project [Bee Teach](https://github.com/KyleMardell/bee-teach)
    - Click the "Fork" button on the top right of the page

#### Clone Repository

- To clone the repository
    - Login or Sign Up to GitHub
    - Navigate to the repository for this project [Bee Teach](https://github.com/KyleMardell/bee-teach)
    - Click on the "Code" button
    - Select how you would like to clone (HTTPS, SSH, or GitHub CLI)
    - Copy your chosen link
    - Open the terminal of your code editor or IDE
    - Change the current working directory to the location you want to use for the cloned directory
    - Type "git clone" into the terminal followed by the copied link and press enter.

### Django Settings

- Django Settings
    - Navigate to the settings.py file of the Bee Teach Django Project
    - Locate the "ALLOWED_HOSTS" and replace the first entry with your own development server URL (in this case, starting "8000-kylemardell-beeteach")
    - Locate the "CSRF_TRUSTED_ORIGINS" and replace the first entry with your own development server URL (in this case, starting "8000-kylemardell-beeteach")
    - If deploying locally install the requirements with the command "pip install -r requirements.txt" in the terminal for your local development environment.

- ENV File
    - In order to run the app locally, you will need to create a file named 'env.py' in the base project folder or same directory as the requirements.txt file.
    - add 'import os' at the top of the file/page
    - add the code 'os.environ.setdefault("DATABASE_URL", "postgres://my_database_url")', making sure to add your own database url in place of 'my_database_url'
    - add the code 'os.environ.setdefault("SECRET_KEY", "my_secret_key")', making sure to add your own secret key in place of 'my_secret_key'
    - add the code 'os.environ.setdefault("CLOUDINARY_URL", "cloudinary://my_cloudinary_url")', making sure to add your own cloudinary url in place of 'my_cloudinary_url' described below

### Cloudinary

- In order to set up the Bee Teach app, an image hosting service is needed to host the images. In this case I used [Cloudinary](https://cloudinary.com/).
    - Login or sign up with your [Cloudinary](https://cloudinary.com/) account
    - Navigate to the dashboard
    - Click "Go to API Keys" at the top of the page
    - Locate the "API environment variable" / Cloudinary URL at the top of the page
    - Copy your "API Key" and "API Secret" into the Cloudinary URL for use in the Heroku settings

### Heroku

- Deploy to Heroku
    - Login or sign up with your [Heroku](https://heroku.com) account
    - Navigate to the dashboard
    - Click "New" at the top right of the screen, select "Create new app"
    - Enter a unique name (I used BeeTeach)
    - Choose a region
    - Click "Create app"
    - Navigate to the "Settings" tab
    - Navigate to "Buildpacks"
    - Click "Add buildpack"
    - Add "Python" as a buildpacks
    - Click "Reveal Config Vars"
    - Add a new config var with key "CLOUDINARY_URL" and the value from your Cloudinary URL detailed above, beginning "cloudinary://"
    - Add a new config var with key "DATABASE_URL" and add the URL of your database, in this case beginning "postgres://"
    - Add a new config var with key "SECRET_KEY" and add your own secret key, e.g. "th15-15-4-53CR3T-K3y"
    - Navigate to the "Deploy" tab
    - Select GitHub as deployment method
    - Authenticate with GitHub account
    - Search for repo name (BeeTeach), click "Connect"
    - Optionally enable "Automatic deploys"
    - Click "Deploy branch" under "Manual Deploy" ensuring main branch is selected

## Credits

### Django
In order to learn more about how to use Django and find out how to use features such as pagination, template snippets and overriding admin templates, I used the [Django Docs](https://docs.djangoproject.com/). When coding the functionality for an admin user, I needed to get a list of all the users resource and any resources published by other users. I learned about the django Q object using [this reference](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/query_relatedtool.html) to learn how to get the list of all resources in a single query.
I referenced the django blog practice project from [Code Institute](https://codeinstitute.net/) to set up the initial project and app before expanding.

### Javascript
When writing the javascript for the project, I referenced a combination of examples from my previous projects, and the django blog practice project from [Code Institute](https://codeinstitute.net/)

### Images
The default placeholder Bee image is from [Freepik](https://www.freepik.com/free-vector/cute-bees-set_18737678.htm#fromView=image_search_similar&page=1&position=1&uuid=0106aee3-1cfd-4e2b-837d-901652d8cfc9) - Image by lesyaskripak

### Resources
There are resources added by my peers in teaching or educational professions. Although this is the purpose of the app, I still wanted to mention there may be images or links to external sources shared, not owned by myself or the publisher. All shared resources should be used for educational purposes only and be either owned by the user or free to use.

### Testing
When writing unit tests, I wanted to test messages for correct feedback and found the following [Stack Overflow](https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages/14909727) thread on testing Django messages. I used this method in my testing to check for correct message feedback when carrying out certain operations in the app.
