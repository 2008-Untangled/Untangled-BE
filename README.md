# Untangled Backend

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Build Status](https://travis-ci.com/travis-ci/travis-web.svg?branch=master)](https://www.travis-ci.com/github/2008-Untangled/Untangled-BE)

  <h3 align="center">Untangled Backend</h3>

  <p align="center">
    This is the Back End repository for the <a href="https://github.com/2008-Untangled">Untangled</a> application, which works in tandem with the <a href="https://github.com/2008-Untangled/Untangled-FE">Untangled Frontend Repository</a>. This Backend piece returns information to the Front End through API requests.
    <br />
    <a href="https://github.com/2008-Untangled/Untangled-BE"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- for adding a demo video
    <a href="Add our video link here">View Demo</a>  · -->
    ·
    <a href="https://github.com/2008-Untangled/Untangled-BE/issues">Report Bug</a>
    ·
    <a href="https://github.com/2008-Untangled/Untangled-BE/issues">Request Feature</a>
  </p>
</p>

### Table of Contents

1. [About This Project](#about-this-project)
   * [Built With](#built-with)
1. [Virtual Environment setup](#virtual-environment-setup)
1. [Database Setup](#database-setup)
1. [Running Tests](#runing-tests)
1. [Endpoints](#endpoints)
1. [Endpoints Table](#endpoints-table)
1. [Database Schema](#database-schema)
1. [Roadmap](#roadmap)
1. [Contributing](#contributing)
1. [Contact](#contact)


## About This Project
Visit [Untangled](https://github.com/2008-Untangled) to view all the repositories associated with this application.

This Backend application stores all the relevant data needed for the Untangled application.  It has information for users, rooms, and memories, and allows for updates to users and memories.  It responds to the Frontend of the application through API requests and responses.  Scroll down to the endpoints section see what is available.  

### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Docker](https://www.docker.com/)
* [Travis CI](https://www.travis-ci.com/)
* [Heroku](https://www.heroku.com/)

## Virtual Environment setup

```bash
# build a virtual environment to install your Python packages
python3 -m venv ./venv

# 'activate' the virtual environment for your project
# do this every time you start a new terminal and enter your project folder
source venv/bin/activate

# install your Python packages
pip3 install -r requirements.txt
```

To shut off your virtual environment, run `deactivate` at a terminal where you
have an active virtual environment.


## Database Setup

```bash
createdb untangled_dev
createdb untangled_test

export DATABASE_URL=postgresql://localhost:5432/untangled_dev

# examine any database models you have set up
python3 manage.py db migrate

# "upgrade" your database schema to use the changes you've made in your models
python3 manage.py db upgrade

# then apply the same for your test database:
export DATABASE_URL=postgresql://localhost:5432/untangled_test
python3 manage.py db upgrade

# you can seed your database with:
python3 manage.py db_seed

```


## Running Tests

If you just want to run your tests, `pytest` by itself will do the job.

In order to return a test coverage report run:
```bash
# remove any previous test caching, previous coverage reports, and a database
# of coverage data from the last time you ran this
rm -rf .pytest_cache/ coverage_html_report/ .coverage

# set your database url for your test database and use 'coverage' to launch
# pytest
DATABASE_URL=postgresql://localhost/untangled_test coverage run -m pytest

# generate the HTML reports
coverage html

# open the coverage report in your browser
open coverage_html_report/index.html

# count how many 'assert' calls you make in your tests
# my last project using this structure had 76 tests and 296 assertions that
# made sure every little thing got tested
grep -R assert tests | grep '.py:' | wc -l
```


## Endpoints

All endpoints can be reached at:
```
https://untangled-be.herokuapp.com/api/v1/
```
- GET and PATCH endpoints will return a 200 status code on success
- POST endpoints will return a 201 status code on success
- DELETE endpoints will return a 204 status code on success

Failure conditions will return an appropriate 400-series or 500-series error
and a JSON payload indicating helpful errors in a format such as:
```json
{
  "error": 404,
  "message": "Resource not found"
}
```
#### GET request:  Require no headers or body. <br>
#### PATCH request:  Require a body with the new information as a JSON payload.  For example, the body for a user patch request:
```json
{
  "name": "ian",
  "email": "ian.douglas@iandouglas.com"
}
```

---

## Endpoints Table
`https://untangled-be.herokuapp.com/api/v1`
| Description | URL | Verb | Request Body | Sample Success Response |
|----|----|----|----|----|
| Get All Users |`/users`| GET | | <pre>{<br>   "success": true,<br>   "results": [<br>     {<br>       "id": `<int>`,<br>       "name": "`<string>`"<br>       "email": "`<string>`"<br>     }<br>   ]<br>}</pre>
| Get A User By Id |`/users/:id`| GET | | <pre>{<br>    "id": `<int>`,<br>    "name": "`<string>`",<br>    "email": "`<string>`"<br>    "success": ture<br>}</pre>
| Get All Rooms |`/users/:id/rooms`| GET || <pre>{<br>  "success": true,<br>  "data": [<br>    {<br>      "id": `<int>`, <br>      "name": "`<string>`", <br>      "image": "`<string>`",<br>      "user_id": `<int>`<br>     },<br>     {...}<br>   ]<br>} </pre>|
| Get A Room By Id |`/rooms/:id`| GET | | <pre>{<br>  "success": true,<br>  "data": {<br>    "id": `<int>`<br>    "name": "`<string>`"<br>    "image": "`<string>`",<br>    "user_id": `<int>`<br>  }<br>}    |
| Get All Memories For A Room |`/rooms/:id/memories`| GET | | <pre> {<br>   "success": true,<br>   "data": [<br>       {<br>        "id": `<int>`,<br>        "description": "`<string>`",<br>        "image": "`<string>`",<br>        "song": "`<string>`",<br>        "aromas": "`<string>`",<br>        "x": `<int>`,<br>        "y": `<int>`,<br>        "room_id": `<int>`<br>       },<br>       {<br>        "id": `<int>`,<br>        "description": "`<string>`",<br>        "image": "`<string>`",<br>        "song": "`<string>`",<br>        "aromas": "`<string>`",<br>        "x": `<int>`,<br>        "y": `<int>`,<br>        "room_id": `<int>`<br>       }<br>    ]<br>} </pre> |
| Update a Memory By Id |`/memories/:id`| PATCH | <pre>{<br>  "description": "`<string>`",<br>  "image": "`<string>`",<br>  "song": "`<string>`",<br>  "aromas": "`<string>`",<br>  "x": `<int>`,<br>  "y": `<int>`<br>}</pre>| <pre> {<br>   "success": true,<br>   "data": {<br>        "id": `<int>`,<br>        "description": "`<string>`",<br>        "image": "`<string>`",<br>        "song": "`<string>`",<br>        "aromas": "`<string>`",<br>        "x": `<int>`,<br>        "y": `<int>`,<br>        "room_id": `<int>`<br>     }<br>} </pre> |


<!-- DB SCHEMA -->
## Database Schema
<img alt="Database Schema" src="https://user-images.githubusercontent.com/65255478/109689580-aae31980-7b42-11eb-8ac5-6d932ae06945.png">

<!-- ROADMAP -->
## Roadmap

See [Open Issues](https://github.com/2008-Untangled/Music-Service-API/issues) or visit our [Project Board](https://github.com/orgs/2008-Untangled/projects/1) for a list of proposed features, known issues, and project extensions.


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make this community such an amazing and fun place to learn, grow, and create! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch ```git checkout -b feature/NewGreatFeature```
3. Commit your Changes ```git commit -m 'Add some NewGreatFeature'```
4. Push to the Branch ```git push origin feature/NewGreatFeature```
5. Open a new Pull Request!


<!-- CONTACT -->
## Contact

Bryce Jarrett &nbsp;&nbsp;&nbsp;&nbsp; - [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/bryce-jarrett/) - [GitHub](https://github.com/brycemara)

Cameron Romo &nbsp; - [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/cameron-romo-64b3a69b/) - [GitHub](https://github.com/cameronRomo)

Joe Lopez &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/joseph-lopez-100/) - [GitHub](https://github.com/Codo-Baggins)

Estelle Staffieri &nbsp; - [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/estellestaffieri/) - [GitHub](https://github.com/Estaffieri)

Grant Dempsey &nbsp;- [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/grant-dempsey-8a9a16169/) - [GitHub](https://github.com/GDemps)

Eduardo Parra &nbsp;&nbsp;&nbsp; - [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/eduardo--parra/) - [GitHub](https://github.com/helloeduardo)

Jesse Mellinger &nbsp;&nbsp;- [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/jesse-mellinger/) - [GitHub](https://github.com/JesseMellinger)

Sean Steel &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/sean-steel/) - [GitHub](https://github.com/s-steel)



Project Link: [Untangled](https://github.com/2008-Untangled)



<!-- ACKNOWLEDGEMENTS -->
<!-- Add resources that were used to help create this project here -->

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/2008-Untangled/Untangled-BE
[contributors-url]: https://github.com/2008-Untangled/Untangled-BE/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/2008-Untangled/Untangled-BE
[forks-url]: https://github.com/2008-Untangled/Untangled-BE/network/members
[stars-shield]: https://img.shields.io/github/stars/2008-Untangled/Untangled-BE
[stars-url]: https://github.com/2008-Untangled/Untangled-BE/stargazers
[issues-shield]: https://img.shields.io/github/issues/2008-Untangled/Untangled-BE
[issues-url]: https://github.com/2008-Untangled/Untangled-BE/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555