1. Prerequisites
- Ubuntu server (20.04 LTS or higher)
- SSH access to server
- Domain name (optional but recommended)
- Django project ready for deployment
- Basic Linux command knowledge

2. Initial Server Setup

Connect to your server:
```bash
ssh username@your_server_ip
```

Update server packages:
```bash
sudo apt update
sudo apt upgrade -y
```

Create a non-root user (if not already exists):
```bash
sudo adduser deployer
sudo usermod -aG sudo deployer
```

Set up SSH key authentication:
```bash
# On your local machine
ssh-keygen -t rsa -b 4096

# Copy key to server
ssh-copy-id deployer@your_server_ip
```

3. Install Required Software

Install Python and related tools:
```bash
sudo apt install python3 python3-pip python3-venv
sudo apt install nginx
sudo apt install postgresql postgresql-contrib
sudo apt install supervisor
sudo apt install git
```

4. PostgreSQL Database Setup

```bash
# Create database and user
sudo -u postgres psql

postgres=# CREATE DATABASE your_db_name;
postgres=# CREATE USER your_db_user WITH PASSWORD 'your_password';
postgres=# ALTER ROLE your_db_user SET client_encoding TO 'utf8';
postgres=# ALTER ROLE your_db_user SET default_transaction_isolation TO 'read committed';
postgres=# ALTER ROLE your_db_user SET timezone TO 'UTC';
postgres=# GRANT ALL PRIVILEGES ON DATABASE your_db_name TO your_db_user;
postgres=# \q
```

5. Project Setup

Create project directory:
```bash
sudo mkdir /var/www/
sudo chown deployer:deployer /var/www/
cd /var/www/
```

Clone your project:
```bash
git clone https://github.com/your-username/your-project.git
cd your-project
```

Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
pip install gunicorn
```

6. Environment Variables

Create .env file:
```bash
nano .env
```

Add environment variables:
```
DEBUG=False
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://your_db_user:your_password@localhost:5432/your_db_name
ALLOWED_HOSTS=your_domain.com,www.your_domain.com,your_server_ip
```

7. Django Project Configuration

Update settings.py for production:
```python
import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

# Database
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL')
    )
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

8. Gunicorn Setup

Create Gunicorn socket file:
```bash
sudo nano /etc/systemd/system/gunicorn.socket
```

Add:
```ini
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

Create Gunicorn service file:
```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Add:
```ini
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=deployer
Group=www-data
WorkingDirectory=/var/www/your-project
Environment="PATH=/var/www/your-project/venv/bin"
ExecStart=/var/www/your-project/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          your_project.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start and enable Gunicorn:
```bash
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

9. Nginx Configuration

Create Nginx configuration:
```bash
sudo nano /etc/nginx/sites-available/your-project
```

Add:
```nginx
server {
    listen 80;
    server_name your_domain.com www.your_domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root /var/www/your-project;
    }

    location /media/ {
        root /var/www/your-project;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```

Enable the site:
```bash
sudo ln -s /etc/nginx/sites-available/your-project /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

10. SSL Configuration (Using Certbot)

Install Certbot:
```bash
sudo apt install certbot python3-certbot-nginx
```

Obtain SSL certificate:
```bash
sudo certbot --nginx -d your_domain.com -d www.your_domain.com
```

11. Final Deployment Steps

Collect static files:
```bash
python manage.py collectstatic
```

Apply migrations:
```bash
python manage.py migrate
```

Set proper permissions:
```bash
sudo chown -R deployer:www-data /var/www/your-project
sudo chmod -R 755 /var/www/your-project
```

12. Maintenance and Monitoring

Setup basic firewall:
```bash
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw enable
```

View logs:
```bash
# Nginx error logs
sudo tail -f /var/log/nginx/error.log

# Gunicorn logs
sudo journalctl -u gunicorn
```

13. Deployment Script (Optional)

Create deploy.sh:
```bash
#!/bin/bash
cd /var/www/your-project
source venv/bin/activate
git pull
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --no-input
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

Make it executable:
```bash
chmod +x deploy.sh
```

14. Common Issues and Solutions

1. Permission Issues:
```bash
sudo chown -R deployer:www-data /var/www/your-project
sudo chmod -R 755 /var/www/your-project
sudo chmod 660 /var/www/your-project/db.sqlite3  # if using SQLite
```

2. Nginx/Gunicorn not working:
```bash
# Check status
sudo systemctl status nginx
sudo systemctl status gunicorn

# Check logs
sudo tail -f /var/log/nginx/error.log
sudo journalctl -u gunicorn
```

3. Static files not loading:
```bash
# Verify STATIC_ROOT in settings.py
# Rerun collectstatic
python manage.py collectstatic --clear --no-input
# Check Nginx configuration
```