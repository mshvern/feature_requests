# Feature Requests App
### Core Stack
* Flask
* SQLAlchemy
* jQuery
* Bootstrap
###Development Approach
The first thing that needs to be decided when creating an MVP is a core tech stack to be used.

Flask was chosen as a framework because of it's simplicity and extensive documentation. Therefore, SQLAlchemy followed as the most popular way to provide a powerful and developer-friendly ORM. Bootstrap was chosen for its ease of integration, color-coded buttons, and simple yet powerful grid layout. 
Mimesis was chosen for generating fake data for initial feature requests. 

When it comes to testing, the approach was fairly standard, utilizing stdlib's unittest and unittest.mock.      

Ultimately, all the core dependencies were established for a single reason - fast development process.


### Deployment
To easily make this deployment automated, Heroku was chosen as a cloud platform. Since Heroku natively supports WSGIs, nginx was managed to be avoided and as a result, only gunicorn needed to be configured (which happens in Procfile).  

The project itself is very quick to set-up (provided you have heroku-cli installed and are logged in).

In your terminal (tested on Ubuntu):
    
    heroku create
    git push heroku master
    heroku ps:scale web=1
      
After executing these commands, you can access the application via a url that was given to you at `heroku create` stage or simply by typing the following in your terminal:
    
    heroku open
    
### Running a Development Server and Tests
Clone this repository and create a virtualenv in your location of choice. After activating the environment, install the dependencies: 

    pip install -r requirements.txt
    
After this, you should launch a script dedicated to database setup.

    python -m database.database_setup

After the database setup is finished and mock data is generated, you can now run a development server.

    python -m flask run
    
To run tests, execute the following command in your terminal:

    python -m nose

#### Ideas On Future Development
* Make the layout of the main page responsive and mobile-friendly
* Ideally, utilize npm and bower to manage Javascript dependencies, instead of linking CDNs
* Utilize a framework instead of relying on jQuery Templates
* Improve the design of the main page
* Implement authentication and authorization systems
* Refactor the project structure as it grows bigger
