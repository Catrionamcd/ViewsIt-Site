# ViewsIt Site

The ViewsIt site is a social website. There are three different type of users for the site, a super user or administrator, a visitor to the site who chooses not to create a profile on the site and a visitor to the site who creates a user profile so they can contribute to the site. A visitor to the site can view all of the approved posts and channels on the site. Users with a profile on the site can create a new channel or create posts to their own channel or another users channel. Once a channel is created it has to be approved by the administrator before a post can be posted to it. A post has to be approved by the channel owner before it can be viewed by all visitors to the site.

## Multi Screen of the site
Click on [ViewsIt](https://views-it.herokuapp.com/) to see the site.

![ViewsIt](assets/images/ViewsIt-Multi-Device.png)

## Design of the site
### Wireframes
When designing the look and feel of the site I looked to Reddit and Facebook and tried to simulate some of the layout on these sites. 

![All Channels Desktop](assets/images/ViewsIt-AllChannels-DeskTop.png)
![All Channels Mobile](assets/images/ViewsIt-AllChannels-Mobile.png)
![Channel Post Desktop](assets/images/ViewsIt-Post-DeskTop.png)
![Channel Post Mobile](assets/images/ViewsIt-Post-Mobile.png)


### Data Models
There are two database models, the Channel model and the Channel Posts model. The Channel model will store all the details on the channel, the channel topic, description, author, date created, date updated and an approved field, status, which will be set to 0(draft) or 1(published). It will hold a unique key which is a prepopulated slug field, channel topic url.

The Channel Posts model will store all of the details on the post attached to a channel, the post title, post description, post image, post url/link for more information on the post, author, date created, updated date and an approve field. It will hold a unique key which is comprised of the post title and the current date/time. It also holds the channel topic and has on delete cascade so that when a channel is deleted by the channel author all of the posts attached to this chanel will also be deleted automatically.

![Data Model](assets/images/ViewsIt-Data-Model.png)

![Data Model](assets/images/ViewsIt-Database.png)

## User Stories
* Site visitor to view list of approved channels.
* Site visitor to view posts in channels.
* Site visitor to view stats for a post, see how many likes there are.
* Site visitor to use search for author, channel topic or post title.
* Account Registration for site vistor.
* Set up a new channel as a registered user of the site.
* As a super user/administrator add, edit and delete posts.
* As a registered user of the site add, edit and delete posts.
* As an owner of a channel the ability to approve channel posts.
* As a user to like/unlike posts and comments.
* As a super user/administrator the ability to approve a new channel.
* Add an image to channel posts.
* Add a url within a channel posts.

## Features/Functions

## Existing Features

### Registration/Login Forms
* A new layout was created for user registration on the site. A new layout was also created for the login and logout forms.

![alt text](assets/images/Register-User-Screen.png)

![alt text](assets/images/ViewsIt-Login-Screen.png)

![alt text](assets/images/User-Logout-Screen.png)

* Messages will appear on screen to alert the user that their login or logout was successful.
* Alternatively, error mesages will appear if the user has entered invalid data while trying to login or register.

![alt text](assets/images/Login-Message-Screen.png)

* These messages are timed to only appear for a few seconds but can be closed down by clicking the X on the top right hand corner of the message window.


### Navigation Bar

A visitor to the site does not have to be registered to see the approved channels and approved posts on the ViewsIt site.

* A visitor will be presented with a navigation bar that includes :
1. The site logo.
2. A home button.
3. Register or login options.
4. View a list of the approved channels on the site. 
5. Search field.

![alt text](assets/images/Navbar-No-Login.png)

* The site visitor may search for a phrase contained in either Post Title, Post Content, or Post Author.
* Entering a username into the search field allows a user to find all of the posts contributed by that author name.
* Approved posts will be displayed for the site user to view and read.

![alt text](assets/images/Search-By-Author.png)

* If logged in as a registered user there will be more options available on the navigation bar : 

1. Channel manage - manage all the posts, approve or unapprove posts, edit or delete posts attached to the channel created by you.
2. New Channel - functionality to create a new channel.
3. Post - functionality to create a post against any approved channel on the ViewsIt site.

![alt text](assets/images/Register-User-NavBar.png)

* The navigation bar is located at the top of all pages on the site.
* The logo also acts as a home button.

![alt text](assets/images/ViewsIt-Logo.png)

### Channel List

* Lists all approved channels so the user can view approved posts within a specific channel.

![alt text](assets/images/ViewsIt-Channel-List.png)

* Visitors to the site (Unauthenticated login) can also view the approved channel list.

* Author of a channel will also see unapproved posts for the channel that they have created.

![alt text](assets/images/Unapproved-Post.png)

* An unapproved post will be have a shaded background and will have a message 'Post not approved yet' attached to the post.
* The channel author will also have the option to edit or delete this post.

### Channel Manage

* One stop place for all channel management activity.
* Activities that can be accessed via the Channel Management page are: 

1. Delete a channel 
2. Edit a channel 
3. Un-approve posts submitted by users 
4. Approve posts submitted by users

![alt text](assets/images/Channel-Manage-Screen.png)

* Only channels created by the current user logged in are accessible on this page
* If a logged in user has created a new channel, this will be visible on their page with a status of 'Draft'. No other user will be able to see or post to this channel until it has been approved by the super user/administrator of the site.

![alt text](assets/images/Draft-Channel-Screen.png)

* The new channel requested must be approved by the site super user/administrator before the channel changes to status of approved.
* The channel will be approved by the super user/administrator in the Django dashboard.

![alt text](assets/images/Publish-Channel-Dashboard.png)

* Once the channel is approved it will then be possible for users to create posts under this channel.
* If the channel author presses the Delete Channel button a modal confirmation dialog will be displayed.

![alt text](assets/images/Channel-Delete-Screen.png)

* Deleting a channel also removes any posts created under the channel.
* The channel author (person who creates the channel) can also edit the channel detail. Doing so will put the channel back into a status of 'Draft' requiring the super user/administrator's approval again, which means that any posts created under the channel will be hidden from users until the channel has been re-approved.
* The channel author also has the option to un-approve posts that have been created by users of the channel. This will link to the Posts page interface to allow this to happen (see below). The Posts page (when called from Channel Manage page) will only display posts with a status of approved and only from the channel selected. 

![alt text](assets/images/Unapprove-Posts-Screen.png)

* The channel author has the option also to approve posts created by users of the channel. The link in the channel manager displays the amount of un-approved posts in the channel as a link. This will link to the Posts page interface to allow this to happen (see below). The Posts page (when called from Channel Manage page) will only display posts with a status of Draft and only from the channel selected.

![alt text](assets/images/Approve-Post-Screen.png)

* Any posts created by the current logged in user will also show an Edit button to re-edit the post, and a Delete button to delete the post. A modal confirm window is presented if the user presses the Delete button.
* If the user re-edits a post and saves it, the status of that post will be reset back to 'Draft'. This means that no other logged in users or visitors will be able to see the post.
* The posts page also conditionally shows two other buttons for Channel Managers, the Approve button and the Un-approve button. These are only available if the page has been called from the channel manage page and will not be visible to other users. They will also not be visible if the owner of the channel visits the posts page directly, only if invoked via the channel manage page. Refer to channel manage above.
* The posts page indicates via a solid heart icon if the post has been 'liked' and also shows the amount of 'likes' that post has received. 

![alt text](assets/images/ViewsIt-Post-Likes.png)

* Any authenticated user can 'like' an approved post.
### Create a channel
* This option is available to authorised users.

![alt text](assets/images/New-Channel-Screen.png)

* The channel author/owner can enter the channel topic and a short description of what the channel is about.
* The new channel will have a status of 'Draft' until the super user/administrator approves it.
* The channel will ony be visible to the channel author/owner until it is approved.
* Once the channel is approved by the super user/administrator all authenticated users may create posts under this channel.

### Create a Post
* This option is available from the menu bar at the top of the site for authenicated users.
* A person creating a post can enter the following information: 
1. A channel (only shown if selected by home button)
2. A title for the post
3. The post details
4. An image
5. An associated URL that will be available to click when viewing the post. 
* Not all fields are mandatory so the user can choose to skip some if not relevant to their post.

![alt text](assets/images/New-Post-Channel-Select.png)

*  Channel is only shown if selected via the Home button path. 
*  If posting from within a channel (viewing posts from the Channel List path) the channel will not be shown and will be recorded based on the channel the user is currently viewing.
* Images are uploaded and stored in Cloudinary as part of the post save process.
* Once a post is submitted a message is displayed to inform the user that the post has to be approved by the channel author/owner.

![alt text](assets/images/New-Post-Detail.png)

* The new post will be displayed with a shaded background until it is approved by the channel author/owner and will only be visible to post author and channel owner until it is approved. 

![alt text](assets/images/Draft-New-Post.png)


## Functions
Views.py code
* Code in the Views.py carry out various validation checks throughout. For example if code to delete a channel is initiated, then a check is first made that the user is the current channel owner before proceeding with the deletion. 

### Future Features 
* The site could be extended to send notifications of new channels to the super user/administrator for approval. At the moment the administrator has no way of knowing how many new channels are awaiting approval other than looking in the dashboard to see how many have a status of draft. 
* Send notifications of new post to the channel owner for approval.
* Add an image to channel information to make it more appealing.
* Display a thumbnail of the image chosen for a new channel or post as they are created or edited.
* Extend the site to enable users to add comments to the posts that are attached to each channel.


## Technology
### Language Used

* [Python](https://www.python.org) - Python is an interpreted high-level general-purpose programming language. 
* [CSS](https://) - Cascading Style Sheets (CSS) is a style sheet language used for describing the presentation of a document written in a markup language such as HTML. 
* [HTML](https://) - The HyperText Markup Language, or HTML is the standard markup language for documents designed to be displayed in a web browser.
* [JavaScript](https://) - JavaScript is a text-based programming language used both on the client-side and server-side that allows you to make web pages interactive.
### Databases 
* SQLite3 - SQLite is a relational database management system which was used as a test database while developing my webite in GitPod
* PostgreS - PostgreS is a relational database management system which is used on my deployed site in Heroku.

### Other Technologies and Libraries

* [Django](https://www.) - Django is a Python-based free and open-source web framework that follows the model–template–views architectural pattern.
* [GitPod](https://gitpod.io) - Gitpod is an online cloud based IDE. I developed and tested my project using Gitpod. I added and commited changes with messages and pushed to GitHub.
* [GitHub](https://github.com) - GitHub is a provider of Internet hosting for software development and version control using Git.
* [Heroku](https://heroku.com) - Heroku is a cloud platform as a service supporting several programming languages. I used Heroku to deploy and run the project.
* [Cloudinary](https://cloudinary.com) - is used to store the images that areposted to on the channel posts.
* [Google Sheets](https://www.google.com/sheets/about/) - used to plan the data moddels story flow, the story content, story prompts and the next steps for the game. 
* [Diagrams](https://wwww.diagrams.net) - used to create the flowchart for the project.
* [Bootstrap v5.1](https://getbootstrap.com/) - used for the styling and the reposnive design site.
* [Balsamiq](https://balsamiq.com/) - used for creating the wireframes while planning the look of the site. Not all the wireframes are exactly like the end product.


## Testing

Code Validation and Manual Testing can be viewed [here](TEST.md)

## Deployment

The application uses Heroku for deployment:

### Create the application
1. Create the requirements file the Heroku will use to import the dependencies required for deployment: type pip3 freeze > requirements.txt. 

2. Navigate to the [Heroku](https://heroku.com) website
3. Create an account by entering your email address and a password
4. Activate the account through the authentication email sent to your email account
5. Click the new button and select create a new app from the dropdown menu
6. Enter a name for the application which must be unique, in this case the app name is called views-it.
7. Select a region, in this case Europe
8. Click create app
## Attach the PostgreSQL database
1. Click on the resources tab on the horizontal menu bar to add a database
2. In the add-ons box search for Postgres
3. Add Heroku Postgres to the project
## Heroku settings
1. From the horizontal menu bar select 'Settings'.
2. Click on Reveal Config Vars,  this gives us our database url, the connection to our database.
3. Make sure you have your secret key added
4. Make sure the Cloudinary Url is added
5. Tke out any temporary environment variables, such as DISABLE_COLLECT_STATIC.

### Deployment
1. In the top menu bar select 'Deploy'.
2. In the 'Deployment method' section select 'Github' and click the connect to Github button to confirm.
3. In the 'search' box enter the Github repository name for the project. Click search and then click connect to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository which in this case is [ViewsIt-Site](https://github.com/catrionamcd/viewsit-site).
4. Scroll down to select either automatic or manual deployment. For this project automatic deployment was selected. If you wish to select automatic deployment select the button 'Enable Automatic Deploys'. This will rebuild the app every time a change is pushed to Github. If you wish to manually deploy click the button 'Deploy Branch'. The default 'Master' option in the dropdown menu should be selected in both cases.
5. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser. The live deployment of the project can be seen here
6. The app starts automatically and can be restarted by pressing the 'Run Program' button.

## Forking the Repository
If you wish to fork the repository to make changes without affecting the original you can fork the repository

1. Navigate to the [ViewsIt](https://github.com/catrionamcd/viewsit-site) repository
2. Click the 'Fork' button at the top right of the page.
3. A forked copy of the repository will appear in your Repositories page.
## Cloning the Repository
1. On [GitHub](https://github.com) navigate to the main page of the  [ViewsIt](https://github.com/catrionamcd/viewsit-site) repository.
2. Above the list of files click the dropdown code menu.
3. Select the https option and copy the link.
4. Open the terminal.
5. Change the current working directory to the desired destination location.
6. Type the git clone command with the copied URL: git clone https://github.com/catrionamcd/viewsit-site.git.
7. Press enter to create the local clone.

Press enter to create the local clone.

## Credits
### Content
* Reddit Social Network Site - https://www.reddit.com
* Facebook Social Networking Site - https://www.facebook.com 

### Code
* Mastering Django by Nigel George
* Code Institute - https://codeinstitute.net/.com
* Bootstrap - https://getbootstrap.com/docs
* w3schools - https://www.w3schools.com
* stackoverflow - https://www.stackoverflow.com
* pythontutorials - https://www.pythontutorial.net
* geeksforgeeks - https://www.geekforgeek.org
* python - https://docs.python.org
* OrdinaryCoders - https://www.ordinarycoders.com

I would like to credit my family for helping me with the content, the ideas and logic of this project. 
I would like to thank my mentor for being very understanding, helpful and very generous with her time. I would also like to thank our cohort facilitator, Kasia Bogucka, for always going above and beyond to help us.


