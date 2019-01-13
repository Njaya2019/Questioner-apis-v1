import pytest, json
from application import create_app



"""""""Creates a test client fixture to be used in several test cases"""""""

@pytest.fixture
def cli_ent():
    app=create_app()
    client=app.test_client()
    return client

"""""""A class to test registration of users. It has insatance methods as tests"""""""

class TestsUserRegistration():
    
    """""""This instance method test for successful registration of users""""""" 
    def test_register_user(self,cli_ent):
        response=cli_ent.post('/api/v1/registration',data=json.dumps(dict(user_firstname="Juma",user_secondname="Masha",user_gender="Male",user_email="jumamasha@gmail.com",account_type="Admin",password="1234",confirm_password="1234")),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==201
        """""""This test if the enpoint registers a user and returns a user id,first name and second name"""""""
        assert 1==data["user"]["user_id"]
        assert "Juma"==data["user"]["user_firstname"]
        assert "Masha"==data["user"]["user_secondname"]
        assert "Male"==data["user"]["user_gender"]
        assert True==data["user"]["isAdmin"]
    """""""This intance method tests if user values passed are empty"""""""
    def test_register_user_empty_values(self,cli_ent):
        response=cli_ent.post('/api/v1/registration',data=json.dumps(dict(user_firstname=None,user_secondname=None,user_gender="Male",user_email="jumamasha@gmail.com",account_type="Admin",password="1234",confirm_password="1234")),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==400
        assert "All user's information is required to register" in data["error_msg"]

    """""""This instance method tests if the user values passed are valid"""""""
    def test_register_user_invalid_values(self,cli_ent):
        response=cli_ent.post('/api/v1/registration',data=json.dumps(dict(user_firstname=1,user_secondname=1234,user_gender="Male",user_email="jumamasha@gmail.com",account_type="Admin",password="1234",confirm_password="1234")),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==400
        assert "Please provide user valid values" in data["error_msg"]
        assert 400==data["status"]
    def test_register_user_invalid_email(self,cli_ent):
        response=cli_ent.post('/api/v1/registration',data=json.dumps(dict(user_firstname="Willy",user_secondname="Mzae",user_gender="Male",user_email="willymzaegmail.com",account_type="Admin",password="1234",confirm_password="1234")),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==422
        assert "Please provide a valid email" in data["error_msg"]
        assert 400==data["status"]


