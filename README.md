# Tiggolino Children's Playground Website

This repository contains the source code for the *Tiggolino Children's Playground* website. The project is developed using the *Django* web framework and serves as the online presence for the Tiggolino children's recreational park.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Customization](#customization)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview
The *Tiggolino Children's Playground Website* is designed to provide visitors with information about the playground, including attractions, events, opening hours, and contact details. The website aims to offer an engaging and user-friendly experience for families planning their visit.

## Features
- *Home Page:* Welcoming introduction to the playground with highlights of main attractions.
- *Attractions Section:* Detailed descriptions and images of various play areas and activities available.
- *Events Calendar:* Information on upcoming events and special activities hosted at the playground.
- *Visitor Information:* Essential details such as opening hours, ticket prices, and safety guidelines.
- *Contact Form:* Allows visitors to send inquiries or feedback directly through the website.
- *Responsive Design:* Ensures optimal viewing on desktops, tablets, and mobile devices.

## Technologies Used
- *Django:* High-level Python web framework for rapid development and clean design.
- *Python:* Programming language used for server-side logic.
- *HTML5 & CSS3:* Markup and styling for structuring and designing the web pages.
- *JavaScript:* Adds interactivity and dynamic content to the website.
- *SQLite:* Default database for development; can be replaced with PostgreSQL or MySQL in production.
- *Git:* Version control system for tracking changes and collaboration.

## Installation and Setup
To set up the project locally, follow these steps:

1. *Clone the Repository:*
   ```bash
   git clone https://github.com/erenaktuerk/tiggolino.git

	2.	Navigate to the Project Directory:

cd tiggolino


	3.	Create a Virtual Environment:

python -m venv venv


	4.	Activate the Virtual Environment:
	•	On Windows:

venv\Scripts\activate


	•	On macOS and Linux:

source venv/bin/activate


	5.	Install Dependencies:

pip install -r requirements.txt


	6.	Apply Database Migrations:

python manage.py migrate


	7.	Create a Superuser (Optional):

python manage.py createsuperuser

Follow the prompts to set up the admin user.

	8.	Collect Static Files:

python manage.py collectstatic


	9.	Run the Development Server:

python manage.py runserver

The website will be accessible at http://127.0.0.1:8000/.

Project Structure

The project is organized as follows:

tiggolino/
├── manage.py             # Django management script
├── tiggolino/            # Project configuration directory
│   ├── _init_.py
│   ├── settings.py       # Project settings
│   ├── urls.py           # URL routing
│   ├── wsgi.py           # WSGI configuration
│   └── asgi.py           # ASGI configuration
├── pages/                # Application for static pages
│   ├── migrations/
│   ├── _init_.py
│   ├── admin.py          # Admin configurations
│   ├── apps.py           # Application configuration
│   ├── models.py         # Data models
│   ├── tests.py          # Test cases
│   └── views.py          # View functions
├── static/               # Static files (CSS, JavaScript, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── index.html        # Home page template
│   └── ...
├── .gitignore            # Git ignore file
└── requirements.txt      # Python package dependencies

Usage
	•	Navigation: Users can explore various sections such as attractions, events, and visitor information.
	•	Interactivity: JavaScript enhances user experience with dynamic content and interactive elements.
	•	Admin Interface: Authorized users can manage content through Django’s built-in admin panel.

Customization
	•	Styling: Modify CSS files in the static/css/ directory to update the website’s appearance.
	•	Templates: Edit HTML templates in the templates/ directory to change page layouts and content.
	•	Functionality: Extend or modify functionalities by updating views and models in the respective Django applications.

Deployment

For deploying the project to a production environment:
	1.	Set Up the Production Environment: Ensure Python and necessary dependencies are installed on the server.
	2.	Configure Environment Variables: Set DEBUG to False and configure ALLOWED_HOSTS in settings.py.
	3.	Set Up the Database: Configure a production-ready database such as PostgreSQL or MySQL.
	4.	Collect Static Files:

python manage.py collectstatic


	5.	Configure the Web Server: Use a WSGI server like Gunicorn and set up a reverse proxy with Nginx or Apache.
	6.	Secure the Application: Implement HTTPS, configure security settings, and monitor the application.

Contributing

Contributions to enhance the project are welcome. To contribute:
	1.	Fork the Repository.
	2.	Create a New Branch:

git checkout -b feature/your-feature-name


	3.	Commit Your Changes:

git commit -m "Add your descriptive commit message"


	4.	Push to the Branch:

git push origin feature/your-feature-name


	5.	Open a Pull Request: Submit the pull request for review and discussion.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

For inquiries or support, please contact the project maintainer via the GitHub repository.