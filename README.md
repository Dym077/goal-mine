# My To-do-list
![]()


- The live link is found via this link - [](https://dymo-my-todo-list-7a30e9c04781.herokuapp.com/)


## Why a To-do-list app?

### The Idea behind it all
- My initial idea behind buildning a web based task manager, was that I don't always consider myself good at planning things. 
Making the right priorities and meeting a deadline can sometimes be a challenge for many people, myself included. Therefore I thought it would be great to design something that could be a tool for achieving both bigger goals and smaller tasks. 
Making the app a web-based tool that can be operated both from a desktop computer, a tablet and a mobile phone, being fully responsive and accessible, could make life easier for a lot of people. 

### 
### 
## Site Owner Goals
## User Stories

### First time user

### Returning user

### Frequent user

## Features
### Authentication
* A new user will be prompted to create a user name and a password. As soon as that is done, the user will be able to log on to the site and start using the features. A returning user will already have created a user name and can log in with those credentials. The user will also be able to change the password if necessary. 

### Goals
- A user will be able to set a new goal with a date attached to it, from the goals dashcard.
There is also an option to set a status for the goal - if it has been completed or not. Each goal has a texte area where the user can describe in detail what he goal consists of. The user can use a maximum of 200 characters to give the goal an elaborate description. Also, there is an option of assigning different tasks to every goal. These tasks can help the user to break down each goal into smaller pieces which will make it much easier to achieve the assigned goal. 
### Tasks
- A task is a smaller chore which can be a part of a bigger goal. The task is optional and a user can attach one or more tasks to a goal. There is also the option of setting a status to each task. The user can also - as with the goals edit, update ad delete the tasks. If a task is completed it acn be given the status of done, or if it is no longer current it can be deleted. There is no limit to how many tasks a goal can have, but the user should make sure of not cluttering the goal too much. 
### Calendar
### Authorization
## Responiveness

## Planning and development
- This was the first project in which I made use of the Agile methodology. A fair amount of time went into planning the project before I could get into building it. 
I started out with a kanban board - assigned to this repository on Github, to identify the EPIS's and User Stories needed to realize the project in a satisfactory way. Using the backlog in the kanban board, appeared to be a very powerful process to keep track of what I was doing.
- Realizing the ideas I had written down and put in ERD's and flowcharts was more challenging than I expected. Actually, just coming up with a comprehensive entity relationship diagram that could be translated into code, was something I had to practice alot before ending up with the ERD represented in this document. 
- Translating the ideas into code was another challenge. My first examples of the initial model for the project was based on a tutorial, which gave me alot of tips on how to structure the application. However I needed to go back to the drawing board as the building of this first project got too convoluted and error prone. I decided to revisit the walkthrough of Code Institutes blog project to be able to start afresh. A also went back to study the Agile methodology again, before starting writing new code.
- This final version of this project is built using the Django Framework. All models and relations betweeen them as well as dialog with databases are utilizing the powerful features built into the Django framework.  
### Target audience
### App Objectives

## Wireframes

## Flow charts and ERD’s

## Kanban board
### EPICS
### User Stories

![Flow Chart]
![ERD]

### Models

## Design
### Colors
### Fonts

## Features

### CRUD Implementation
- This app makes use of the CRUD operations (Create, Read, Update & Delete).
For example, when a user is adding a new goal or task, the app is creating this item.
The user is then able to view this item, which is making use of the "read"-operation
If a user has to update a goal or task, the selected item can be edited in the form and submitted again,
which makes use of the "update"-operation. Finally, if a user wants to delete a goal or task, clicking the Delete- button 
will make use of the "delete"-operation and the item will be erased accordingly. 

## Testing

### PEP8 Testing

### Input Testing

### Other Testing
•	Lighthouse
•	JSHInt 
•	W3C CSS Validator
•	W3C HTML Validator
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

### Platforms used

## Data model

### Programs Used

## Features left to implement.

## Agile Methodology
* 
* Kanban board: https://github.com/users/Dym077/projects/2 

## Known Bugs

## Fixed Bugs

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

### Resources Used

#### Online Resources
- [Django To Do List App With User Registration & Login](https://www.youtube.com/watch?v=llbtoQTt4qw&t=1484s)

#### Desktop resources

## Acknowledgments

