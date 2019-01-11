from flask import Flask
from app.api.v1.endpoints.meetups import meetups_blueprint
from app.api.v1.endpoints.questions import questions_blueprint

"""""Creates a flask app"""
def create_app():

    app=Flask(__name__)
    """""""register flask blueprints"""""""
    app.register_blueprint(meetups_blueprint)
    app.register_blueprint(questions_blueprint)
    return app

app=create_app()


"""""""Runs flask application"""""""
if __name__=="__main__":
    app.run(debug=True)