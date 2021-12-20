from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraping

app= Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config['MONGO_URI']= "mongodb://localhost:27017/mars_app"
mongo=PyMongo(app)

# Set Up Routes
@app.route("/")
def index():
    mars=mongo.db.mars.find_one()
    return render_template('index.html', mars=mars)

@app.route("/scrape")
def scrape():
    mars=mongo.db.mars
    #holds newly scraped data, referencing scrape_all() function in scraping.py file
    mars_data=scraping.scrape_all()

    print("=====================")
    print(mars_data)
    print("=====================")

    mars.replace_one({},mars_data,upsert=True)
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)