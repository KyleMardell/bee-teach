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
When designing the Bee Teach app, creating a solid database schema was paramount as I wanted to avoid making large changes or unnecessary migrations later in the development phase. With this in mind, I designed my app using the wire-frame software [Excalidraw](https://excalidraw.com/) to help envision what pages the app would need, thus helping me to understand the models my database would require. I created a database schema using the same wire-frame software, checking multiple times before finalising my plans and creating the database models. 
[Database schema](/docmedia/wireframes/db-schema.png)

### Functionality
The functionality of the Bee Teach app needed to reflect the core idea of sharing educational resources and provide both a quick way to find and obtain resources, as well as being able to easily share resources. With this in mind, the user needed only a few core functions in the app: view a list of resources posted by other users, post their own resources, view a list of their own posted resources, and finally be able to edit or delete resources they have posted. To extend the core functionality and allow users to give support and feedback to other users resources, I also wanted to add the ability to like or comment on a resource. This would become a more social media based approach, providing the familiarity I wanted to app to have, and create a fuller experience for educators when sharing resources and ideas. This kind of functionality meant the users need the ability to create an account with an associated username, and therefore some form of authorisation would also be needed.

As the user will need to make an account and sign in, this meant I could create a hero page introducing new users to the app. The hero page needed to inform new users of the Bee Teach apps purpose, explain its core ethos, display some example posts and have a call to action to encourage new users to sign up. 
In order to keep the app simple and familiar feeling, once a user is logged in they should be instantly shown a list of the most recent resources and be able to scroll through them. This meant I needed to think about the apps performance, as loading potentially a large amount of resources in one go would not be ideal, and therefore the user would need to be able to load resources upon request.
Resources themselves needed to be able to hold different types of information or data depending on what that resource is, and not all data may be needed for all resources. This meant the only mandatory resource information would be the title and the key-stage (which also has a default value) for simplicity. The other types of data in a resource could then be a combination of text, links or images, all of which are optional. Each resource can be either posted immediately or saved as a draft.
The user should be able to view a list of resources they have posted or saved as draft. The list simply comprises of the resource titles and creation dates, each linking to the posted or draft resource page. This is where the user can edit or delete a resource. If the user deleted a resource, they are shown a confirmation notice and must click a second delete button to permanently delete the resource. When editing a resource, a pre populated form should be displayed at the top of the page and the user can edit the resource information before saving.
Users can comment on resources when viewing them in detail, or once clicked on to view its page. Once a comment has been posted, edit and delete buttons for the users posted comments are then attached to each comment. Similarly to deleting a resource, when deleting a comment the user must also confirm the deletion. When editing a comment, the form used to post the comment on tha particular resource should be pre populated with the comment for editing.
A user can also like a resource when viewing it in detail. Liking a resource should be as simple as pressing a single like button to both like and unlike a resource.
Using this functionality brief, I then created some of the user stories in a document before transferring to the Github project later, as they would help in the wire frame design process. [User Stories](/docmedia/wireframes/user-stories.png)

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
When it came to choosing a colour scheme for the app, I wanted to keep the colours quite muted and stick to one colour, creating a brand associated colour. Using a single colour also helps to maintain the focus on the resources or content of the app, as using a large number of different colours can sometimes distract from the user posted content, and I wanted the resources to be the focal point of the Bee Teach app. In the end I chose an all green colour scheme, green being a colour invoking feelings of positivity and nature. I also chose a yellow for accenting and an off white that i could use for light coloured text.

[Colour Scheme](/docmedia/designs/colour-scheme.png)

## Features

###



### Images

[Bee Images](https://www.freepik.com/free-vector/cute-bees-set_18737678.htm#fromView=image_search_similar&page=1&position=1&uuid=0106aee3-1cfd-4e2b-837d-901652d8cfc9) Image by lesyaskripak on Freepik

[Crayola Sheets](https://www.crayola.com/free-coloring-pages/make-and-play/cut-and-color-coloring-pages/)