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
        assert response.status_code==400
        assert "Please provide a valid email" in data["error_msg"]
        assert 400==data["status"]

class TestLoginUser():
    """""""This instance method test for successful sign in of users""""""" 
    def test_login_user(self,cli_ent):
        response=cli_ent.post('/api/v1/login',data=json.dumps(dict(email="jumamasha@gmail.com",password="1234")),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==200
        assert data["user"]["user_firstname"]=="Juma"
        assert data["user"]["user_secondname"]=="Masha"
    
    """""""This instance method test when user passes empty credentials""""""" 
    def test_login_user_empty_values(self,cli_ent):
        response=cli_ent.post('/api/v1/login',data=json.dumps(dict(email="",password="")),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==400
        assert data["error_msg"]=="Please fill both email and password to login"
    
    """""""This instance method test when user passes invalid email""""""" 
    def test_login_user_invalid_email(self,cli_ent):
        response=cli_ent.post('/api/v1/login',data=json.dumps(dict(email="jumamashagmail.com",password="1234")),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==400
        assert data["error_msg"]=="Please provide a valid email"

    """""""This instance method test when the email doesn't""""""" 
    def test_login_user_email_notfound(self,cli_ent):
        response=cli_ent.post('/api/v1/login',data=json.dumps(dict(email="yahyanyiro@gmail.com",password="1234")),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==401
        assert data["error_msg"]=="The user's email provided doesn't exist"
    """""""This instance method test when the password in incorrect"""""""   
    def test_login_user_password_incorrect(self,cli_ent):
        response=cli_ent.post('/api/v1/login',data=json.dumps(dict(email="jumamasha@gmail.com",password="4321")),content_type="application/json")
        data=json.loads(response.data)
        assert response.status_code==401
        assert data["error_msg"]=="The user's password provided is incorrect"
    
    


