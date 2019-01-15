from flask import Flask, jsonify
from app.endpoints.meetups import meetups_blueprint
from app.endpoints.questions import questions_blueprint
from app.endpoints.users_auth import userauth_blueprint

def create_app():
    """
    Creates a flask app
    """
    app=Flask(__name__)
    """
    register flask blueprints
    """
    app.register_blueprint(meetups_blueprint)
    app.register_blueprint(questions_blueprint)
    app.register_blueprint(userauth_blueprint)
    return app

app=create_app()
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

@app.errorhandler(405)
def method_not_allowed(error):
    """
        This error hundler returns a json message that
         the request couldn't be performed.
    """
    return jsonify({
        "error":"The request made cannot be performed",
        "status": 405
        }), 405

if __name__=="__main__":
    """
    Runs flask application
    """
    app.run(debug=True)