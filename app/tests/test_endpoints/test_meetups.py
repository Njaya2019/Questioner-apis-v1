import pytest, json
import datetime
from application import create_app
from models.meetups_model import meetups_list,meetups

@pytest.fixture
def cli_ent():
    """
    Creates a test client fixture to be used in several test cases
    """
    app=create_app()
    client=app.test_client()
    return client

class TestCreateMeetUps():
    def test_missing_meetupkey(self,cli_ent):
        """
            This Instance method to test if a json meetup
             key is missing
        """
        response=cli_ent.post(
            '/api/v1/meetups',
            data=json.dumps(
                dict(
                    description="We started this to help each other.Regardless of your experince just join us share and learn.Welcome!",
                    location="Mombasa,Kenya"
                    )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==500
        assert "One of the json key is missing"==data["error_msg"]
    
    def test_createmeetup(self,cli_ent):
        """
        Instance method to test create a meetup.
        This tests an endpoint to create a meetup and uses test
         client of flask app
        """
        now=datetime.datetime.now()
        now=now.strftime("%Y-%m-%d %H:%M")
        response=cli_ent.post(
            '/api/v1/meetups',
            data=json.dumps(
                dict(
                    topic="python programming for beginners",
                    description="We started this to help each other.Regardless of your experince just join us share and learn.Welcome!",
                    location="Mombasa,Kenya"
                    )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==201
        assert "python programming for beginners"==data["data"]["topic"]

    def test_createmeetup_empty_value(self,cli_ent):
        """Instance method to test empty posted values.
        This tests if one of the values of meet up
         information wasn't provided.
        """
        now=datetime.datetime.now()
        now=now.strftime("%Y-%m-%d %H:%M")
        response=cli_ent.post(
            '/api/v1/meetups',
            data=json.dumps(
                dict(
                    topic="python programming for beginners",
                    description=" ",
                    location="Mombasa,Kenya"
                    )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==400
        assert "Please fill all the meet up information" in data["error_msg"]

    def test_createmeetup_invalid_value(self,cli_ent):
        """Instance method to test posted invalid values.
        This tests if the values are invalid.
         An integer instead of a string.
        """
        now=datetime.datetime.now()
        now=now.strftime("%Y-%m-%d %H:%M")
        response=cli_ent.post(
            '/api/v1/meetups',
            data=json.dumps(dict(
                topic="python programming for beginners",
                description=1234,
                location="Mombasa,Kenya"
                )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==400
        assert "Please provide valid data" in data["error_msg"]

class TestGetMeetUps():

    def test_get_a_meetup_record(self,cli_ent):
        """
        A test to get a specific meetup record
        """
        response=cli_ent.get('/api/v1/meetups/'+str(1))
        data=json.loads(response.data)
        assert response.status_code==200
        assert data["data"]["topic"]=="python programming for beginners"

    def test_get_a_meetup_record_notfound(self,cli_ent):
        """
        Tests if the meetup wasn't found
        """
        response=cli_ent.get('/api/v1/meetups/'+str(2))
        data=json.loads(response.data)
        assert response.status_code==404
        assert 'The meetup record wasn\'t found' in data["error_msg"]

    def test_get_all_meetups(self,cli_ent):
        """
        Tests if the enpoint can get all meet ups
        """
        response=cli_ent.get('/api/v1/meetups')
        data=json.loads(response.data)
        assert response.status_code==200
        assert data["data"]==meetups_list

#This class tests for response to an rsvp
class TestRsvp():
    
    def test_respond_rsvp(self,cli_ent):
        """
        This test if a response if successfully submitted
        """
        response=cli_ent.post(
            '/api/v1/meetups/1/rsvp',
            data=json.dumps(dict(
                userid=1,
                RSVPresponse="Yes"
                )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==201
        assert "Yes"==data["data"]["status"]
    def test_respond_rsvp_inexist_meetup(self,cli_ent):
        """
        When the meetup doesn't exist
        """
        response=cli_ent.post(
            '/api/v1/meetups/2/rsvp',
            data=json.dumps(dict(
                userid=1,
                RSVPresponse="Yes"
                )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==404
        assert "The meetup no longer exists or doesn't exists"==data["error_msg"]