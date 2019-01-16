import pytest, json
import datetime
from application import create_app
from models.questions_model import questions_list,questionsmodel

@pytest.fixture
def cli_ent():
    """
    Creates a test client fixture to be used in several test cases
    """
    app=create_app()
    client=app.test_client()
    return client

class TestCreateQuestion():
    
    def test_missing_question_key(self,cli_ent):
        """
            This tests if one of the json keys wasn't provided.
        """
        response=cli_ent.post(
            '/api/v1/questions',
            data=json.dumps(dict(
                title="Access a value after an update query in postgresql",
                body="I want to display the values to a user after they have updated instead of just an update message",
                userid=1,
                )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==500
        assert "One of the json key is missing" in data["error_msg"]

    def test_createquestion(self,cli_ent):
        """
        This tests an endpoint to create a question
         and uses test client of flask app.
        This test if the enpoint creates and returns a 
        question id,title and description
        """
        now=datetime.datetime.now()
        now=now.strftime("%Y-%m-%d %H:%M")
        response=cli_ent.post(
            '/api/v1/questions',
            data=json.dumps(dict(
                title="Access a value after an update query in postgresql",
                body="I want to display the values to a user after they have updated instead of just an update message",
                userid=1,
                meetupid=1
                )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==201
        assert 1==data["data"]["userid"]
        assert "Access a value after an update query in postgresql" in data["data"]["title"]
        assert "I want to display the values to a user after they have updated instead of just an update message" in data["data"]["body"]

    def test_createquestion_empty_value(self,cli_ent):
        """
        This tests if one of the values wasn't provided.
        """
        response=cli_ent.post(
            '/api/v1/questions',
            data=json.dumps(dict(
                title="Access a value after an update query in postgresql",
                body=" ",
                userid=1,
                meetupid=1
                )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==400
        assert "Please fill all the question information" in data["error"]
        assert 400==data["status"]

    def test_createquestion_invalid_value(self,cli_ent):
        """
        This tests if the values are invalid. An integer instead of a string.
        """
        response=cli_ent.post(
            '/api/v1/questions',
            data=json.dumps(dict(
                title="Access a value after an update query in postgresql",
                body="I want to display the values to a user after they have updated instead of just an update message",
                userid="1",
                meetupid=1
                )),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==400
        assert "Please provide valid data" in data["error"]
        assert 400==data["status"]

#Class to test an endpoint that votes on question up or down.It has instance methods
class TestVoteQuestion():
    
    def test_upvote(self,cli_ent):
        """
        Tests if the enpoint can implement an up-vote on a question
        """
        response=cli_ent.patch(
            '/api/v1/questions/1/upvote',
            content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==200
        assert data['data']["votes"]==1

    def test_upvote_empty_quetion(self,cli_ent):
        """
        Tests if the enpoint would reject an up-vote
          to question that doesn't exist
        """
        response=cli_ent.patch('/api/v1/questions/2/upvote',content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==403
        assert data['error']=='Forbidden. The question doesn\'t exist'

    def test_downvote(self,cli_ent):
        """
        Tests if the enpoint can implement an downvote-vote on a question
        """
        response=cli_ent.patch('/api/v1/questions/1/downvote',content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==200
        assert data['data']["votes"]==0
        
    def test_downvote_empty_quetion(self,cli_ent):
        """
        Tests if the enpoint would reject an down-vote
          to question that doesn't exist
        """
        response=cli_ent.patch('/api/v1/questions/2/downvote',content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==403
        assert data['error']=='Forbidden. The question doesn\'t exist'