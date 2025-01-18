#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

# Create SQLite database directory if it doesn't exist
mkdir -p instance

# Initialize the database (you'll need to create this script)
python init_db.py