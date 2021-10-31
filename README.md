# ViewsIt Site

The ViewsIt site is a social website. There are three different type of users for the site, a super user or administrator, a visitor to the site who chooses not to create a profile on the site and a vistor to the site who creates a user profile so they can contribute to the site. A visitor to the site can view all of the posts and channels on the site. Users can create a new channel or create posts to their own channel or another users channel. Once a channel is created it has to be approved by the administrator before a post can be posted to it. A post has to be approved by the channel owner before it can be viewd by all visitors to the site.

## Multi Screen mock-up of the site
![alt text]()

## Design of the site
### Flowchart
![alt text]()

## Features/Functions
* As a visitor to the site you can view a approved list of channels on the site
* View posts on Channel
### Existing Features

* The user is presented with a 
![alt text]()


### Future Features 
* The site could be extended to 

## Data Model


![alt text]()


### Development of Data Model

When I first approached this project 

## Technology
### Language Used

* [Python](https://www.python.org) - Python is an interpreted high-level general-purpose programming language. I used Python to access the data in Google Sheets and run the game.

### Other Technologies and Libraries

* [GitPod](https://gitpod.io) - Gitpod is an online cloud based IDE. I developed and tested my project using Gitpod. I added and commited changes with messages and pushed to GitHub.
* [GitHub](https://github.com) - GitHub is a provider of Internet hosting for software development and version control using Git.
* [Heroku](https://heroku.com) - Heroku is a cloud platform as a service supporting several programming languages. I used Heroku to deploy and run the project.
* [Google Chrome Browser](https://www.google.com/intl/en_ie/chrome/) - was used to view the game.
* [Google Cloud Platform](https://cloud.google.com) - was used to set up the API's for the project.
* [Google Sheets](https://www.google.com/sheets/about/) - used to store the story flow, the story content, story prompts and the next steps for the game. 
* [Diagrams](https://wwww.diagrams.net) - used to create the flowchart for the project.
## API
Set up API to access the data in the Google Sheets

* Go to the [Google Cloud Platform](https://cloud.google.com) page.
* Click on 'Select a Project' button.
* Select 'New Project' and enter project name, 'AdventuresOfAlice' and click 'Create'
* Select project to bring you to the project page.
* Select the 'APIs & Services' option from the side menu.
* Select 'Library' to enable two APIs, Google Drive to get credentials to access the Google files and the second API will be to Google Sheets.
* In the search bar enter 'Google Drive' and select it from the list.
* Click the 'Enable' button.
* From the "Which API are you using?" choose Google Drive API.
* For the "What data will you be accessing?" select Application Data.
* For the "Are you planning to use this API with Compute Engine, Kubernetes Engine, App Engine, or Cloud Functions?" select No, I'm not using them.
* Click Next
* Enter Service Account details, 'AdventuresOfAlice' and click 'Create.
* For Role click 'Editor' and click 'Continue'.
* On the next page click on the Service Account that was created.
* On the next page click on 'KEYS' tab.
* Click on 'Add' key and 'Create New Key'
* Select 'JSON' and click 'Create'
* To select the Google Sheets API, go back to the 'Library' and search for 'Google Sheets'.
* Select 'Google Sheets API' and click 'Enable'.

## CREDS.JSON

* Copy the credentials file created into my gitpod repository and rename it to 'creds.json'
* Ensure the 'creds.json' file is added to the 'gitigore' file as it should not be pushed to GitHub.
* Take a copy the email address generated from the creds.json file.
* In the Google Sheets click 'Share' button and paste in the email address.
* Select 'Editor' and untick 'Notify People, then click 'Share'.


## Testing
### Manual Testing
* Ensure that API is working and that my code is able to access the data in the google sheets. I initially tested this by putting two rows of data in the google sheet and printing the data to screen.
* Test the validation of a player name entered. If the player name is not entered, an error message should appear and the user will be prompted for a name again.
* Test validation against the reponses in the data model. If a response is entered by the player other than the responses in the google sheet an error message should display and the player is prompted again with the same question.
* Test that the correct story content and prompt is appearing for the current step of the game.
* Make sure that the correct value in the next step is moved into the current step when the player has entered a valid response for that step.
* If there is data in the output column ensure that the correct output content is printing.
* If the next step is a 'Win' or 'Lose' step make sure that the correct ouptut is printed to the screen. Also test that the correct accummulated tallies of wins and losses are printed.
* Ensure that the player is promted to play again if the next step is 'Win' or 'Lose'.
* If the data in the data structure is not setup properly, ensure that an informative error message should appear with the current step of the game printed on screen.
* Test that the flow of the story makes sense, that for each step the next step is a valid, realistic move.
* Used the Google Sheets data as a checklist to test that all of the next steps and outputs were correct and the flow of the game was correct.


### Validator Testing

PEP8 online check
http://pep8online.com
![alt text](assets/images/PEP8-Checker.png)

* No errors were found in the code 


## Bug Fixes

* 

## Deployment

The application uses Heroku for deployement

### Create the application
1. Create the requirements file the Heroku will use to import the dependencies required for deployment: type pip3 freeze > requirements.txt. 

2. Navigate to the [Heroku](https://heroku.com) website
3. Create an account by entering your email address and a password
4. Activate the account through the authentication email sent to your email account
5. Click the new button and select create a new app from the dropdown menu
6. Enter a name for the application which must be unique, in this case the app name is adventures-of-alice
7. Select a region, in this case Europe
8. Click create app
## Heroku settings
1. From the horizontal menu bar select 'Settings'.
2. In the buildpacks section, where further necessary dependencies are installed, click 'add buildpack'. Select 'Python' first and click 'save changes'. Next click 'node.js' and then click 'save changes' again. The 'Python' buildpack must be above the 'node.js' buildpack'. They can be clicked on and dragged to change the order if necessary.
### Deployment
1. In the top menu bar select 'Deploy'.
2. In the 'Deployment method' section select 'Github' and click the connect to Github button to confirm.
3. In the 'search' box enter the Github repository name for the project. Click search and then click connect to link the heroku app with the Github repository. The box will confirm that heroku is connected to the repository which in this case is [Adventures of Alice](https://github.com/catrionamcd/adventures-of-alice).
4. Scroll down to select either automatic or manual deployment. For this project automatic deployment was selected. If you wish to select automatic deployment select the button 'Enable Automatic Deploys'. This will rebuild the app every time a change is pushed to Github. If you wish to manually deploy click the button 'Deploy Branch'. The default 'Master' option in the dropdown menu should be selected in both cases.
5. When the app is deployed a message 'Your app was successfully deployed' will be shown. Click 'view' to see the deployed app in the browser. The live deployment of the project can be seen here
6. The app starts automatically and can be restarted by pressing the 'Run Program' button.

## Forking the Repository
If you wish to fork the repository to make changes without affecting the original you can fork the repository

1. Navigate to the [Adventures of Alice](https://github.com/catrionamcd/adventures-of-alice) repository
2. Click the 'Fork' button at the top right of the page.
3. A forked copy of the repository will appear in your Repositories page.
## Cloning the Repository
1. On [GitHub](https://github.com) navigate to the main page of the  [Adventures of Alice](https://github.com/catrionamcd/adventures-of-alice) repository.
2. Above the list of files click the dropdown code menu.
3. Select the https option and copy the link.
4. Open the terminal.
5. Change the current working directory to the desired destination location.
6. Type the git clone command with the copied URL: git clone https://github.com/catrionamcd/adventures-of-alice.git.
7. Press enter to create the local clone.

Press enter to create the local clone.

## Credits
### Content
* Reddit Social Network Site - https://www.reddit.com
* Facebook Social Networking Site - https://www.facebook.com 
### Code
* [w3schools] - https://www.w3schools.com
* [stackoverflow] - https://www.stackoverflow.com
* [pythontutorials] - https://www.pythontutorial.net
* [analyticsvidhya] - https://www.analyticsvidhya.com
* [geeksforgeeks] - https://www.geekforgeek.org
* [python] - https://docs.python.org

* I would like to credit


