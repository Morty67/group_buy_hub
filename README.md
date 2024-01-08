# Shared Purchase API
This application is created using Django Rest Framework for convenient management of a shared purchase platform.

## Installing / Getting started:
```shell
To get started, you need to clone the repository from GitHub: https://github.com/Morty67/group_buy_hub/tree/developer
Python 3 must be installed

cd config
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)

pip install -r requirements.txt

Your settings for DB in .env file:
POSTGRES_DB=<POSTGRES_DB>
POSTGRES_USER=<POSTGRES_USER>
POSTGRES_PASSWORD=<POSTGRES_PASSWORD>
POSTGRES_HOST=<POSTGRES_HOST>
SECRET_KEY=<SECRET_KEY>

Settings for account verification by email
EMAIL_HOST=your EMAIL_HOST
EMAIL_PORT=your EMAIL_PORT
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your EMAIL_HOST_USER
EMAIL_HOST_PASSWORD=your EMAIL_HOST_PASSWORD

python manage.py migrate
python manage.py runserver
```
## Run Docker
Docker must be installed 
```shell
*  docker-compose build
*  docker-compose up
```
## How to get access

Domain:
*  localhost:8000 or 127.0.0.1:8000
*  create new user - register/
*  get JWT Token - /token/

## Features:

*  User Authentication and Security: The application ensures security through JWT authentication, safeguarding user accounts and data.
*  Email-Based Account Verification: To enhance account security, an email verification process can be implemented, requiring users to verify their email addresses during registration.
*  Administrative Panel: The platform includes an admin panel accessible at /admin/, empowering administrators to manage users, monitor activities, and oversee the overall functioning of the platform.
*  Comprehensive Documentation: The API is thoroughly documented using tools like Swagger, providing users and developers with clear and accessible information on endpoints, functionalities, and integration details.
*  Docker Compatibility: The application supports Docker, making it easier to deploy and manage in various environments.
*  Group Purchase Lists: Users can create lists of items for a group purchase, allowing them to collectively order products and receive group discounts on the entire list.
*  Invitations and Group Formation: Users can invite others to join their purchasing group, fostering collaboration and enabling multiple users to contribute to and benefit from shared orders.
*  Display of Discounts and Savings: The platform showcases the discounts and savings achieved through group purchases, giving users a clear view of the economic benefits they've gained by participating in shared buying.
