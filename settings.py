import os

DB_USER = os.environ.get('DB_USER', 'docker')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'docker123')
DB_SCHEMA = os.environ.get('DB_SCHEMA', 'docker')
DB_HOST = os.environ.get('DB_HOST', '127.0.0.1')
