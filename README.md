![Flask Logo](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fupload.wikimedia.org%2Fwikipedia%2Fcommons%2Fthumb%2F3%2F3c%2FFlask_logo.svg%2F1200px-Flask_logo.svg.png&f=1&nofb=1)
# Setup environement

Follow all these steps :

*All commands must be runned in App root.*

```bash
# Create Vitual Python env
python3 -m venv venv

# Activate python environement
source ./venv/bin/activate

# Install all required dependencies
pip install -r requirements.txt

# Export main file path
export FLASK_APP="main.py"

# Define dev mode to have debugger
export FLASK_ENV="development"

# Run your app
flask run
```

## Framework info

This app is runnig with [Flask](https://flask.palletsprojects.com/en/1.1.x/)