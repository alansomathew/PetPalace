# Django Project README

## Project Overview



## Prerequisites

- Python 3.x
- pip (Python package installer)

## Setting up a Virtual Environment

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Windows
.\venv\Scripts\activate

# On Unix or MacOS
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Start the development server
python manage.py runserver

# Creating superuser or Admin
python manage.py createsuperuser




