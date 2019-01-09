import pytest, json
import datetime
from application import create_app
from models.questions_model import questions_list,questionsmodel


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

"""""""This tests if one of the values wasn't provided"""""""
def test_createquestion_empty_value(cli_ent):
    response=cli_ent.post('/api/v1/user/createquestion',data=json.dumps(dict(question_title="Access a value after an update query in postgresql",qusetion_description=None,user_id=1,meetup_id=1)),content_type="application/json")
    data=json.loads(response.data)
    assert response.status_code==422
    assert "Please fill all the question information" in data["error"]
    assert 422==data["status"]

"""""""This tests if the values are invalid. An integer instead of a string."""""""
def test_createquestion_invalid_value(cli_ent):
    response=cli_ent.post('/api/v1/user/createquestion',data=json.dumps(dict(question_title="Access a value after an update query in postgresql",qusetion_description="I want to display the values to a user after they have updated instead of just an update message",user_id="1",meetup_id=1)),content_type="application/json")
    data=json.loads(response.data)
    assert response.status_code==400
    assert "Please provide valid data" in data["error"]
    assert 400==data["status"]

"""""""Tests if the enpoint can implement an up-vote on a question"""""""
def test_upvote(cli_ent):
    response=cli_ent.patch('/api/v1/user/question/'+str(1)+'/upvote')
    data=json.loads(response.data)
    assert response.status_code==200
    assert data['upvoted_question']==questionsmodel.up_vote_question(1)
"""""""Tests if the enpoint would reject an up-vote  to question that doesn't exist"""""""
def test_upvote_empty_quetion(cli_ent):
    response=cli_ent.patch('/api/v1/user/question/'+str(2)+'/upvote')
    data=json.loads(response.data)
    assert response.status_code==403
    assert data['error']=='Forbidden. The question doesn\'t exist'