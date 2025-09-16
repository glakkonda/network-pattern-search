

 ## 🚀 Network Pattern Search

A Lightweight Python Project for Searching Patterns in Text Files, with Server–Client Support and Automated tests.


 ## 📂 Project Structure

````markdown
network-pattern-search/
├── search.py        # Pattern searching utility / CLI
├── server.py        # HTTP server exposing the search API
├── client.py        # Client to query the server
├── test_search.py   # Pytest tests
├── requirements.txt # Python dependencies
├── sample.txt       # Any type of Text Files
├── .gitignore       # Ignore venv, cache, logs, etc.
├── README.md        # Documentation
````
## ⚙️ Setup
````markdown
python3 -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
````
## ▶️ Usage

#### Start the server:
````markdown
python3 server.py
````

#### Query using the client:
````markdown
python3 client.py 
````

## 🧪 Run Tests
````markdown
pytest -q
````


