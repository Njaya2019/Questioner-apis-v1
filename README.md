[![Build Status](https://travis-ci.org/Njaya2019/Questioner-apis-v1.svg?branch=develope)](https://travis-ci.org/Njaya2019/Questioner-apis-v1)[![Coverage Status](https://coveralls.io/repos/github/Njaya2019/Questioner-apis-v1/badge.svg?branch=develope)](https://coveralls.io/github/Njaya2019/Questioner-apis-v1?branch=develope)[![Maintainability](https://api.codeclimate.com/v1/badges/a571e9674add385974ab/maintainability)](https://codeclimate.com/github/Njaya2019/Questioner-apis-v1/maintainability)

# Questioner api overview
It's an api that where a user can register as an admin or a regular user.An admin can create or delete a meetup.A regular user can request to join a meetup.Once on a meetup he/she can ask a question, delete the question,comment on his or other questions and can down vote or up vote a question.

## Endpoints
The api has the following endpoints:-

| Endpoints                                     | Request       | function       |
| ------------------------                      | ------------- |----------------|
|/api/v1/meetups                                | POST          | Create a meetup|
| /api/v1/meetups/<meetupid>                    | GET           | get a  meetup  |
| /api/v1/meetups                               | GET           | get all meetups|
| /api/v1/questions                             | POST          | ask question   |
| /api/v1/questions/<int:question_id>/upvote    | PATCH         | upvote         |
| /api/v1/question/<int:question_id>/downvote   | PATCH         | downvote       |
| /api/v1/meetups/1/rsvp                        | POST          | RSVP           |
| /api/v1/login                                 | POST          | Login          |
| /api/v1/signup                                | POST          | Sign up        |

api/v1/user/meetups/1/rsvp
## Technologies
The project is created with
```
* python version:3.6
* Flask framework
```
## Installation
1. Install python version 3.6
  ```
  Find installation instructions for your OS on python.org
  ```
2. clone the project
  ```
  - git clone -b develope https://github.com/Njaya2019/Questioner-apis-v1.git
  ```
3. Get in to the project's directory
  ```
  - cd Questioner-apis-v1
  ```
4. Install all project's dependancies
  ```
  - pip install -r requirements.txt
  ```
5. Run the app
  ```
  - python application.py
  ```
## Usage

#### Use postman to run endpoints

1. Install postman
2. Run postman and open an account if you don't have one.
3. While flask still running insert the url link of an endpoint,choose request       method and send. The response will be displayed at the bottom.
4. Incases of a post like **POST /api/v1/meetups**.    Select body, raw and change text content type to application/json.
Example json file endpoint.
```
{"topic":"Object oriented programming with python","description":"Learn all the basics of OOP.Inheritance,encapusaltion,polymorphism and more","location":"Kenya,Mombasa"}
```


#### Postman link

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/8649524d0a7494780a9e)

## Testing
#### Tests tools
```python
* Pytest Framework
```
Tests were written first to make sure the endpoints returns required response to the user.
The test below is an `example`. It tests `POST /api/v1/meetups` endpoint that creates a new meetup.


```python

def test_createmeetup(cli_ent):
    response=cli_ent.post(
      '/api/v1/meetups',
          data=json.dumps(dict(topic="python programming for beginners",description="We started this to help each other.Regardless of your      experince just join us share and learn.Welcome!",
          location="Mombasa,Kenya")
          ),content_type="application/json")
    data=json.loads(response.data)
    assert response.status_code==201
    assert "python programming for beginners"==data["data"]["topic"]
    
```

#### How to run tests.
```
py.test -vv
```
## Errors handlers
The application has error handlers. This prevents the app from crushing completely. The following are some:-
`500 internal sever error handler`
This error hundler returns a json message that there is a programming error or the server is overloaded. Note this  custom error will be seen when debug is `False`
```python
@app.errorhandler(500)
def internal_erro(error):
    """
        This error hundler returns a json message that
         there is a programming error or the server is 
         overloaded.
    """
    return jsonify({
        "error":"There is a programming error or the server is overloaded",
        "status": 500
        }), 500
```
`404 page not found error handler`
This error hundler returns a json message when the requested resource wasn't found.

```python
@app.errorhandler(404)
def page_not_found(error):
    """
        This error hundler returns a json message when
         the resource requested wasn't found
    """
    return jsonify({
        "error":"The requested resource wasn't found",
        "status": 404
        }), 404

```

## Contributing
Pull requests are welcome. For major changes, Open an issue first to discuss what you would like to change.

## Collaborators
[Samuel munyili](https://github.com/munyili-samuel)

## Authors
[Andrew Njaya](https://github.com/Njaya2019)