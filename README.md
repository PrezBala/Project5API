# FlickRater API- Project 5

The objective of this API is to serve as a robust backend mechanism for the Flickrater frontend application. It is specifically designed to facilitate seamless Create, Read, Update, and Delete (CRUD) operations through the user interface. This structure empowers users to interact with the application effectively and efficiently.

FlickRater API is the backend service used by the [Live link to the Repository](https://github.com/PrezBala/Project5FE)

<hr>

# Table of contents

- [Development Goals](#development-goals)
- [Agile Planning](#agile-planning)
- [User-Experience-Design](#user-experience-design)
  - [Site Goals](#site-goals)
  - [Agile Planning](#agile-planning)
  - [User Stories](#user-stories)
- [API Endpoints](#api-endpoints)
- [Security](#security)
- [Technologies](#technologies)
  - [Python Packages](#python-packages)
- [Testing](#testing)
  - [Functional Testing](#functional-testing)
- [Deployment](#deployment)
- [Heroku Deployment](#heroku-deployment)
- [Credit](#credit)

# Development Goals

Astro Community aims to unite space enthusiasts in a thriving online platform, fostering knowledge exchange, stimulating discussions, and encouraging the exploration of the wonders of the universe. My goal is to create an engaging, supportive space where members can connect, learn, and share their passion for the cosmos.

# Agile Planning

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

# User Experience Design

- Implement responsive design.
- Create a homepage featuring categories for various topics.
- Create a admin dashboard only available to the administrator
- Create a page for comments where users have the ability to edit their comments.
- Provide a search field for users to locate specific topics.
- Display user post count and a point system managed by the administrator.
- Indicate engagement levels using images under each category, representing low engagement, popular topics, closed topics, etc.
- Limit certain features for users who are not logged in.

## Site Goals

## Agile Planning

## User Stories

# API Endpoints

- User Story - As a user, I want to easily view the main categories and navigate to the relevant one.

# Security

- User Story: As site owner, I want to share my name within the footer.

# Technologies

- User Story: As a user who is not logged in, I want to have the ability to explore forum posts created by other users.

Even without logging in, anyone can access the website to browse posts, navigate between categories, and read through all posts, comments, and replies

## Python Packages

- User Story: As a user, I want to search for topics of interest to discover if other users have shared similar thoughts or comments.

# Testing

User Stories

## Functional Testing

- User Story: As a user, I want to effortlessly share my questions or theories on the site so that I can exchange ideas with others.

Upon logging in, users can create their own posts using forms designed with Crispy Forms.

The image below showcases the mobile view, illustrating how the forms adapt to a smaller screen, ensuring a user-friendly experience on mobile devices.

<img src="https://github.com/PrezBala/project4/blob/main/static/assets/images/phonesize.png">

# Deployment

- User Story: As a user, I want the ability to upload a profile picture for the new account I've just created.

# Heroku Deployment

- User Story: As a user, I want the ability to upload a profile picture for the new account I've just created.

# Credit

User Stories

[Back to Table of Contents](https://github.com/PrezBala/project4#table-of-contents)
