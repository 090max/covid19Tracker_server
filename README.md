

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Covid 19 Tracker</h3>

  <p align="center">
   A python flask API that regularly tracks Covid19 cases in India. 
    <br />
    <a href="http://covidtracker19.herokuapp.com/">View Demo</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [API Information](#api-information)
  * [Routes Information](#routes-information)
  * [API Files Information](#api-files-information)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
  * [Database Setup](#database-setup)
  * [Heroku Hosting](#heroku-hosting)
* [Contributing](#contributing)
* [License](#license)




<!-- API Information -->
## API Information
## Routes Information

* /getgeneral : Returns a JSON data of the current cases report of India.
* /getanalytics : Returns a JSON data of the past case report along with current cases in India .This is specifically for data visualization.
* /getstate?state=statename :Return a JSON data of the current case report of a particular state.Note : statename should be in lowercases and without any white spaces.
* /getstate?state=all :Return a JSON data of the current case report of all Indian states.
  
## API Files Information

* app.py : Responsible for routing purpose.
* information_fetcher.py : Fetches the information for a particular route.
* scrapper.py :Scrapes the data from "https://www.mohfw.gov.in/"
* clock.py :Runs the cron job in the given interval of time.
  

### Built With
* Python
* Flask
* Mongo DB


<!-- GETTING STARTED -->
## Getting Started

Here is a quick installation guide.Please note this is for Ubuntu machines.

### Installation

1. To Run the application for development ,Clone the repo
```sh
git clone https://github.com/090max/covid19Tracker_server
```
2. Install requirements.
```sh
pip install requirements.txt
```
3. Run the application.`
```Py
python app.py
```
### Database Setup

1. Go to any of the Mongo DB hosting website( ex - Mongo Atlas)
2. Create a Database named "covid19".
3. Create two collections named "general" and "state_wise"
4. Paste the connection url in db_helper.py file.


### Heroku Hosting

1. Login to heroku and create a new web app. 

2. Install heroku CLI .Follow this <a href="https://devcenter.heroku.com/articles/heroku-cli">link</a>.

3. Run the following commands on your terminal in the directory of project.Note : The Procfile and requirements.txt is already defined here , so no need of making a new one.
```sh
git init
```
```sh
heroku git:remote -a <your heroku app name>
```
```sh
git add .
```
```sh
git commit -m "Commit info"
```

```sh
git push heroku master
```
4. Run the following commands to scale the clock (cron job) and web app , run on your terminal.
```sh
heroku ps:scale clock =1
```
```sh
heroku ps:scale web=1
```
5. Add time zone to the heroku application ,run this on terminal
```sh
heroku config:add TZ="Asia/Kolkata"
```
6. Thats is your application is LIVE !!.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/FeatureBranch`)
3. Commit your Changes (`git commit -m 'Add some Feature'`)
4. Push to the Branch (`git push origin feature/FeatureBranch`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


