# FlickRater API- Project 5

The objective of this API is to serve as a robust backend mechanism for the Flickrater frontend application. It is specifically designed to facilitate seamless Create, Read, Update, and Delete (CRUD) operations through the user interface. This structure empowers users to interact with the application effectively and efficiently.

FlickRater API is the backend service used by the [Live link to the Repository](https://github.com/PrezBala/Project5FE)

# Table of contents

- [FlickRater API- Project 5](#flickrater-api--project-5)
- [Table of contents](#table-of-contents)
- [Development Goals](#development-goals)
- [Agile Planning](#agile-planning)
  - [Epics](#epics)
  - [Set Up](#set-up)
  - [Movie Creation](#movie-creation)
  - [Movie Description](#movie-description)
  - [Custom Auth Token](#custom-auth-token)
  - [Movie Rating](#movie-rating)
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

The objective of this API is to function as a backend service, enabling the FlickRater frontend application to carry out Create, Read, Update, and Delete operations through its user interface.

# Agile Planning

This project was developed following agile principles, with a series of four sprints. Each feature was prioritized and labeled as either "must-have," "should-have," or "could-have." We began by implementing the must-have features, followed by the should-have features, and finally addressed the could-have features if time and resources permitted. This approach ensured the delivery of a comprehensive website, with optional enhancements added based on capacity.

Our Kanban board, created using GitHub Projects, facilitated project management and can be accessed [here](https://github.com/users/PrezBala/projects/1/views/1). For more detailed information on each task, simply click on the respective view.

![kanban](readme/kanban.png)

## Epics

The user stories were grouped into different Epics

## Set Up

This epic encompasses the crucial steps to get the Django application and Django REST Framework operational, creating a robust platform to start developing the features.

## Movie Creation

This epic focuses on the establishment of API endpoints and database integrations to support CRUD operations for the creation of movie posts, forming the backbone of movie content in the application.

## Movie Description

This epic is dedicated to designing and implementing API endpoints and database connections for the CRUD operations specifically related to the Movie description field, allowing for detailed storytelling and representation of each movie.

## Custom Auth Token

This epic targets the creation and handling of unique user tokens. It involves designing API endpoints and database interactions for CRUD operations of these tokens, providing a layer of security and personalization for each user in the system.

## Movie Rating

This epic covers the design and development of a comprehensive movie rating system. It includes creating API endpoints and database connections that allow users to rate each movie, offering a user-driven evaluation of each movie listing.

# User Stories

By Epics

Setup

As a developer, I need to establish the foundational project setup to facilitate the construction of requisite features.
User Permissions

As a developer, I need to build a system where users have the ability to delete and edit their own movie listings, yet are restricted from modifying others' listings.

As a developer, I need to implement a special admin section that is exclusively accessible to admin/staff users, who possess the rights to delete any movie listing.

As a user, I need the capability to create a new account so that I can avail of all features that are available to registered users.
Movie Listing Creation

As a user, I need to have the functionality to create a new movie listing, provide a detailed description, and assign a rating through the implemented 5-star rating system.
Movie Listing and Rating Review

As a user, I need to be able to view the total count of ratings for a specific movie listing, as well as understand its average star rating.

# API Endpoints

API Endpoints

User Story:

As a developer, I need to establish the base project setup for the construction of requisite features.

Implementation:

The foundational project was formulated, and a virtual environment was created with all necessary packages installed and solidified into the requirements.

Secret variables were hidden and settings were modified to distinguish between the development and production environments.

User Story:

As a user, I need the capability to create a new account to gain access to all features exclusive to registered users.

Implementation:

To harness their built-in authentication system, Django rest framework and dj_rest_auth were installed, added to the URL patterns, and incorporated into the site packages.

User Story:

As a developer, I need to generate API views for movie enthusiasts for their utilization on the front end.

Implementation:

Endpoint: /api/movies

Methods:

POST - Utilized for creating a Movie listing.
GET - Utilized for retrieving a list of Movies.

Methods:

GET - Utilized for viewing a Movie.
PUT - Utilized for updating a movie listing.
DELETE - Utilized for removing a movie listing.

User Story:

As a user, I need to be able to observe movie ratings.

As a user, I need to have the capacity to contribute my own rating to particular movies.

Implementation:

Endpoint: /api/ratings

Methods:

POST - Utilized for adding a new rating to a movie.
GET - Utilized for obtaining a list of ratings for a movie.

User Story:

As a developer, I need to have the ability to observe the users that have been created.

Implementation:

Endpoint: /api/users

Methods:

POST - Utilized for creating a new user.
GET - Utilized for retrieving a list of users and their respective staff ratings.

# Security

- A permission class, named 'class IsAdminUser(permissions.BasePermission)', was implemented to ensure that only administrators are granted access to the admin section and possess the rights to delete all movie listings, among other admin-exclusive functionalities.

# Technologies

- Django
This is the primary framework utilized for the creation of the application.

- Django REST Framework
This framework is employed for the development of the API.

- Heroku
This platform is used for the hosting of the application.

- Git
This tool is utilized for version control.

- Github
This is the repository used for the storage of the code base and documentation.

## Python Packages

asgiref==3.6.0
I use this for ASGI support, which helps me with asynchronous web applications.

cloudinary==1.33.0
I use this service to manage images in the cloud, simplifying media management.

dj-database-url==2.0.0
This tool allows me to utilize database URLs in my Django configuration for flexible deployment.

dj-static==0.0.6
This is a static file server for Django, useful during app development and deployment.

Django==3.2.13
The main high-level web framework I use for rapid and clean application development.

django-cloudinary-storage==0.3.0
This helps me use Django storages with Cloudinary.

django-cors-headers==4.0.0
I use this Django app to add Cross-Origin Resource Sharing (CORS) headers to responses.

django-rest-authtoken==2.1.4
A simple token-based authentication system I use for my Django REST framework.

djangorestframework==3.14.0
I use this toolkit for building Web APIs in Django.

djangorestframework-simplejwt==5.2.2
A minimal JSON Web Token authentication plugin for Django REST Framework.

gunicorn==20.1.0
My choice for a Python WSGI HTTP Server for UNIX with a pre-fork worker model.

Pillow==9.5.0
A user-friendly fork of Python's PIL library I use for image processing.

psycopg2-binary==2.9.6
The PostgreSQL database adapter for Python that I use.

PyJWT==2.7.0
I use this for implementing JSON Web Tokens in Python.

pytz==2023.3
This Python library helps me with accurate timezone calculations.

sqlparse==0.4.4
A non-validating SQL parser module I use in Python.

static3==0.7.0
A wrapper I use for Django’s static files serving.

urllib3==1.26.16
The HTTP client I use in Python for making requests.

whitenoise==6.4.0
I use this to allow my web app to serve its own static files, making it self-contained and easy to deploy.

# Testing

User Stories

## Functional Testing

- User Story: As a user, I want to effortlessly share my questions or theories on the site so that I can exchange ideas with others.

Upon logging in, users can create their own posts using forms designed with Crispy Forms.

The image below showcases the mobile view, illustrating how the forms adapt to a smaller screen, ensuring a user-friendly experience on mobile devices.

# Deployment

- User Story: As a user, I want the ability to upload a profile picture for the new account I've just created.

# Heroku Deployment

- User Story: As a user, I want the ability to upload a profile picture for the new account I've just created.

# Credit

User Stories

[Back to Table of Contents](https://github.com/PrezBala/project4#table-of-contents)
