# FlickRater API- Project 5

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/astrohome.png">

The objective of this API is to serve as a robust backend mechanism for the Flickrater frontend application. It is specifically designed to facilitate seamless Create, Read, Update, and Delete (CRUD) operations through the user interface. This structure empowers users to interact with the application effectively and efficiently.

[Live link to the forum](https://astro-community.herokuapp.com/)

<hr>

# Table of contents

- [FlickRater API- Project 5](#flickrater-api--project-5)
- [Table of contents](#table-of-contents)
- [User-Experience-Design](#user-experience-design)
  - [Site Goals](#site-goals)
  - [Agile Planning](#agile-planning)
  - [Scope](#scope)
  - [Structure](#structure)
    - [Astro Community Features - USER](#astro-community-features---user)
    - [Astro Community Features - ADMIN](#astro-community-features---admin)
    - [Home Page](#home-page)
    - [Footer](#footer)
    - [Browse Posts](#browse-posts)
    - [Search](#search)
    - [Log In Log Out Sign Up](#log-in-log-out-sign-up)
    - [Create Post](#create-post)
    - [Profile Picture](#profile-picture)
    - [Engagement](#engagement)
- [Wireframes](#wireframes)
- [Database](#database)
- [Security](#security)
- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Imagery](#imagery)
  - [Icons](#icons)
- [Technologies](#technologies)
  - [External Python Modules](#external-python-modules)
- [Testing](#testing)
  - [Functional Testing](#functional-testing)
    - [Navigation Links](#navigation-links)
    - [Sign Up Page](#sign-up-page)
    - [Log out Page](#log-out-page)
    - [Log in](#log-in)
    - [Create New Post](#create-new-post)
    - [Delete A Comment or Reply](#delete-a-comment-or-reply)
    - [Edit, Close and Delete a post](#edit-close-and-delete-a-post)
    - [Closed post](#closed-post)
    - [Comment on a post](#comment-on-a-post)
    - [Reply on a post](#reply-on-a-post)
    - [User test](#user-test)
  - [Accessibility](#accessibility)
  - [Validator Testing](#validator-testing)
  - [PP8 Validator](#pp8-validator)
  - [Javascript Validator](#javascript-validator)
  - [Lighthouse Report](#lighthouse-report)
- [Responsiveness](#responsiveness)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [References](#references)
- [Future Features](#future-features)
- [Acknowledgements](#acknowledgements)

# User-Experience-Design

## Site Goals

Astro Community aims to unite space enthusiasts in a thriving online platform, fostering knowledge exchange, stimulating discussions, and encouraging the exploration of the wonders of the universe. My goal is to create an engaging, supportive space where members can connect, learn, and share their passion for the cosmos.

## Agile Planning

This project was developed following agile principles, with a series of four sprints. Each feature was prioritized and labeled as either "must-have," "should-have," or "could-have." We began by implementing the must-have features, followed by the should-have features, and finally addressed the could-have features if time and resources permitted. This approach ensured the delivery of a comprehensive website, with optional enhancements added based on capacity.

Our Kanban board, created using GitHub Projects, facilitated project management and can be accessed [here](https://github.com/users/PrezBala/projects/1/views/1). For more detailed information on each task, simply click on the respective view.

![kanban](/static/assets/images/kanban.png)

The user stories were grouped into different Epics

Epic 1 - Setup

The initial step focused on establishing the foundational Django app, as it was crucial to complete this before progressing to other tasks. During this phase, the base HTML, header, and footer were created, and deployment was also addressed to prevent complications at a later stage.

Epic 1 user stories:

As a developer, I need to set up the project to lay the groundwork for incorporating core features.
As a developer, I want to create a base HTML page to maintain a consistent format across all pages.
As a user, I want seamless navigation throughout the site on my mobile and tablet devices.
As a site owner, I want to enable users to sign up for new accounts, fostering communication and interaction.
As a developer, I want to ensure smooth deployment via Heroku / ElephantSQL to circumvent potential issues.

Epic 2 - Database Model and Admin

The focus of this phase was to establish the database model and admin functions, which would allow the admin to approve or reject new posts. Additionally, the admin would have the ability to clsoe forum posts once the topic question was adequately addressed.

Epic 2 User Stories:

As a developer, I want to create the foundation for the database, enabling users to update their posts by commenting below them.
As a developer, I want to be able to delete comments / replies from all users within Front.
As a user, I want the ability to remove my own comments,replies and edit my comments while ensuring that this action is limited exclusively to my own submissions.
As a non-logged-in user, I want to browse ideas from other users, but I will need to log in to post my own.

Epic 3 - Login, Signup, and Logout Pages

Epic 3 User Stories:

As a new user, I want an easy and intuitive signup process.
As a returning user, I want a straightforward login experience.
As a user, I want to safely and easily log out of the site.
As a developer I want to be able to access front and backend to edit,remove and delete posts.
As a developer I want to ensure the users are not able to access backend system.

Epic 4 User Stories:

As a user, I want to effortlessly share my ideas by submitting them to the site.
As a user, I want the ability to comment on and respond to other users' posts.
As a user, I want to view the post count and points allocated by the admin for any user.
As the site owner, I want to ensure only space-related topics are posted, requiring admin or delegated mod approval for each new post.

Epic 5 - Styling

Epic 5 User Stories:

As a user, I want a clear and self-explanatory front page to confirm I am in the right place.
As a developer, I want to implement a space-themed color scheme for the forum.
As a developer, I want to feature a space-related video on the main page to captivate users.
As a developer, I want to standardize the style of all forms and ensure they look good on various devices.
As a developer, I want to have a well-organized table that enables me to efficiently view, edit, and approve user-generated posts.

--

Epic 6 - Documentation

Epic 6 Tasks

- Finalize Readme documentation.
- Conduct comprehensive testing and provide a writeup.

## Scope

- Implement responsive design.
- Create a homepage featuring categories for various topics.
- Create a admin dashboard only available to the administrator
- Create a page for comments where users have the ability to edit their comments.
- Provide a search field for users to locate specific topics.
- Display user post count and a point system managed by the administrator.
- Indicate engagement levels using images under each category, representing low engagement, popular topics, closed topics, etc.
- Limit certain features for users who are not logged in.

## Structure

### Astro Community Features - USER

Navbar

User story - As a user I want to be able to navigate easily around the site easily from any devise

Navigation Menu

When the user is not logged in the navigation bar links to the Sign In, Sign Up page and the Home Page and the 'Click here to create post' button is not visible

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/pendingsignin.png">

Once the user has signed in the navigation menu changes to Comments, Log out and Home.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/signin1.png">

On smaller devices, i ensured the NavBar shows correctly with all text visible.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/mobileloguser.png">

### Astro Community Features - ADMIN

Once the user has signed in the navigation menu changes to Log out and Home with the "Click here to create a new post" message appearing, allow the user to create a new post.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/adminsignin.png">

I've designed an Admin interface that provides the administrator with the ability to edit, delete, and approve user-submitted posts.

Administrators will possess unique authorizations that standard users do not have access to. This includes an exclusive 'Admin' page accessible through the forum's frontpage navigation bar. On this page, administrators can view all posts and have the option to edit, delete, and authorize comments for public viewing on the website. Additionally, the design has been enhanced to ensure clarity and aesthetic appeal.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/updatebasicmodel.png">

### Home Page

- User Story - As a user, I want to easily view the main categories and navigate to the relevant one.

The main page features an engaging .mp4 video of the moon with clouds circulating, emphasizing the space theme of the website.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/moonimage.png">

A search function is included, allowing users to look for topics of interest. If a match is found, users will be directed to the search results page.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/searchbox.png">

After logging in, users will see a message "Click here to create a new post". By clicking on this message, they can create a new post by providing a title, content, and selecting a category. Additionally, users can add tags to improve the accuracy of the search results.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/plus.png">

Forum stats are displayed, showcasing the total post count, details of the latest post, and the user who created it.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/forumstats.png">

### Footer

- User Story: As site owner, I want to share my name within the footer.

The Footer has been added to the bottom of the site.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/footer.png">

### Browse Posts

- User Story: As a user who is not logged in, I want to have the ability to explore forum posts created by other users.

Even without logging in, anyone can access the website to browse posts, navigate between categories, and read through all posts, comments, and replies

### Search

- User Story: As a user, I want to search for topics of interest to discover if other users have shared similar thoughts or comments.

Upon entering their search query, users will be directed to a search results page displaying relevant content, or a message indicating no results were found.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/searchresult.png">

### Log In Log Out Sign Up

User Stories

- As a new user, I want a straightforward and intuitive signup process.
- As a returning user, I want an effortless login experience.
- As a user, I want to safely and easily log out of the site.
- As a developer, I want to standardize the style of all forms and ensure they look good on various devices.

Users can seamlessly sign in and out using consistently styled forms and confirmation pages.

User Stories:

### Create Post

- User Story: As a user, I want to effortlessly share my questions or theories on the site so that I can exchange ideas with others.

Upon logging in, users can create their own posts using forms designed with Crispy Forms.

The image below showcases the mobile view, illustrating how the forms adapt to a smaller screen, ensuring a user-friendly experience on mobile devices.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/phonesize.png">

### Profile Picture

- User Story: As a user, I want the ability to upload a profile picture for the new account I've just created.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/profilepic.png">

### Engagement

User Stories

- As a user, I want to see the level of engagement for each post, which is represented by clear images within each category page.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/postengagement.png">

When a user creates a new post and it is approved by the site admin, the engagement will be displayed as '0 Engagement Topic.'

As users comment or reply within that post, the engagement indicator will be updated accordingly.

The image below represents a new post with no engagement from other users, and thus, a sad face status image is displayed to signify this lack of interaction.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/0engage.png">

In contrast, the image below demonstrates a scenario where a user comments on the post, resulting in an updated status image displaying a book symbol, which indicates a level of 'low engagement.'

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/1engage.png">

# Wireframes

Home Page and Navbar extended

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/wireframe1.png">

Sign In and Sign Up.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/wireframe2.png">

Category Selection and Posts.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/wireframe3.png">

# Database

The system is configured to grant administrators CRUD functionality upon signing in. Both the administrator and any designated moderator can approve, remove, edit, and close posts through the admin function, which is exclusively viewable and accessible by the admin. This feature is demonstrated in the accompanying screenshot.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/adminpost.png">

Additionally, the Django admin page can be accessed for more sophisticated modifications, such as creating categories, assigning points to users, and so on.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/admin.png">

# Security

Views were safeguarded using Django's view mixin, UserPassesTestMixin. A test function was implemented to employ the mixin and ensure that the user has the necessary authorization to access the page. Moreover, an else statement is used in detail.html to restrict unauthorized users from commenting or replying to posts unless approved by the administrator or moderators.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/userlock.png">

Environment variables were stored in an env.py file for security purposes to ensure no secret keys, api keys or sensitive information were added to the repository.  These variables were added to ElephantSQL config vars within the project

# Design

## Colour Scheme

To maintain the space theme of the website, I searched for a suitable color palette using Colorswall [https://colorswall.com/] ensuring a cohesive and visually appealing design.

## Imagery  

The hero video featured on the website is an .mp4 file depicting the moon with clouds swirling around it. This captivating visual was found through a Google image search using video filters.

## Icons

The icons on the Forum page were sourced from Font Awesome [https://fontawesome.com/]

# Technologies

- HTML
  - The site's structure was created using HTML.
- CSS
  - An external stylesheet was utilized to style the website with CSS.
- Python
  - The Django app was primarily developed using Python.
- Github
  - The source code was hosted on Github.
- Git
  - Git was employed to write, commit, and push code during development.
- Font Awesome
  - Various Font Awesome icons were incorporated throughout the site.
- Balsamiq
  - Balsamiq wireframes were used for planning purposes.
- javascript
  - A minimal amount of JavaScript was implemented to make toast messages disappear.

## External Python Modules

- Django==3.2.16 - Framework used to build the application
- django-crispy-forms==1.14.0 - used to style forms
- Pillow==9.4.0 - Installed to upload images.
- asgiref==3.6.0 - Installed to provide various ASGI-related utilities,
- sqlparse==0.4.3 - Used for parsing, splitting, and formatting SQL statements
- register==0.1 - Related to user registration within the Django app
- django-etc==1.4.0 - Contains various utilities and extensions for Django projects, aiming to improve productivity and code quality.
- django-hitcount==1.3.5 - This Django app allows me to track the number of hits/views for chosen objects within my project.
- django-resized==1.0.2 - This package provides a simple Django field for handling resizing of images upon upload. It helps maintain a consistent size for all uploaded images
- django-taggit==3.1.0 -Installed this Django app to simplify the addition of tagging my application, allowing me to associate tags with any model instances
- django-tinymce==3.5.0 - This package integrates the TinyMCE rich text editor with the Django framework, allowing to create and edit rich-text content easily
- pytz==2022.7.1 - This library provides world timezone definitions, allowing me to work with timezone-aware datetime objects in Python

# Testing

## Functional Testing

### Navigation Links

Testing was performed on on all navigation links throughout the site.  I achieved this by clicking on each link to ensure it went to the correct place.

Navbar 'Burger' Menu => Expands Navbar to signin.html, signup.html and index.html
Home page => index.html
Sign In => signin.html
Signup => signup.html
Logout => index.html

Admin only FRONT access

Admin  => admindashboard.html

### Sign Up Page

Testing was taken out to ensure a user could sign up to the website.
Steps:

- Navigate to [AstroCommunity](https://astro-community.herokuapp.com/)
- Navigate to the Sign Up page.
- Enter User Name and Password
- Enter Full name, Bio and upload profile picture
- Click Update

Expected outcome: Upon successful creation of a new post, the user is redirected to the home page. The navbar on the top of the page will be updated to show options for logging out and returning to the home page. Additionally, the navbar will display a button with the message "Click here to create a new post" which users can click to create additional posts.

### Log out Page

Testing was taken out to ensure a user could log out of the website.
Steps:

- Navigate to Log Out page
- Click Confirm button

Expected outcome: Upon completing the action, the user is redirected to the homepage, and the navbar should only display options for signing in, signing up, and returning home. The message "Click here to create a new post" should not be present.

Actual outcome: The expected outcome was met, and the user was redirected to the homepage with the navbar displaying only options for signing in, signing up, and returning home. The message "Click here to create a new post" was not present.

### Log in

Testing was taken out to ensure a user could log in to the website.
Steps:

- Navigate to [AstroCommunity](https://astro-community.herokuapp.com/)
- Navigate to Sign In page
- Enter User Name and Password
- Click Sign in

Expected outcome: Upon completing the action, the user is redirected to the homepage, and the navbar should only display options for logging out and returning home. The "Click here to create a new post" message should be present.

Actual outcome: The expected outcome was met, and the user was redirected to the homepage with the navbar displaying only options for logging out and returning home. The "Click here to create a new post" message was present.

### Create New Post

Testing was carried out to ensure the user could create a new post.

Assuming user is already logged in
Steps:

- Navigate to the home page
- Click the button "Click here to create a new post"
- Complete form
  - Title
  - Content
  - Categories
  - Tags
- Click Save

  Expected outcome: If all fields are filled in correctly, the user will be redirected to the home page. The new post will appear for the administrator or forum moderator to review, and they can decide whether or not to authorize it to appear publicly. This function serves to prevent spamming and ensure that all content is reviewed by the administrator or moderators before it is made public on the forum.

### Delete A Comment or Reply

Testing was conducted with both super user and standard user roles. The goal was to verify that super users have the ability to delete any comments and replies posted by users on the forum, while standard users can only remove their own comments and replies, and not those of other standard users.

Steps:

- Login as super user (Admin)
- Navigate to category of interest
- Navigate to a post
- Make a comment and reply to the comment
- Login as standard user (user:Wizard in the screenshot below)
- Navigate to the same page
- Make another comment and reply to the main post
- Check visibility of what can be deleted and also test deletion.
- Logged back in as superuser and check Front and backend to ensure data removed correctly.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/deletetest.png">

  Expected outcome: A superuser has the capability to remove all comments and replies within the forum, while a standard user can only delete their own posts and responses.

### Edit, Close and Delete a post

Administrators have the ability to edit or delete any user post through the admin page, which can be accessed via the front-end interface (for user posts only) and the Django Admin page. This comprehensive administration coverage includes creating and editing categories, assigning points to users, and managing tasks such as deleting users and posts.

Assuming the administrator is logged in
Steps:

- Navigate to the admin page
- The administrator can select to either delete, edit,close or approve a post (button)

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/adminpage.png">

Expected outcome:  The user will be redirected back to admin main page.

Upon successful login, I have designed a "Comments" page that displays a table containing all the comments made by the user within the forum. The user can select any comment from the list and either edit or delete it.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/commentboard.png">

Upon selecting the "Edit" option for a specific comment, the user will be directed to a page that resembles the image provided. This page will allow the user to make modifications to their comment and then save those changes by clicking on the "Update Comment" button. This functionality ensures that users can successfully edit and delete the comments they have made.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/editcomment.png">

The expected outcome of implementing the feature to edit and delete comments is that users are able to modify and remove their comments successfully.

The outcome was as expected.

### Closed post

If a post is closed, no users will be able to comment and reply until the post is opened up again by the administrator.

Steps

- Navigate to a post with the padlock symbol under status

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/closedpost.png">

- Users will encounter a message indicating that the topic is closed and will not have the ability to comment or reply until the post is reopened.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/closedpost2.png">

The outcome was as expected.

### Comment on a post

Initially, I examined the comment section while the user was logged out.

As anticipated, there was no option to submit a comment, but rather a message indicating that the user must log in to post, accompanied by a link within the text.

If the user is logged in:

Steps

- Navigate to a post within any of the categories
- Click on comment and select submit
- User comment will appear below

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/commenttest.png">

Expected outcome: The comment will appear below the original post.

The outcome was as expected.

### Reply on a post

If the user is logged in:

Steps

- Navigate to a post within any of the categories
- Click on reply to an existing post with comments and select submit
- User response will appear below
- User response text box will appear shifted to the right to differentiate from standard comment messages.

Expected outcome: When a response is posted, it will appear beneath the user's comment, with the entire response field indented to the right.

The outcome was as expected.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/replytest.png">

### User test

I enlisted my wife's help to test the website's functionality. She was instructed to register for an account and create a new post. Moreover, she evaluated the search feature and the engagement viewer to confirm that they updated properly.

## Accessibility

I utilized the [Wave Accessibility](https://wave.webaim.org/) tool for assistance with accessibility testing. All pages displayed zero errors.

However, there are Alerts related to underlined text and a contrast issue. Despite these alerts, multiple user testing sessions have confirmed the clarity of the content.

## Validator Testing

All pages were tested using the [w3 HTML validator](https://validator.w3.org/). At first, there were a few errors, such as missing closing tags and a < p> tag incorrectly placed within a < span>.

All identified issues were resolved, and the pages passed the validator without any errors.

As the HTML files used Django's template language, the HTML code had to be extracted from the live web page by right-clicking and choosing "View Source." This code was then copied and pasted into the validator for verification.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/htmlcheck.png">

## PP8 Validator

As pep8online.com was not accessible, I utilized Flake8 to detect and rectify issues in the project's Python files. The majority of these issues were related to incorrect formatting, such as incorrect spacing and typographical errors. The errors detected by Flake8 included lines that were too long, blank spaces, indentation, and missing docstrings.

All of the issues detected by Flake8 were successfully resolved, with the exception of the lines that were too long in the migration files and arctictern, which were located within the vscode directory. Since these files were auto-generated, they were not modified.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/flake8.png">

I also utilized an online Python checker that I discovered through a Google search. [Python Checker](https://extendsclass.com/python-tester.html)

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/PYTHON1.png">

I've also employed the Code Institute's CI Python Linter validator, which returned no errors, as demonstrated below.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/urlspy.png">

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/viewspy.png">

## Javascript Validator

All pages were tested using the [Jshint Validator](https://jshint.com/). No errors appeared.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/JAVACHECK.png">

## Lighthouse Report

Initially, the Lighthouse report indicated a low score for best practices and also indicated where i can make imporvements.
To improve the score, I added accessible names to specific buttons and made sure links were crawlable.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/error1.png">

I've fixed these issues by adding a void element to the a href attribute for each of the highlighted instances.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/error1v1.png">

In the Lighthouse report, two additional issues were identified: the buttons are missing accessible names, and there is an insufficient contrast ratio between the background and foreground elements.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/error2.png">

I've added an arial label to the text highlighted which resolved that issue.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/error2v2.png">

I made adjustments to the text color to make it more visible for users. This change not only resolved the error but also improved the overall score.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/error2v1.png">

After implementing these changes, the score increased to 100, resulting in high ratings across all four criteria.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/lighthouse.png">

# Responsiveness

I evaluated the website's responsiveness on all devices with widths of 320px and above. The testing was conducted on Chrome, Edge, Firefox, and Safari browsers.

To accomplish this, I utilized developer tools and resized the website down to 320px.

As anticipated, there were no issues with responsiveness.

# Bugs

- There was an issue that prevented users' profile pictures from being displayed within the forum page, as illustrated below.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/noprofilepic.png">

I've added the below code within the urls.py for static/media root which resolved the issue.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/profilepiccode.png">

- An issue arose when users who were not logged in could still comment on forum posts. To resolve this, a check was added to ensure that the request user is authenticated before allowing them to comment. This solution was also applied to reply comments and closed posts, preventing users from commenting or replying when a post is closed.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/replyissue.png">

- The search function was not producing any results due to a typo in the search.html file. After identifying and correcting the error, the search function was tested and successfully displayed the relevant results.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/searchresult.png">

- I faced a problem where a standard user could delete administrator comments within any forum section. I realized that I had used 'request.user.is_authenticated' instead of the correct conditional statement, 'request.user == comment.user.user or request.user.is_staff'. After rectifying this mistake, the functionality worked as intended.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/deletecommenterror.png">

- After deploying my project on Heroku, I faced a problem and sought assistance from student support. The root cause of the issue turned out to be the background image URL I had used within style.css. To resolve it, I linked the URL directly to the image on Cloudinary, as demonstrated in the following image.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/urlerror.png">

# Deployment

To deploy my site to Heroku I followed the following steps

- Navigate to heroku and create/log into account
- Click the new button in the top right corner
- Select create new app
- Enter app name (astro-community)
- Select region and click create app (europe)
- Click the resources tab and search for Heroku Postgres
- Select hobby dev and continue
- Go to the settings tab and then click reveal config vars
- Add the following config vars:
  - SECRET_KEY: (Your secret key)
  - DATABASE_URL: (ElephantSQL URL)
  - HEROKU_POSTGRESQL_OLIVE_URL
  - CLOUNDINARY_URL: (cloudinary api url)
- Click the deploy tab
- Scroll down to Connect to GitHub and sign in / authorize when prompted
- In the search box, find the repository you want to deploy and click connect
- Scroll down to Manual deploy and choose the main branch
- Click Deploy

The app should now be deployed

# References

- I referenced other people's projects to gather ideas for kanbans and determine which code snippets to search for on Google.
  <https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak>
- I also followed the Code Institute Blog walkthrough to kickstart my project.
- Youtube - This platform has been incredibly useful and after watching countless videos i've learnt several different ways to code certain things i wouldnt have thought of
  before, i watched a vast number of channels and listed a few below.
- freeCodeCamp.org - Create a Twitter-like App
- AIOC all in one code - Reddit Clone
- Shadee Merhi - Reddit Clone REACTJS
- I consulted the Django documentation.
- I referred to the Summernote documentation.
- I contacted student support for guidance on creating an admin page, and they graciously provided various suggestions and ideas to help with the implementation.

# Future Features

- Implement like and dislike buttons to foster user engagement.

- Incorporate additional animations on the homepage for enhanced aesthetics.

# Acknowledgements

I want to thank:

- The Slack community. The help a student is able to receive from the other students is a really great tool to have.
- My Mentor Andre Aquilina who has provided me several tips/advise which has helped me in figuring out bugs i encountered during testing phases.
- My sister and my wife for testing my site for me.
- I'd like to express my gratitude to my wife for her patience during the numerous late-night study and testing sessions I spent, especially since the computer is in our bedroom!
- Youtube - This platform has been incredibly useful and after watching countless videos i've learnt several different ways to code certain things i wouldnt have thought of    before.
- I'm grateful to the student support team for their exceptional assistance in resolving the deployment issue I experienced with Heroku.

[Back to Table of Contents](https://github.com/PrezBala/project4#table-of-contents)
