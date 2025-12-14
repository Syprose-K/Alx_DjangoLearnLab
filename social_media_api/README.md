# Social Media API

## Setup
1. `pip install -r requirements.txt`
2. `python manage.py migrate`
3. `python manage.py createsuperuser`
4. `python manage.py runserver`

## Endpoints
- `POST /api/accounts/register/` → Register a new user.
- `POST /api/accounts/login/` → Login and get token.
- `GET /api/accounts/profile/` → Get user profile (token required).

## User Model
- `username`
- `email`
- `bio`
- `profile_picture`
- `followers` (ManyToMany to self)
