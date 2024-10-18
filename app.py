from flask import Flask
from routes.animal import bp_animal
from routes.employee import bp_employee


app = Flask(__name__)

app.register_blueprint(bp_animal)
app.register_blueprint(bp_employee)

@app.route("/")
def index():
    return "<h1>Welcome to our My API!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
