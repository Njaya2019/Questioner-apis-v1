import pytest, json
import datetime
from application import create_app


"""""""Creates a test client fixture to be used in several test cases"""""""

@pytest.fixture
def cli_ent():
    app=create_app()
    client=app.test_client()
    return client

"""""""This tests an endpoint to create a meetup and uses test client of flask app"""""""
def test_createmeetup(cli_ent):
    now=datetime.datetime.now()
    now=now.strftime("%Y-%m-%d %H:%M")
    response=cli_ent.post('/api/v1/admin/createmeetup',data=json.dumps(dict(meetup_title="python programming for beginners",meetup_description="We started this to help each other.Regardless of your experince just join us share and learn.Welcome!",location="Mombasa,Kenya",date_created=now)),content_type="application/json")
    data=json.loads(response.data)
    assert response.status_code==201
    assert "congratulations you have created a meet up" in data["message"]

"""""""This tests if one of the values of meet up information wasn't provided"""""""
def test_createmeetup_empty_value(cli_ent):
    now=datetime.datetime.now()
    now=now.strftime("%Y-%m-%d %H:%M")
    response=cli_ent.post('/api/v1/admin/createmeetup',data=json.dumps(dict(meetup_title="python programming for beginners",meetup_description=None,location="Mombasa,Kenya",date_created=now)),content_type="application/json")
    data=json.loads(response.data)
    assert response.status_code==422
    assert "Please fill all the meet up information" in data["message"]

"""""""This tests if the values are invalid. An integer instead of a string."""""""
def test_createmeetup_invalid_value(cli_ent):
    now=datetime.datetime.now()
    now=now.strftime("%Y-%m-%d %H:%M")
    response=cli_ent.post('/api/v1/admin/createmeetup',data=json.dumps(dict(meetup_title="python programming for beginners",meetup_description=1234,location="Mombasa,Kenya",date_created=now)),content_type="application/json")
    data=json.loads(response.data)
    assert response.status_code==400
    assert "Please provide valid data" in data["message"]
