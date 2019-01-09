import pytest, json
import datetime
from application import create_app


"""""""Creates a test client fixture to be used in several test cases"""""""

@pytest.fixture
def cli_ent():
    app=create_app()
    client=app.test_client()
    return client

"""""""This tests an endpoint to create a question and uses test client of flask app"""""""
def test_createquestion(cli_ent):
    now=datetime.datetime.now()
    now=now.strftime("%Y-%m-%d %H:%M")
    response=cli_ent.post('/api/v1/user/createquestion',data=json.dumps(dict(question_title="Access a value after an update query in postgresql",qusetion_description="I want to display the values to a user after they have updated instead of just an update message",user_id=1,meetup_id=1,date_created=now)),content_type="application/json")
    data=json.loads(response.data)
    assert response.status_code==201
    """""""This test if the enpoint creates and returns a question id,title and description"""""""
    assert 1==data["question_id"]
    assert "Access a value after an update query in postgresql" in data["question_title"]
    assert "I want to display the values to a user after they have updated instead of just an update message" in data["question_description"]