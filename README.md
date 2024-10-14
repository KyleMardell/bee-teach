# Bee Teach

Bee Teach is an educational resource sharing app. The Bee Teach app is aimed at teachers, parents and educators in general who want to share and access educational resources in the form of posts. Users can view a lists of resources that other users have shared and view the resource in further detail, including written content and shared images.

[Bee Teach Live App](https://bee-teach-95df758315f5.herokuapp.com/)

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

#### Create Resource
The create resource page is where logged in users can add resources of their own to the Bee Teach App. It has a simple form users can add their resources information, images and link to. The form has text in for the Title (required), text content and a link, a select option for the key stage (required) with options for early years and key stages 1, 2 and 3. Finally users can add multiple images using a file explorer. Once the required fields are filled in, the user can choose to publish a resource or save it as a draft.

#### Resource Detail
When a resource preview is clicked on from the home page, a resource detail page is shown, which displays the entire resource, all its images, content and link if added. Each resource detail page uses a card style design to keep the resource information easy to navigate and read, with the title, author and key stage at the top, followed by the text content, then any images added in a scrolling carousel with navigation arrows, with a link at the bottom of the page.

Below the resource card is the comments section where there is a collapsible comment box for users to add their own comments, and below are any comments left on the resource. If there are no comments, only the collapsible comment box is displayed.

#### Resource Draft
If a resource is saved as a draft when created or edited, a user can view a preview of the resource from the users resources list. This preview is identical to a resource detail page, omitting the comments section. This gives the user a way to see what a resource may look like before publishing or posting.

#### User Resources List
This page displays a simple list of any resources a logged in user has posted. Each list item has a clickable link that takes the user to either the resource detail or draft pages, the date posted and number of comments on that resource. There are also buttons to edit and delete each resource. When a delete button is clicked, a modal confirmation box is displayed and the user must click a confirmation delete button to delete a resource. When editing a resource, a form similar to the create resource form is displayed, pre populated with the chosen resources detail to be edited and again confirmed.  

### Images

[Bee Images](https://www.freepik.com/free-vector/cute-bees-set_18737678.htm#fromView=image_search_similar&page=1&position=1&uuid=0106aee3-1cfd-4e2b-837d-901652d8cfc9) Image by lesyaskripak on Freepik

[Crayola Sheets](https://www.crayola.com/free-coloring-pages/make-and-play/cut-and-color-coloring-pages/)