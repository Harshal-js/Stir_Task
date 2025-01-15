from flask import Flask, render_template, redirect, url_for
from scrape_twitter import scrape_twitter_data, get_public_ip 
import pymongo

app = Flask(__name__)

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["twitter_scraper"]
collection = db["tweets"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run')
def run_script():
    trends, timestamp = scrape_twitter_data()
    
    # Fetch the latest record from MongoDB
    last_record = collection.find_one(sort=[("timestamp", -1)])
    
    if last_record is None:
        json_extract = {
            "_id": "N/A",
            "timestamp": "No records found",
            "trends": []
        }
    else:
        json_extract = {
            "_id": str(last_record["_id"]),
            "timestamp": last_record["timestamp"],
            "trends": last_record["trends"]
        }

    # Fetch public IP address (through ProxyMesh)
    ip_address = get_public_ip()  # Now this works

    return render_template(
        'results.html',
        trends=trends,
        timestamp=timestamp,
        ip_address=ip_address, 
        json_extract=json_extract
    )

if __name__ == "__main__":
    app.run(debug=True)
