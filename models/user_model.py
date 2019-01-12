from werkzeug.security import check_password_hash,generate_password_hash

"""""""A global list to store users"""""""
users_list=[]

"""""""A class that has instance models and class methods"""""""
class users_model():
    def __init__(self,first_name,second_name,gender,email,password,confirm_pwd):
        self.first_name=first_name
        self.second_name=second_name
        self.isAdmin=True
        self.gender=gender
        self.email=email
        self.password=password
        self.confirm_pwd=confirm_pwd
        self.user_id=len(users_list)+1
    """""""An instance method to add a user to user's list global"""""""
    def register_user(self):
        if self.password!=self.confirm_pwd:
            return "The passwords do not match"
        for user in users_list:
            if user['email']==self.email:
                return "The email already exists. Choose another email"
        hashed_password=generate_password_hash(self.password)
        users_dict={"user_id":self.user_id,'user_firstname':self.first_name,'user_secondname':self.second_name,'isAdmin':self.isAdmin,'user_gender':self.gender,'email':self.email,'password':hashed_password}
        users_list.append(users_dict)
        return users_dict
        
            
