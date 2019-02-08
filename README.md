# strava-app


A simple app which uses Strava's API to get and display information about laps (as subsets of activities). The app gives visibility into laps disambiguated from their parent activity, which Strava does not provide.

The app is written in Python, using the Flask framework and Jinja templates. It uses Flask-Table to format data and and Requests to handle calling Strava's API.

The app is deployed on Heroku at https://dry-mountain-30530.herokuapp.com/
