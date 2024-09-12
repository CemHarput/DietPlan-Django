# DietPlan-Django

DietPlan is a Django-based application for tracking user diets using ChatGPT, body characteristics, and integration with AWS S3 for file storage.

## Features
- User authentication and registration
- CRUD operations for managing body traits (like weight, height, etc.)
- Integration with AWS S3 for file uploads
- Docker support for containerization
- Django REST Framework (DRF) for API development

## Project Structure



## Installation

1. Clone the repository:
```bash
git clone https://github.com/CemHarput/DietPlan-Django.git
cd DietPlan-Django

python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

export AWS_ACCESS_KEY_ID=your-access-key
export AWS_SECRET_ACCESS_KEY=your-secret-key

python manage.py migrate
python manage.py runserver

docker-compose up --build
