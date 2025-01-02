I'll create a step-by-step tutorial for deploying a Django project on Render.com. I'll break this down into key sections:

1. Prerequisites
- A Django project ready for deployment
- A GitHub repository with your project
- A Render.com account
- PostgreSQL database (Render provides this)

2. Project Preparation

First, ensure your Django project has these files:
- requirements.txt
- render.yaml (optional but recommended)
- build.sh

Create requirements.txt:
```bash
pip freeze > requirements.txt
```

Ensure these packages are in requirements.txt:
```
django
gunicorn
whitenoise
psycopg2-binary
python-dotenv
dj-database-url
```

Create build.sh in your project root:
```bash
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
```

3. Project Configuration

Update settings.py:
```python
import os
import dj_database_url
from pathlib import Path

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='your-default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Database
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Add whitenoise middleware
MIDDLEWARE = [
    # ...other middleware...
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
```

4. Deployment Steps on Render.com

1. Log in to Render.com
2. Click "New +" and select "Web Service"
3. Connect your GitHub repository
4. Configure your web service:
   - Name: Your project name
   - Environment: Python 3
   - Build Command: `./build.sh`
   - Start Command: `gunicorn your_project.wsgi:application`
   - Select plan (Free or paid)

5. Environment Variables

Add these environment variables in Render.com dashboard:
- DATABASE_URL (Render will auto-set this)
- SECRET_KEY (Your Django secret key)
- PYTHON_VERSION (e.g., 3.9.0)
- RENDER=true

6. Database Setup

1. Create a new PostgreSQL database on Render:
   - Go to Dashboard → New + → PostgreSQL
   - Choose a name and plan
   - Create database
2. Copy the Internal Database URL
3. Add it as DATABASE_URL in your web service environment variables

7. Common Issues and Solutions

1. Static Files Not Loading:
- Ensure whitenoise is properly configured
- Check STATIC_ROOT and STATIC_URL settings
- Verify collectstatic runs during build

2. Database Connection Issues:
- Verify DATABASE_URL is correctly set
- Check database credentials
- Ensure psycopg2-binary is installed

3. Build Failures:
- Check build.sh permissions (`git update-index --chmod=+x build.sh`)
- Verify all requirements are listed in requirements.txt
- Check Python version compatibility





