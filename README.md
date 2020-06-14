# Image-Steganography-WebApp
# Steps to Run this Project:

1.Create an environment
  Create a project folder and a venv folder within:

  $ mkdir myproject
  $ cd myproject
  $ python3 -m venv venv

  On Windows:
  $ py -3 -m venv venv

  If you needed to install virtualenv because you are using Python 2, use the following command instead:
  $ python2 -m virtualenv venv

  On Windows:
  > \Python27\Scripts\virtualenv.exe venv

2.Activate the environment
  Before you work on your project, activate the corresponding environment:
  $ . venv/bin/activate

  On Windows:
  > venv\Scripts\activate

  Your shell prompt will change to show the name of the activated environment.

3.Install Flask
  Within the activated environment, use the following command to install Flask:
  $ pip install Flask

  Flask is now installed.

4.It’s a good idea to save the packages (including version numbers) that are being used in the project:
  $ pip freeze > requirements.txt

5. For Heroku to be able to run our application like it should, we need to define a set of processes/commands that it should run beforehand. 
    These commands are located in the Procfile:
    $ web: gunicorn app:app

6.Now Create a Heroku Account
  Once that is out of the way, on the dashboard, select New -> Create new app:
  Once the application is created on Heroku, we're ready to deploy it online.

7.To upload our code, we'll use Git. First, let's make a git repository:
  $ git init .
  
8.And now, let's add our files and commit:
  $ git add app.py Procfile requirements.txt
  $ git commit -m "first commit"
  
9.To finally deploy the application, we'll need to install the Heroku CLI with which we'll run Heroku-related commands. 
  Let's login to our account using our credentials by running the command:
  $ heroku login -i
  
  Alternatively, we can login using the browser if we run the command:
  $ heroku login

  At this point, while logged in, we should add our repository to the remote one:
  $ heroku git:remote -a {your-project-name}

10.Now upload the project by pushing it to Heroku:
  $ git push heroku master
  
11.A lengthy progress log should come up on your terminal.

# Congratulations, you have successfully uploaded your first web app to Heroku! It's now time now to test and verify our API.




