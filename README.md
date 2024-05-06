# Goal-Mine (An everyday task manager)
![Goal-Mine](documentation/responsive.png)

- The Github project can be found [here](https://github.com/Dym077/goal-mine) 
- The live link is found via [this link](https://goal-mine-8c569f15a81b.herokuapp.com/)


## Why a To-do-list app?

### The Idea behind it all
- My initial idea of building a web based task manager, was that I don't always consider myself good at planning things. 
Making the right priorities and meeting a deadline can sometimes be a challenge for many people, myself included. Therefore I thought it would be great to design something that could be a tool for achieving both bigger goals and smaller tasks. 
Making the app a web-based tool that can be operated both from a desktop computer, a tablet and a mobile phone, being fully responsive and accessible, could make life easier for a lot of people. 

## Site Owner Goals
- As a site owner I want to provide an easy-to-use but yet powerful tool for the user to manage their goals and tasks in an efficient way.
- As a site owner I want to provide the user with the opportunity to create a unique user profile which is only accessible to the user.
- As a site owner I want to make sure that the user easily can edit, delete and add new goals and tasks using the app.

## Features

### Authentication
* A new user will be prompted to create a user name and a password. As soon as that is done, the user will be able to log on to the site and start using the features. A returning user will already have created a user name and can log in with those credentials. The user will also be able to change the password if necessary. 

### Goals
- A user will be able to set a new goal with a date attached to it, from the goals dashcard.
There is also an option to set a status for the goal - if it has been completed or not. Each goal has a texte area where the user can describe in detail what he goal consists of. The user can use a maximum of 200 characters to give the goal an elaborate description. Also, there is an option of assigning different tasks to every goal. These tasks can help the user to break down each goal into smaller pieces which will make it much easier to achieve the assigned goal. 

## Features left to implement.

### Tasks
- A task is a smaller chore which can be a part of a bigger goal. The task is optional and a user can attach one or more tasks to a goal. There is also the option of setting a status to each task. The user can also - as with the goals edit, update ad delete the tasks. If a task is completed it acn be given the status of done, or if it is no longer current it can be deleted. There is no limit to how many tasks a goal can have, but the user should make sure of not cluttering the goal too much. Due to time constraints, the task page wasn't properly implemented. Instead the user will be redirected to the goals form, where tasks can be added and edited manually to the users content. The decision to not include the task page was a hard one - a sort of "kill your darlings"- decision, as it was a good and quite useful feature. In a future update, the task will most likely be implemented though.

### Calendar
- Another feature that had to be gone because of time constraints. The calendar was planned to be on a separate page where the user could see the goals and tasks to be able to set deadlines and reschedule. This feature is not a must-have, but would absolutely be a nice addition to a future version of this project. 

- For this project I was using allauth to make it possible for the user to sign up and log in to the site safely. 
## Responiveness
- The app is responsive on all platforms, from desktop to tablets and mobile phones. 

## Planning and development
- This was the first project in which I made use of the Agile methodology. A fair amount of time went into planning the project before I could get into building it. 
I started out with a kanban board - assigned to this repository on Github, to identify the EPIS's and User Stories needed to realize the project in a satisfactory way. Using the backlog in the kanban board, appeared to be a very powerful process to keep track of what I was doing.
- Realizing the ideas I had written down and put in ERD's and flowcharts was more challenging than I expected. Actually, just coming up with a comprehensive entity relationship diagram that could be translated into code, was something I had to practice alot before ending up with the ERD represented in this document. 
- Translating the ideas into code was another challenge. My first examples of the initial model for the project was based on a tutorial, which gave me alot of tips on how to structure the application. However I needed to go back to the drawing board as the building of this first project got too convoluted and error prone. I decided to revisit the walkthrough of Code Institutes blog project to be able to start afresh. A also went back to study the Agile methodology again, before starting writing new code.
- This final version of this project is built using the Django Framework. All models and relations betweeen them as well as dialog with databases are utilizing the powerful features built into the Django framework.  
- When struturing the views, I was not really sure which page should end up being the landing page. Therefore I changed the original index.html to goal.html. However, this really should be the index.html, as this is the page the user will be taken to after logging in or signing up. 

### Target audience
- Anyone who needs a tool to structure and prioritize their goals can make use of this app.
Because of its wed-based nature, the app is available everywhere where the user has an internet connection. 

### App Objectives

## Wireframes
- [Wireframe]()

## Flow charts and ERD’s
- ![Flow Chart](documentation/To-do-list.png)
- ![ERD](documentation/ERD%20my-to-do-list.png)
## Kanban board
![Kanban](documentation/kanban.png)
### EPICS
* Create App
* Django Setup
* Pagination
* Account Management
* Goals
* Tasks
* Calendar
* Deployment
* Documentation 
* Testing 

### User Stories

* Automated Testing
* Goals Menu
* Update Personal Info
* Readme
* Show Goals/ tasks
* Goals dash card
* Delete Goal
* Delete Account
* Log in with social media platforms
* Links to social media
* Scheduled taskt - status
* Manual testing
* Responsiveness and accessibility
* Log in/ Log out
* ERD
* Tasks menu
* Sign up
* Task dash card
* Reset password

### Models

## Design
### Colors
### Fonts

### CRUD Implementation
- This app makes use of the CRUD operations (Create, Read, Update & Delete).
For example, when a user is adding a new goal, the app is creating this item.
The user is then able to view this item, which is making use of the "read"-operation
If a user has to update a goal, the selected item can be edited in the form and submitted again,
which makes use of the "update"-operation. Finally, if a user wants to delete a goal, clicking the Delete- button 
will make use of the "delete"-operation and the item will be erased accordingly. 

## Testing

### PEP8 Testing
- All python code has been tested with the ![Pythonchecker]https://www.pythonchecker.com/
Results vary from 'solid'(c:a 50%) to 'guido'(100%).
### Input Testing

### Other Testing
•	Lighthouse
- Lighthouse testing of the page resulted in an average score of 94% for desktop and 92% for mobile devices.
•	JSHInt 
- The JavaScript validation returned no errors but these warnings were listed:
19 warnings
1	'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
2	'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
3	'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
4	'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
6	'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
7	'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
8	'const' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
11	'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
11	'for of' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
12	'arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6').
13	'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
14	'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
14	'template literal syntax' is only available in ES6 (use 'esversion: 6').
17	'template literal syntax' is only available in ES6 (use 'esversion: 6').
22	'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
22	'for of' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
23	'arrow function syntax (=>)' is only available in ES6 (use 'esversion: 6').
24	'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
25	'template literal syntax' is only available in ES6 (use 'esversion: 6').
One undefined variable
6	bootstrap

•	W3C CSS Validator
- The CSS passed through the validation tool without any errors or warnings.
•	W3C HTML Validator
- The validator returns some info and errors that don't create any conflicts in the project. However they are listed below just for the sake of the documentation. In a future version of this project, there might be useful information to draw from when implementing new features. 
- [HTML Validation](documentation/html_errors.png)
- [HTML Validation2](documentation/html_errors2.png) 
### Browser testing


## Technologies Used
•	Framework
-	Django
•	Languages
-	Python
-	HTML
-	CSS
-	JavaScript
•	Databases
-   PostgreSQL
### Libraries used
- Django
- Bootstrap


### Platforms used

## Data model

### Programs Used
* Gitpod for coding.
* Lucidchart for making ERD's.
* 

## Agile Methodology
* Making use of the Agile Methodology for the first time was a steep learning curve for me. However, it proved to be a quite powerful awy of realizing a project. Even though I struggled to put the final project together, it would probably have been even more difficult without proper planning and methodical structuring of the application.  
* Kanban board: https://github.com/users/Dym077/projects/2 

## Known Bugs
 

## Fixed Bugs
- When trying to submit a goal when not logged in, the user would encounter an error instead of being prompted to log in first. This error as the cause of the login function not restraining access to the goal form, which should only be accessible after the usrer has been registered or logged in. To prevent this from happening, I made the goal form inaccessible to an unauthenticated user, which acquires a new user to register or a returning user to simply login. 

## Deployment
* This project was deployed using Heroku.
I made an early deployment to ensure that the live app was running correctly and that the versions of the libraries were working together.
- This is how to create the Heroku app:
- Log in to Heroku or create a new account.
- When on the main page, click the button called New in the top right corner and from the drop-down menu select "Create New App".
- Type in the name of the app, which must be unique to work.
- Select your region.
- Click the Create App button.
- Click the Settings Tab - scroll down to Config Vars.
- Click Reveal Config Vars and enter PORT into the Key box and 8000 into the Value box and click the Add button.

## Credits
- [Planner App (Task Manager)](https://github.com/OleksiyLa/Project_4)
- Image was downloaded from [Freepik](https://www.freepik.com/)  Designed by pch.vector / Freepik
### Resources Used

#### Online Resources
- [Django To Do List App With User Registration & Login](https://www.youtube.com/watch?v=llbtoQTt4qw&t=1484s)
- [TinyPNG]https://tinypng.com/ for compressing images.
- [Cloudconvert](https://cloudconvert.com/) for comverting images to webp-format.

#### Desktop resources
* Affinity Photo for image editing.
* Paint for image editing.

## Acknowledgments
- Antonio Rodriquez
- Tomas Kubancik
- Roman Rakic
- Martin Degerman
- The Slack community and Community Sweden
