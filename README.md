# Stir_Task
# Twitter Trending Topics Scraper

This project is a Python-based web scraper that uses Selenium to log in to Twitter, scrape trending topics, and save the data to a MongoDB database. The application includes a Flask-based web interface to run the scraper and view results.

---

## Features

- **Twitter Login**: Automated login using Selenium.
- **Trending Topics Scraping**: Extracts Twitter's trending topics.
- **MongoDB Integration**: Stores trends and timestamps in a MongoDB database.
- **Proxy Support**: Utilizes ProxyMesh for dynamic IP routing.
- **Web Interface**:
  - **Home Page**: Run the scraper.
  - **Results Page**: View trends, timestamp, and JSON extract from MongoDB.

---

## Prerequisites

- **Python**: Version 3.8 or higher.
- **Google Chrome**: Installed and updated.
- **ChromeDriver**: Matches your Chrome version.
- **MongoDB**: Installed and running locally.
- **ProxyMesh**: Account and credentials.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/twitter-trending-scraper.git
cd twitter-trending-scraper
```

### 2. Set Up Python Environment
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Set Up MongoDB
1. Install MongoDB from [MongoDB Official Website](https://www.mongodb.com/try/download/community).
2. Start the MongoDB server:
   ```bash
   mongod
   ```
3. MongoDB will run on `localhost:27017` by default.

### 4. Configure ChromeDriver
1. Download ChromeDriver from [ChromeDriver Download Page](https://chromedriver.chromium.org/downloads).
2. Ensure the version matches your installed Google Chrome.
3. Update the `chromedriver` path in `scrape_twitter.py`:
   ```python
   driver = webdriver.Chrome(service=Service("/path/to/chromedriver"))
   ```

### 5. Add Credentials
Update the following placeholders in `scrape_twitter.py`:
- **Twitter Login**:
   ```python
   twitter_username = "your_twitter_username"
   twitter_password = "your_twitter_password"
   ```
- **ProxyMesh Credentials**:
   ```python
   proxy_username = "your_proxymesh_username"
   proxy_password = "your_proxymesh_password"
   ```

---

## Usage

### 1. Start the Flask Application
Run the Flask app:
```bash
python app.py
```

The app will start on `http://127.0.0.1:5000`.

### 2. Interact with the Web Interface
1. Open the browser and navigate to `http://127.0.0.1:5000`.
2. **Home Page**: Click the link to run the scraper.
3. **Results Page**: View the trending topics, timestamp, and the public IP used for the query.

---

## Project Structure

```
.
├── app.py              # Flask app to serve the web interface
├── scrape_twitter.py   # Selenium scraper for Twitter
├── templates/
│   ├── index.html      # Homepage template
│   └── results.html    # Results display template
├── static/             # Optional static files (e.g., CSS, JS)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## Example Output

### **Trending Topics**
- Topic 1
- Topic 2
- Topic 3
- Topic 4
- Topic 5

### **MongoDB Extract**
```json
{
  "_id": "64acdf7b3f1a2",
  "timestamp": "2025-01-15 12:30:45",
  "trends": [
    "Trend 1",
    "Trend 2",
    "Trend 3"
  ]
}
```
