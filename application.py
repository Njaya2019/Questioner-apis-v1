from flask import Flask

"""""Creates a flask app"""
def create_app():

    app=Flask(__name__)

    return app

app=create_app()


"""""""Runs flask application"""""""
if __name__=="__main__":
    app.run(debug=True)
