# Perform django operations
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

python manage.py createsuperuser --noinput --first_name root --last_name theonlyone # Default values come from environment variables

# Load sample data - comment this line for a clear database
python manage.py upload_sample_data

# Start Gunicorn processes with 2 worker processes and 1000 connections each
gunicorn -b 0.0.0.0:8000 --reload blogyourstuff.wsgi