# Import Dependencies 
from flask import Flask, render_template, redirect 
from flask_pymongo import PyMongo
import scrape_mars
import os



# Create an instance of Flask app
app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

##https://stackoverflow.com/questions/66278583/how-to-setup-the-flask-pymongo-configuration-to-use-it-with-a-container-with-a-m
##https://kb.objectrocket.com/elasticsearch/how-to-setup-a-mongodb-app-using-the-flask-framework-557
#Use flask_pymongo to set up connection through mLab
app.config["MONGO_URI"] = os.environ.get('authentication')
mongo = PyMongo(app)


# Use flask_pymongo to set up mongo connection locally 
# app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
# mongo = PyMongo(app)

# route that renders from index.html template and finds data in mongo
@app.route("/")
def home(): 

    # Find data
    mars_data = mongo.db.mars_data.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_data)

# Route that will trigger scrape function
@app.route("/scrape")
def scrape(): 

    # Run scrapped functions
    mars_data = mongo.db.mars_data
    mars_data.update({}, mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__": 
    app.run(debug= True)